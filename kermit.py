#!/usr/bin/env python3
# Created by Ranger
# Cross-platform support for macOS and Linux

# Import Modules
import os
import warnings
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")  # Hide pygame's startup banner
warnings.filterwarnings("ignore", message="pkg_resources is deprecated")  # Noisy pygame import warning

import pygame
import tkinter as tk
import signal
import sys
import platform
import argparse
from pathlib import Path
from PIL import Image, ImageTk, ImageSequence

# Default Configuration
BASE_DIR = Path(__file__).resolve().parent  # Find files/ next to kermit.py, from any directory
DEFAULT_SOUND_FILE = str(BASE_DIR / "files" / "kermit.mp3")
DEFAULT_IMAGE_FILE = str(BASE_DIR / "files" / "kermit.gif")
DEFAULT_VOLUME = 1.0
VERSION = "3.1.1"

# Detect operating system
CURRENT_OS = platform.system()

# Platform-specific key bindings
# Pause is the same physical keys on both platforms: Left Control + Left Option/Alt + P
PAUSE_KEY = "p"
PAUSE_KEYSYMS = {"Control_L", "Alt_L", PAUSE_KEY}
VOLUME_KEYSYMS = {"Up", "Down"}

if CURRENT_OS == "Darwin":  # macOS
    # Tk on macOS reports Left Command as Meta_L (and Left Option as Alt_L)
    SECRET_KEYSYMS = {"Control_L", "Meta_L"}
    SECRET_KEYS_DISPLAY = "Control + Command"
    PAUSE_KEYS_DISPLAY = "Control + Option + P"
else:  # Linux (Kali, Ubuntu, etc.) and others
    SECRET_KEYSYMS = {"Control_L", "Alt_L", "Shift_L"}  # Alt is more reliable in VMs than Super
    SECRET_KEYS_DISPLAY = "Ctrl + Alt + Left Shift"
    PAUSE_KEYS_DISPLAY = "Ctrl + Alt + P"

COMBO_MODIFIERS = (SECRET_KEYSYMS | PAUSE_KEYSYMS) - {PAUSE_KEY}

MESSAGE_DURATION = 3  # Seconds for the message to display
MIN_FRAME_DELAY = 20  # Milliseconds - stops GIFs with 0ms frames from hogging the CPU


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=f"Kermit Screen Lock Experience v{VERSION}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
CONTROLS:
  Exit (Secret):  {SECRET_KEYS_DISPLAY}
  Pause/Resume:   {PAUSE_KEYS_DISPLAY}
  Volume Up:      Up Arrow
  Volume Down:    Down Arrow
  Show Message:   Any other key

EXAMPLES:
  python kermit.py                           # Default settings
  python kermit.py --gif custom.gif          # Custom GIF
  python kermit.py --audio music.mp3         # Custom audio
  python kermit.py --volume 0.5              # 50% volume
  python kermit.py --no-sound                # Silent mode
  python kermit.py --gif cat.gif --no-sound  # Custom GIF, no sound

