# Kermit the Frog Multimedia Experience

This project brings the iconic Kermit the Frog to your screen with a fullscreen animated GIF and looping MP3 audio. It's a fun little application that demonstrates how to combine multimedia elements using Python.

**Run the Script:**
    A: Firstly, Install the dependencies in the requirements.txt file.
    
    ```bash
    pip install -r requirements.txt
    ```
    B: Now all you do is fun the Kermit script!

    ```bash
    python kermit.py
    ```
## Password

*   The application will launch in fullscreen mode, displaying the animated GIF and playing the sound.
*   Press any key (except Control, Command, and Shift together) to see the "What's the Secret?" message for 3 seconds.
*   To exit, press **(Command) ⌘ + (Control) ⌃ + Left Shift** simultaneously. 

## Preview

Here's a glimpse of what you'll see (make sure you're viewing this on GitHub to see the animation):

![Kermit the Frog](files/kermit.gif)

## Audio

You can listen to the Kermit the Frog sound here: [kermit.mp3](files/kermit.mp3)

[Listen on External Host](https://www.example-audio-host.com/kermit-audio)

## Features

*   **Fullscreen Animated GIF Display:** Showcases a fullscreen, looping, animated GIF of Kermit the Frog (as you can see above!). The image is automatically scaled to fit your screen while maintaining its original aspect ratio.
*   **Looping MP3 Audio:** Plays a Kermit the Frog MP3 sound file in a continuous loop.
*   **Secret Exit Combination:** Provides a hidden way to exit the application by pressing a specific key combination: **Control + Command + Shift** (on macOS).
*   **Interactive Message:** Displays a "What's the Secret?" message for 3 seconds when any key (other than the secret exit combination) is pressed.
*   **Hidden Mouse Cursor:** Hides the mouse cursor while the application is running in fullscreen mode.

## Requirements

*   **Python 3:** This project is written in Python 3. Make sure you have Python 3 installed on your system. You can check your Python version by running `python --version` or `python3 --version` in your terminal.
*   **Libraries:**
    *   **pygame:** Used for audio playback.
    *   **Pillow (PIL):** Used for image processing and handling the animated GIF.
    *   **tkinter:** Used for creating the fullscreen window and handling user input.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    (Replace `<repository_url>` with the actual URL of your GitHub repository and `<repository_directory>` with the name of the directory.)

2.  **Install Dependencies:**
    ```bash
    pip install pygame Pillow
    ```

## Usage

1.  **Place Files:** Ensure that the following files are in the same directory as the `kermit.py` script:
    *   `kermit.mp3`: The Kermit the Frog audio file.
    *   `kermit.gif`: The animated GIF of Kermit the Frog (the one displayed above!).

2.  **Run the Script:**
    A: Firstly, Install the dependencies in the requirements.txt file.

    ```bash
    pip install -r requirements.txt
    ```
    B: Now all you do is fun the Kermit script!

    ```bash
    python kermit.py
    ```

3.  **Interaction:**
    *   The application will launch in fullscreen mode, displaying the animated GIF and playing the sound.
    *   Press any key (except Control, Command, and Shift together) to see the "What's the Secret?" message for 3 seconds.
    *   To exit, press **Control + Command + Shift** simultaneously.

## Code Structure

The `kermit.py` script is organized into the `KermitApp` class, which handles the various functionalities:

*   `__init__()`: Initializes the application, loads the image and sound, creates the window, and sets up event bindings.
*   `bind_keys()`: Binds key press and release events to their respective handler functions.
*   `on_key_press()`, `on_key_release()`, `on_any_key_press()`: Handle key press and release events, including checking for the secret exit combination and triggering the message display.
*   `check_secret_combination()`: Checks if the secret key combination is pressed.
*   `play_sound_loop()`: Plays the sound file in a loop (runs in a separate thread).
*   `update_image()`: Updates the displayed GIF frame to create the animation (called repeatedly using `tkinter`'s `after()` method).
*   `update_message()`: Manages the display and hiding of the "What's the Secret?" message.
*   `start()`: Starts the sound thread, the image animation, message updates, and the `tkinter` main loop.
*   `stop()`: Stops the sound, destroys the window, and terminates the application.

## Troubleshooting

*   **MP3 Playback Issues:** If you encounter problems with MP3 playback, you might need to install the `mpg123` library, which can sometimes improve Pygame's MP3 support. Installation instructions for `mpg123` vary by operating system (e.g., `brew install mpg123` on macOS with Homebrew, `sudo apt-get install mpg123` on Ubuntu/Debian).
*   **File Not Found:** Double-check that `kermit.mp3` and `kermit.gif` are in the same directory as the `kermit.py` script.

## Contributing

Feel free to fork this repository and submit pull requests with enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.