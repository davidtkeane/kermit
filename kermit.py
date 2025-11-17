#!/usr/bin/env python3
# Created by Ranger
# Cross-platform support for macOS and Linux

# Import Modules
import pygame
import tkinter as tk
import threading
import time
import sys
import platform
import argparse
from PIL import Image, ImageTk, ImageSequence

# Configuration
SOUND_FILE = "files/kermit.mp3"
IMAGE_FILE = "files/kermit.gif"
VERSION = "3.0.0"

# Detect operating system
CURRENT_OS = platform.system()

# Platform-specific key bindings
if CURRENT_OS == "Darwin":  # macOS
    SECRET_KEY_COMBINATION = {
        "<Control_L>",  # Left Control (Control) ⌃
        "<Meta_L>",     # Left Command (Command) ⌘
        "<Shift_L>",    # Left Shift
    }
    SECRET_KEYS_DISPLAY = "Control + Command + Left Shift"

    PAUSE_KEY_COMBINATION = {
        "<Control_L>",  # Left Control (Control) ⌃
        "<Meta_L>",     # Left Command (Command) ⌘
        "p",            # Key 'p'
    }
    PAUSE_KEYS_DISPLAY = "Control + Command + P"

    SECRET_KEYSYMS = {"Control_L", "Meta_L", "Shift_L"}
    PAUSE_KEYSYMS = {"Control_L", "Meta_L", "p"}

else:  # Linux (Kali, Ubuntu, etc.) and others
    SECRET_KEY_COMBINATION = {
        "<Control_L>",  # Left Control
        "<Alt_L>",      # Left Alt (more reliable in VMs than Super)
        "<Shift_L>",    # Left Shift
    }
    SECRET_KEYS_DISPLAY = "Ctrl + Alt + Left Shift"

    PAUSE_KEY_COMBINATION = {
        "<Control_L>",  # Left Control
        "<Alt_L>",      # Left Alt
        "p",            # Key 'p'
    }
    PAUSE_KEYS_DISPLAY = "Ctrl + Alt + P"

    SECRET_KEYSYMS = {"Control_L", "Alt_L", "Shift_L"}
    PAUSE_KEYSYMS = {"Control_L", "Alt_L", "p"}

MESSAGE_DURATION = 3  # Seconds for the message to display


def show_help():
    """Display help information with platform-specific controls."""
    help_text = f"""
Kermit Screen Lock Experience v{VERSION}
{'=' * 40}

Platform: {CURRENT_OS}

CONTROLS:
  Exit (Secret):  {SECRET_KEYS_DISPLAY}
  Pause/Resume:   {PAUSE_KEYS_DISPLAY}
  Volume Up:      Up Arrow
  Volume Down:    Down Arrow
  Show Message:   Any other key

USAGE:
  python kermit.py          Launch the application
  python kermit.py --help   Show this help message
  python kermit.py -h       Show this help message

REQUIREMENTS:
  - Python 3.7+
  - pygame
  - Pillow (PIL)
  - tkinter (python3-tk on Linux)

FILES:
  - files/kermit.mp3   Audio file
  - files/kermit.gif   Animated GIF
"""
    print(help_text)
    sys.exit(0)

class KermitApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')
        self.root.focus_set()
        self.root.config(cursor="none")  # Hide mouse cursor

        # --- Load and Resize the Image ---
        try:
            self.original_image = Image.open(IMAGE_FILE)
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

            self.frames = [ImageTk.PhotoImage(frame.resize((new_width, new_height)))
                           for frame in ImageSequence.Iterator(self.original_image)]

            self.frame_index = 0
            self.animation_delay = self.original_image.info.get("duration", 100)
        except Exception as e:
            print(f"Error loading or processing image: {e}")
            sys.exit(1)

        # --- Create Image Label ---
        self.image_label = tk.Label(self.root, image=self.frames[0], bd=0, highlightthickness=0)
        self.image_label.pack()

        # --- Initialize Pygame for Sound ---
        pygame.mixer.init()
        try:
            self.sound = pygame.mixer.Sound(SOUND_FILE)
        except pygame.error as e:
            print(f"Error loading MP3 with pygame: {e}")
            print("Attempting to play MP3 using pygame.mixer.music...")
            try:
                pygame.mixer.music.load(SOUND_FILE)
                self.sound = None
            except pygame.error as e:
                print(f"Error loading MP3 with pygame.mixer.music: {e}")
                sys.exit(1)

        # --- Message Label ---
        self.message_label = tk.Label(self.root, text="", font=("Arial", 48), fg="white", bg="black")
        self.message_label.pack()

        # --- Key Handling ---
        self.pressed_keys = set()
        self.bind_keys()

        # --- State Variables ---
        self.running = True
        self.paused = False
        self.show_message = False
        self.message_timer = 0
 
    def bind_keys(self):
        for key in SECRET_KEY_COMBINATION:
            self.root.bind(key, self.on_key_press)
            self.root.bind(f"<KeyRelease-{key[-1]}>", self.on_key_release)

        for key in PAUSE_KEY_COMBINATION:
            self.root.bind(key, self.on_key_press)
            self.root.bind(f"<KeyRelease-{key[-1]}>", self.on_key_release)
        # Bind any key press to show the message
        self.root.bind("<KeyPress>", self.on_any_key_press)
        self.root.bind("<Up>", self.increase_volume)
        self.root.bind("<Down>", self.decrease_volume)
    
    def increase_volume(self, event):
        if self.sound:
            current_volume = self.sound.get_volume()
            new_volume = min(current_volume + 0.1, 1.0)  # Max volume is 1.0
            self.sound.set_volume(new_volume)
        else:
            current_volume = pygame.mixer.music.get_volume()
            new_volume = min(current_volume + 0.1, 1.0)
            pygame.mixer.music.set_volume(new_volume)

    def decrease_volume(self, event):
        if self.sound:
            current_volume = self.sound.get_volume()
            new_volume = max(current_volume - 0.1, 0.0)  # Min volume is 0.0
            self.sound.set_volume(new_volume)
        else:
            current_volume = pygame.mixer.music.get_volume()
            new_volume = max(current_volume - 0.1, 0.0)
            pygame.mixer.music.set_volume(new_volume)

    def on_key_press(self, event):
        if event.keysym in ["<Command>", "<Tab>"]:
            return
        
        self.pressed_keys.add(event.keysym)
        self.check_secret_combination()
        self.check_pause_combination()
        # self.on_any_key_press(event)  # Call this method to handle any other key presses

    def on_key_release(self, event):
        if event.keysym in self.pressed_keys:
            self.pressed_keys.remove(event.keysym)

    def on_any_key_press(self, event):
        # Show the message if any key is pressed (except the secret combination)
        if not all(key in self.pressed_keys for key in PAUSE_KEYSYMS):
            self.show_message = True
            self.message_timer = time.time()
            self.update_message()

    def check_secret_combination(self):
        if all(key in self.pressed_keys for key in SECRET_KEYSYMS):
            self.stop()

    def check_pause_combination(self):
        if all(key in self.pressed_keys for key in PAUSE_KEYSYMS):
            self.toggle_pause()

    def toggle_pause(self):
        self.paused = not self.paused
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

    def play_sound_loop(self):
        while self.running:
            if not self.paused:
                if self.sound:
                    self.sound.play()
                    time.sleep(self.sound.get_length())
                else:
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() and self.running and not self.paused:
                        time.sleep(0.1)
            else:
                time.sleep(0.1)  # Check every 100ms when paused

    def update_image(self):
        if self.running:
            if not self.paused:
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image_label.config(image=self.frames[self.frame_index])
            self.root.after(self.animation_delay if not self.paused else 100, self.update_image)

    def update_message(self):
        if self.show_message:
            self.message_label.config(text="What's the Secret?")
            elapsed_time = time.time() - self.message_timer
            if elapsed_time > MESSAGE_DURATION:
                self.message_label.config(text="")
                self.show_message = False
        if self.running:
            self.root.after(100, self.update_message)

    def start(self):
        # --- Start Sound Thread ---
        sound_thread = threading.Thread(target=self.play_sound_loop)
        sound_thread.daemon = True
        sound_thread.start()

        # --- Start Image Animation ---
        self.update_image()

        # --- Start Message Update ---
        self.update_message()

        # --- Start the Tkinter Main Loop ---
        self.root.mainloop()

    def stop(self):
        self.running = False
        if self.sound:
            pygame.mixer.stop()
        else:
            pygame.mixer.music.stop()
        self.root.destroy()

if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        show_help()

    print(f"Kermit Screen Lock v{VERSION}")
    print(f"Platform: {CURRENT_OS}")
    print(f"Exit: {SECRET_KEYS_DISPLAY}")
    print(f"Pause: {PAUSE_KEYS_DISPLAY}")
    print("Starting...")

    app = KermitApp()
    app.start()