# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned for v3.2.0 - Security & Lock Mode
- Timeout feature with `--timeout <minutes>` auto-exit
- **Lockdown mode** (`--lockdown`) - True screen lock, blocks emergency exits
- Password/PIN protection to exit
- Block Alt-Tab, Alt-F4, Escape key in lockdown mode
- Failed attempt logging

### Planned for v3.3.0 - Visual Feedback
- On-screen volume indicator
- Pause/mute overlay
- Exit hint after inactivity
- Loading screen and graceful error handling

### Planned for v4.0.0 - Platform Support
- Windows platform testing and support
- Type hints and comprehensive docstrings
- Logging system for debugging
- Unit tests

See `TODO.md` for full roadmap and security warnings.

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
| 3.1.0 | 2025-11-17 | macOS, Linux | CLI arguments, custom media, silent mode |
| 3.0.0 | 2025-11-17 | macOS, Linux | Cross-platform support, platform detection |
| 2.0.0 | 2024 | macOS | Volume, pause, improved UX |
| 1.0.0 | Initial | macOS | Core functionality |

## Platform Support

### Current (v3.0.0)
- macOS: Full support (Control + Option + Shift)
- Linux (Kali/Debian/Ubuntu): Full support (Ctrl + Alt + Shift)
- Windows: Not tested (should work with Ctrl + Alt + Shift)
- MacBook keyboard: Same physical keys work on both platforms!

### Planned (v4.0.0)
- Windows: Full tested support
- Custom key binding configuration
- Command-line media file selection
