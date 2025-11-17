# Kermit the Frog Screen Lock Experience

<p align="left">
This project brings the iconic Kermit the Frog to your screen with a fullscreen animated GIF and looping MP3 audio. It's a fun little application that demonstrates how to combine multimedia elements using Python.

[![Kermit ScreenSaver](https://img.shields.io/badge/kermit-screensaver-blue)](https://github.com/davidtkeane/kermit)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-3.0.0-orange)

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/kermit?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/davidtkeane/kermit?authorFilter=davidtkeane)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/kermit?style=flat-square)
![GitHub commit status](https://img.shields.io/github/checks-status/davidtkeane/kermit/fff3b211e20881582eeea4e035dcdd452548ed7a)

## Preview

Here's a glimpse of what you'll see (make sure you're viewing this on GitHub to see the animation):

![Kermit the Frog](files/kermit.gif)

### Badges

![Windows-Badge](https://img.shields.io/badge/Microsoft-Windows%2011-0078D6?logo=windows&logoColor=0078D6&labelColor=white)
![AppleMac-Badge](https://img.shields.io/badge/Apple-macOS-000000?logo=apple&logoColor=white&labelColor=black)
![Linux-Badge](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black&labelColor=white)

## Quick Setup and Running and Setup of the Script - See more info below:

A: Firstly, Install the dependencies in the requirements.txt file.
    
```bash
pip install -r requirements.txt
```
B: Now all you do is fun the Kermit script!

```bash
python kermit.py
```

### Time @ Work!

[![CodeTime Badge](https://img.shields.io/endpoint?style=social&color=222&url=https%3A%2F%2Fapi.codetime.dev%2Fshield%3Fid%3D26388%26project%3D%26in=0)](https://codetime.dev)

## Controls

### Exit (Secret Password)

*   The application will launch in fullscreen mode, displaying the animated GIF and playing the sound.
*   Press any key to see the "What's the Secret?" message for 3 seconds.
*   To exit:
    *   **macOS:** **(Control) ⌃ + (Option) ⌥ + Left Shift**
    *   **Linux:** **Ctrl + Alt + Left Shift**
    *   **MacBook keyboard:** **Control + Option + Left Shift** (same keys on both platforms!)

### Pause/Resume

*   To pause/unpause:
    *   **macOS:** **(Control) ⌃ + (Option) ⌥ + P**
    *   **Linux:** **Ctrl + Alt + P**
    *   **MacBook keyboard:** **Control + Option + P** (same keys on both platforms!)

### Volume

*   **Up Arrow** - Increase volume
*   **Down Arrow** - Decrease volume

### Help

*   Run `python kermit.py --help` to see platform-specific controls

## Audio

You can listen to the Kermit the Frog sound here: [kermit.mp3](files/kermit.mp3)

[Listen on External Host](https://www.example-audio-host.com/kermit-audio)

### Github Commits

![GitHub last commit](https://img.shields.io/github/last-commit/davidtkeane/Sleep-CLI?style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/davidtkeane/Sleep-CLI?authorFilter=davidtkeane)
![GitHub issues](https://img.shields.io/github/issues-raw/davidtkeane/Sleep-CLI?style=flat-square)
![GitHub Sponsors](https://img.shields.io/github/sponsors/davidtkeane)

## Features

*   **Cross-Platform Support:** Works on macOS and Linux (Kali/Debian/Ubuntu) with automatic platform detection and appropriate key bindings.

*   **Fullscreen Animated GIF Display:** Showcases a fullscreen, looping, animated GIF of Kermit the Frog (as you can see above!). The image is automatically scaled to fit your screen while maintaining its original aspect ratio.

*   **Looping MP3 Audio:** Plays a Kermit the Frog MP3 sound file in a continuous loop.

*   **Secret Exit Combination:** Provides a hidden way to exit the application by pressing a platform-specific key combination (see [Controls](#controls) section).

*   **Pause/Resume:** Pause and resume both audio and animation with a key combination.

*   **Volume Control:** Adjust volume with Up/Down arrow keys.

*   **Interactive Message:** Displays a "What's the Secret?" message for 3 seconds when any key (other than the secret exit combination) is pressed.

*   **Hidden Mouse Cursor:** Hides the mouse cursor while the application is running in fullscreen mode.

*   **Command-Line Help:** Run with `--help` to see platform-specific controls and requirements.

## Requirements

*   **Python 3.7+:** This project is written in Python 3. Make sure you have Python 3.7 or higher installed on your system. You can check your Python version by running `python --version` or `python3 --version` in your terminal.

*   **Python Libraries:**

    *   **pygame:** Used for audio playback.
    *   **Pillow (PIL):** Used for image processing and handling the animated GIF.
    *   **tkinter:** Used for creating the fullscreen window and handling user input.

*   **System Packages (Linux):**

    *   **python3-tk:** Required for tkinter GUI (`sudo apt install python3-tk`)
    *   **Optional:** mpg123, libsdl2-mixer for better audio support

### My Other Cool Scripts.

[![Gmail Multi-Account CLI](https://img.shields.io/badge/Gmail-Multi--Account%20CLI-green?logo=gmail&logoColor=white&labelColor=EA4335)](https://github.com/davidtkeane/gmail-multi-cli)
[![Sleep CLI](https://img.shields.io/badge/Sleep-CLI-blue)](https://github.com/davidtkeane/Sleep-CLI)
[![PhoneBook CLI](https://img.shields.io/badge/PhoneBook-CLI-blue)](https://github.com/davidtkeane/PhoneBook-CLI)
[![Kermit ScreenSaver](https://img.shields.io/badge/kermit-screensaver-blue)](https://github.com/davidtkeane/kermit)

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    (Replace `<repository_url>` with the actual URL of your GitHub repository and `<repository_directory>` with the name of the directory.)

2.  **Install System Dependencies:**

    **macOS:**
    ```bash
    # tkinter is included with Python from python.org or Homebrew
    # If missing:
    brew install python-tk@3.x
    ```

    **Linux (Kali/Debian/Ubuntu):**
    ```bash
    sudo apt update
    sudo apt install python3-tk
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    Or manually:
    ```bash
    pip install pygame Pillow
    ```

### Socials

[![Github](https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/davidtkeane)
[![X](https://img.shields.io/badge/twitter-%2300acee.svg?&style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/davidtkeane)
[![Linkedin](https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/)

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
    *   Press any key to see the "What's the Secret?" message for 3 seconds.
    *   To exit: **See [Controls](#controls) section above for platform-specific keys**
    *   The script auto-detects your OS and shows the correct key bindings on startup.

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
*   **File Not Found:** Double-check that `kermit.mp3` and `kermit.gif` are in the `files/` subdirectory relative to the `kermit.py` script.
*   **tkinter Not Found (Linux):** Install with `sudo apt install python3-tk`
*   **Key Combinations Not Working (Linux VM):** If running Linux in a VM on macOS, use the **Option** key (⌥) on your MacBook keyboard - it maps to Alt in Linux.
*   **Platform Not Detected:** Run `python kermit.py --help` to see which platform was detected and the correct key bindings.

## Contributing

Feel free to fork this repository and submit pull requests with enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.


[![Buy me a coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=davidtkeane&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/davidtkeane)

</p>