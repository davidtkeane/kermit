# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Cmd+Q and the Quit menu (macOS) no longer quit Kermit - they show "What's the Secret?" instead
- The window close button and Alt+F4 (Linux) are blocked the same way
- Ctrl+C in the terminal still works as an emergency exit

### Changed
- `TODO.md` is no longer tracked in the repo - the detailed roadmap is kept locally, and the Planned list below is the public summary

### Planned
- v3.2.0 - Friend-proofing & polish: on-screen volume and pause indicators, `--timeout`, custom message, random GIF from a folder
- v3.3.0 - Packaging & code quality: `>=` dependency pins, `pyproject.toml`, unit tests, GitHub Actions
- v4.0.0 - Windows support, multi-monitor, config file

Lockdown mode and password/PIN exit have been dropped - Kermit is a fun screensaver that stops a friend messing with your computer, not a security lock.

## [3.1.1] - 2026-10-16

Merged in [PR #1](https://github.com/davidtkeane/kermit/pull/1).

### Changed
- **macOS secret exit is now Control + Command** (was Control + Option + Left Shift). Linux is unchanged: Ctrl + Alt + Left Shift

### Fixed
- **Secret exit could be triggered by tapping Ctrl, Alt and Shift one at a time.** Key-release bindings were built as `<KeyRelease->>` (the `>` key), so modifier releases were never recorded and the keys stayed "held" forever
- A lone `P` could toggle pause once Ctrl and Alt had each been pressed at any earlier time
- Holding `P` no longer toggles pause on and off repeatedly (auto-repeat on macOS and Linux)
- Sound no longer overlaps itself after pause/resume
- GIF is now centred on screen instead of pinned to the top
- "What's the Secret?" now floats over the GIF instead of being pushed off-screen below it
- Running `kermit.py` from another directory now finds `files/` next to the script
- Keys held when the window loses focus no longer get stuck

### Improved
- Audio loops with `play(loops=-1)` - the background sound thread is gone
- Each GIF frame uses its own duration (minimum 20ms)
- GIF frames are resized with high-quality LANCZOS resampling
- Ctrl+C in the terminal now exits cleanly
- pygame's startup banner and `pkg_resources` warning are hidden

### Tested
- Real-keyboard test on macOS (M3 Pro): Control + Command exits, Control + Option + P pauses, tapping the exit keys one at a time does not exit
- Key-combination logic tested with simulated key presses (exit, pause, auto-repeat on macOS and Linux, focus loss)
- Python 3.11 and 3.13, Tk 8.6.14

### Technical
- New `KeyTracker` class holds the key-combination logic, separate from Tk so it can be unit tested
- One generic `<KeyPress>` / `<KeyRelease>` handler replaces the per-key bindings
- Removed dead `"<Command>"` / `"<Tab>"` keysym check

## [3.1.0] - 2025-11-17

### Added
- Command-line argument support using argparse:
  - `--gif <path>` - Specify custom GIF file
  - `--audio <path>` - Specify custom audio file
  - `--volume <0.0-1.0>` - Set initial volume level
  - `--no-sound` - Run in silent mode without audio
  - `--version` - Display version information
- Graceful error handling for missing files with helpful suggestions
- File validation before launching (checks GIF and audio exist)
- Volume validation (must be between 0.0 and 1.0)
- Startup information display (shows GIF path, audio path, volume level)
- Silent mode support (animation without audio)

### Changed
- Version bumped to 3.1.0
- Replaced manual help with argparse auto-generated help
- KermitApp now accepts parameters for custom configuration
- Improved error messages with current directory display
- Audio initialization skipped in silent mode

### Technical
- Added `parse_arguments()` function for CLI parsing
- Added `validate_files()` function for pre-launch validation
- KermitApp.__init__ now accepts gif_path, audio_path, initial_volume, no_sound parameters
- All audio-related methods check for no_sound flag before executing

## [3.0.0] - 2025-11-17

### Added
- Cross-platform support for macOS and Linux (Kali/Debian/Ubuntu)
- Automatic platform detection using `platform.system()`
- Unified key bindings across platforms (same physical keys on MacBook):
  - macOS: Control + Option + Left Shift (exit), Control + Option + P (pause)
  - Linux: Ctrl + Alt + Left Shift (exit), Ctrl + Alt + P (pause)
- Command-line help flag (`--help` or `-h`) with platform-specific instructions
- Version constant (VERSION = "3.0.0")
- Startup message showing detected platform and key bindings
- Display variables for key combinations (SECRET_KEYS_DISPLAY, PAUSE_KEYS_DISPLAY)

### Changed
- Shebang updated from macOS-specific path to portable `#!/usr/bin/env python3`
- Key binding logic now uses platform-agnostic keysym sets
- requirements.txt enhanced with system package installation notes for Linux
- macOS now uses Option key instead of Command key (matches Linux Alt key behavior)
- Same physical keys work on both macOS and Linux when using MacBook keyboard

### Fixed
- Key combinations now work reliably in Linux VMs (avoids Super key interception)

### Tested
- Successfully tested on Kali Linux VM (ARM64) running on macOS host
- MacBook keyboard: Option key maps to Alt for Linux key bindings
- Pygame 2.6.1 and Pillow 10.3.0 confirmed working on aarch64

## [2.0.0] - 2024-XX-XX

### Added
- Volume control with Up/Down arrow keys
- Pause/Resume functionality (Command + Control + P on macOS)
- Animated GIF support with automatic frame sequencing
- Fullscreen display with aspect ratio preservation
- Hidden mouse cursor during playback
- "What's the Secret?" message on key press (3-second duration)
- Threaded audio playback for smooth performance
- Fallback audio loading (pygame.mixer.Sound -> pygame.mixer.music)

### Features
- Secret exit combination: Control + Command + Left Shift (macOS)
- Looping MP3 audio playback
- Automatic screen size detection and image scaling
- Interactive message display system

## [1.0.0] - Initial Release

### Added
- Basic fullscreen GIF display
- MP3 audio playback
- Simple exit mechanism
- Tkinter-based GUI

---

## Version History Summary

| Version | Date | Platform | Key Changes |
|---------|------|----------|-------------|
| 3.1.1 | 2026-10-16 | macOS, Linux | Secret-exit bug fix, macOS exit is Control + Command, sound/layout fixes |
| 3.1.0 | 2025-11-17 | macOS, Linux | CLI arguments, custom media, silent mode |
| 3.0.0 | 2025-11-17 | macOS, Linux | Cross-platform support, platform detection |
| 2.0.0 | 2024 | macOS | Volume, pause, improved UX |
| 1.0.0 | Initial | macOS | Core functionality |

## Platform Support

### Current (v3.1.1)
- macOS: Full support - exit with Control + Command, pause with Control + Option + P
- Linux (Kali/Debian/Ubuntu): Full support - exit with Ctrl + Alt + Left Shift, pause with Ctrl + Alt + P
- Windows: Not tested (should work with Ctrl + Alt + Left Shift)
- Linux VM on a MacBook: use the Option key for Alt

### Planned (v4.0.0)
- Windows: Full tested support
- Custom key binding configuration
- Multi-monitor blackout
