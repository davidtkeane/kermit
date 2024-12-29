import pygame
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import time
import sys

# Configuration
SOUND_FILE = "files/kermit.mp3"
IMAGE_FILE = "files/kermit.gif"

SECRET_KEY_COMBINATION = {
    "<Control_L>",  # Left Control
    "<Meta_L>",     # Left Command (macOS)
    "<Shift_L>",    # Left Shift
}
MESSAGE_DURATION = 3  # Seconds for the message to display

class KermitApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.configure(background='black')
        self.root.focus_set()

        # --- Hide Mouse Cursor ---
        self.root.config(cursor="none")  # Add this line
        
        # --- Load and Resize the Image ---
        try:
            self.original_image = Image.open(IMAGE_FILE)
            # Get screen dimensions
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            # Resize image to fit screen, maintaining aspect ratio
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
            self.animation_delay = self.original_image.info.get("duration", 100)  # Delay from GIF, default to 100ms
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

        # --- Secret Key Handling ---
        self.pressed_keys = set()
        self.bind_keys()

        # --- State Variables ---
        self.running = True
        self.show_message = False
        self.message_timer = 0

    def bind_keys(self):
        for key in SECRET_KEY_COMBINATION:
            self.root.bind(key, self.on_key_press)
            self.root.bind(f"<KeyRelease-{key[-1]}>", self.on_key_release)

        # Bind any key press to show the message
        self.root.bind("<KeyPress>", self.on_any_key_press)

    def on_key_press(self, event):
        self.pressed_keys.add(event.keysym)
        self.check_secret_combination()

    def on_key_release(self, event):
        if event.keysym in self.pressed_keys:
            self.pressed_keys.remove(event.keysym)

    def on_any_key_press(self, event):
        # Show the message if any key is pressed (except the secret combination)
        if not all(key in self.pressed_keys for key in {"Control_L", "Meta_L", "Shift_L"}):
            self.show_message = True
            self.message_timer = time.time()
            self.update_message()

    def check_secret_combination(self):
        if all(key in self.pressed_keys for key in {"Control_L", "Meta_L", "Shift_L"}):
            self.stop()

    def play_sound_loop(self):
        while self.running:
            if self.sound:
                self.sound.play()
                time.sleep(self.sound.get_length())
            else:
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() and self.running:
                    time.sleep(0.1)

    def update_image(self):
        if self.running:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image_label.config(image=self.frames[self.frame_index])
            self.root.after(self.animation_delay, self.update_image)

    def update_message(self):
        if self.show_message:
            self.message_label.config(text="What's the Secret?")
            elapsed_time = time.time() - self.message_timer
            if elapsed_time > MESSAGE_DURATION:
                self.message_label.config(text="")
                self.show_message = False
        if self.running:
            self.root.after(100, self.update_message)  # Check every 100ms

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
    app = KermitApp()
    app.start()