Platform: {CURRENT_OS}
"""
    )

    parser.add_argument(
        "--gif",
        type=str,
        default=DEFAULT_IMAGE_FILE,
        help="Path to GIF file (default: files/kermit.gif)"
    )

    parser.add_argument(
        "--audio",
        type=str,
        default=DEFAULT_SOUND_FILE,
        help="Path to audio file (default: files/kermit.mp3)"
    )

    parser.add_argument(
        "--volume",
        type=float,
        default=DEFAULT_VOLUME,
        help=f"Initial volume level 0.0-1.0 (default: {DEFAULT_VOLUME})"
    )

    parser.add_argument(
        "--no-sound",
        action="store_true",
        help="Run without audio (silent mode)"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"Kermit Screen Lock v{VERSION}"
    )

    args = parser.parse_args()

    # Validate volume range
    if args.volume < 0.0 or args.volume > 1.0:
        parser.error("Volume must be between 0.0 and 1.0")

    return args


def validate_files(gif_path, audio_path, no_sound):
    """Check if required files exist and provide helpful error messages."""
    errors = []

    # Check GIF file
    if not os.path.isfile(gif_path):
        errors.append(f"GIF file not found: {gif_path}")
        if gif_path == DEFAULT_IMAGE_FILE:
            errors.append("  -> Make sure 'files/kermit.gif' exists next to kermit.py")
        else:
            errors.append("  -> Check that the file path is correct")

    # Check audio file (only if sound is enabled)
    if not no_sound and not os.path.isfile(audio_path):
        errors.append(f"Audio file not found: {audio_path}")
        if audio_path == DEFAULT_SOUND_FILE:
            errors.append("  -> Make sure 'files/kermit.mp3' exists next to kermit.py")
        else:
            errors.append("  -> Check that the file path is correct")
        errors.append("  -> Or use --no-sound to run without audio")

    if errors:
        print("ERROR: Missing required files\n")
        for error in errors:
            print(error)
        print(f"\nCurrent directory: {os.getcwd()}")
        sys.exit(1)


class KeyTracker:
    """Tracks which keys are held down and reports when a key combination is pressed."""

    def __init__(self):
        self.pressed_keys = set()
        self.pause_armed = True  # Stops a held P from toggling pause over and over

    def press(self, keysym):
        """Record a key press. Returns "secret", "pause", "volume", "combo", "repeat" or "other"."""
        keysym = keysym.lower() if len(keysym) == 1 else keysym
        if keysym in self.pressed_keys:
            return "repeat"  # macOS auto-repeat sends presses without releases
        self.pressed_keys.add(keysym)

        if SECRET_KEYSYMS <= self.pressed_keys:
            return "secret"
        if PAUSE_KEYSYMS <= self.pressed_keys:
            if not self.pause_armed:
                return "repeat"  # Linux auto-repeat sends release + press pairs
            self.pause_armed = False
            return "pause"
        if keysym in VOLUME_KEYSYMS:
            return "volume"
        if keysym in COMBO_MODIFIERS:
            return "combo"  # Part of a combination - don't show the message
        return "other"

    def release(self, keysym):
        """Record a key release."""
        keysym = keysym.lower() if len(keysym) == 1 else keysym
        self.pressed_keys.discard(keysym)
        if keysym in PAUSE_KEYSYMS - {PAUSE_KEY}:
            self.pause_armed = True  # Letting go of Control/Alt allows the next pause toggle

    def clear(self):
        """Forget all held keys (e.g. when the window loses focus and misses releases)."""
        self.pressed_keys.clear()
        self.pause_armed = True


class KermitApp:
    def __init__(self, gif_path=DEFAULT_IMAGE_FILE, audio_path=DEFAULT_SOUND_FILE,
                 initial_volume=DEFAULT_VOLUME, no_sound=False):
        self.gif_path = gif_path
        self.audio_path = audio_path
        self.initial_volume = initial_volume
        self.no_sound = no_sound

        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')
        self.root.focus_set()
        self.root.config(cursor="none")  # Hide mouse cursor

        # --- Load and Resize the Image ---
        try:
            self.original_image = Image.open(self.gif_path)
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            img_width, img_height = self.original_image.size
            aspect_ratio = img_width / img_height
            if screen_width / aspect_ratio <= screen_height:
                new_width = screen_width
                new_height = int(screen_width / aspect_ratio)
            else:
                new_height = screen_height
                new_width = int(screen_height * aspect_ratio)

            default_delay = self.original_image.info.get("duration", 100)
            self.frames = []
            self.frame_delays = []
            for frame in ImageSequence.Iterator(self.original_image):
                resized = frame.convert("RGBA").resize((new_width, new_height), Image.Resampling.LANCZOS)
                self.frames.append(ImageTk.PhotoImage(resized))
                delay = frame.info.get("duration", default_delay) or default_delay
                self.frame_delays.append(max(int(delay), MIN_FRAME_DELAY))

            self.frame_index = 0
        except Exception as e:
            print(f"Error loading or processing image: {e}")
            sys.exit(1)

        # --- Create Image Label (centred on screen) ---
        self.image_label = tk.Label(self.root, image=self.frames[0], bd=0, highlightthickness=0)
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- Initialize Pygame for Sound ---
        self.sound = None
        if not self.no_sound:
            pygame.mixer.init()
            try:
                self.sound = pygame.mixer.Sound(self.audio_path)
                self.sound.set_volume(self.initial_volume)
            except pygame.error as e:
                print(f"Error loading audio with pygame.mixer.Sound: {e}")
                print("Attempting to load using pygame.mixer.music...")
                try:
                    pygame.mixer.music.load(self.audio_path)
                    pygame.mixer.music.set_volume(self.initial_volume)
                    self.sound = None
                except pygame.error as e:
                    print(f"Error loading audio with pygame.mixer.music: {e}")
                    sys.exit(1)
        else:
            print("Sound disabled (--no-sound)")

        # --- Message Label (overlaid near the bottom, hidden until a key is pressed) ---
        self.message_label = tk.Label(self.root, text="What's the Secret?", font=("Arial", 48),
                                      fg="white", bg="black")
        self.message_hide_id = None

        # --- Key Handling ---
        self.keys = KeyTracker()
        self.bind_keys()

        # --- State Variables ---
        self.running = True
        self.paused = False

    def bind_keys(self):
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)
        self.root.bind("<FocusOut>", lambda event: self.keys.clear())

    def change_volume(self, step):
        if self.no_sound:
            return  # No volume control in silent mode

        if self.sound:
            new_volume = min(max(self.sound.get_volume() + step, 0.0), 1.0)
            self.sound.set_volume(new_volume)
        else:
            new_volume = min(max(pygame.mixer.music.get_volume() + step, 0.0), 1.0)
            pygame.mixer.music.set_volume(new_volume)

    def on_key_press(self, event):
        result = self.keys.press(event.keysym)
        if result == "secret":
            self.stop()
        elif result == "pause":
            self.toggle_pause()
        elif result == "volume":
            self.change_volume(0.1 if event.keysym == "Up" else -0.1)
        elif result == "other":
            self.show_message()

    def on_key_release(self, event):
        self.keys.release(event.keysym)

    def show_message(self):
        """Show "What's the Secret?" for MESSAGE_DURATION seconds."""
        self.message_label.place(relx=0.5, rely=0.95, anchor="s")
        if self.message_hide_id:
            self.root.after_cancel(self.message_hide_id)
        self.message_hide_id = self.root.after(MESSAGE_DURATION * 1000, self.hide_message)

    def hide_message(self):
        self.message_label.place_forget()
        self.message_hide_id = None

    def toggle_pause(self):
        self.paused = not self.paused
        if not self.no_sound:
            if self.paused:
                if self.sound:
                    pygame.mixer.pause()
                else:
                    pygame.mixer.music.pause()
            else:
                if self.sound:
                    pygame.mixer.unpause()
                else:
                    pygame.mixer.music.unpause()

    def start_sound(self):
        if self.no_sound:
            return

        # loops=-1 repeats forever, so no background thread is needed
        if self.sound:
            self.sound.play(loops=-1)
        else:
            pygame.mixer.music.play(loops=-1)

    def update_image(self):
        if self.running:
            if not self.paused:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image_label.config(image=self.frames[self.frame_index])
            delay = self.frame_delays[self.frame_index] if not self.paused else 100
            self.root.after(delay, self.update_image)

    def start(self):
        # --- Stop cleanly on Ctrl+C in the terminal ---
        signal.signal(signal.SIGINT, lambda signum, frame: self.stop())

        # --- Start Sound ---
        self.start_sound()

        # --- Start Image Animation ---
        self.update_image()

        # --- Start the Tkinter Main Loop ---
        self.root.mainloop()

    def stop(self):
        if not self.running:
            return
        self.running = False
        if not self.no_sound:
            if self.sound:
                pygame.mixer.stop()
            else:
                pygame.mixer.music.stop()
            pygame.mixer.quit()
        self.root.destroy()

if __name__ == "__main__":
    # Parse command line arguments
    args = parse_arguments()

    # Validate that required files exist
    validate_files(args.gif, args.audio, args.no_sound)

    # Display startup information
    print(f"Kermit Screen Lock v{VERSION}")
    print(f"Platform: {CURRENT_OS}")
    print(f"Exit: {SECRET_KEYS_DISPLAY}")
    print(f"Pause: {PAUSE_KEYS_DISPLAY}")
    print(f"GIF: {args.gif}")
    if not args.no_sound:
        print(f"Audio: {args.audio}")
        print(f"Volume: {args.volume:.0%}")
    else:
        print("Audio: DISABLED (--no-sound)")
    print("Starting...")

    app = KermitApp(
        gif_path=args.gif,
        audio_path=args.audio,
        initial_volume=args.volume,
        no_sound=args.no_sound
    )
    app.start()
