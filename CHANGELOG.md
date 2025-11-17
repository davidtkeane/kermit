# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Windows platform testing and support
- Configuration file for custom key bindings
- Custom GIF/audio file support via command-line arguments

## [3.0.0] - 2025-11-17

### Added
- Cross-platform support for macOS and Linux (Kali/Debian/Ubuntu)
- Automatic platform detection using `platform.system()`
- Platform-specific key bindings:
  - macOS: Control + Command + Left Shift (exit), Control + Command + P (pause)
  - Linux: Ctrl + Alt + Left Shift (exit), Ctrl + Alt + P (pause)
- Command-line help flag (`--help` or `-h`) with platform-specific instructions
- Version constant (VERSION = "3.0.0")
- Startup message showing detected platform and key bindings
- Display variables for key combinations (SECRET_KEYS_DISPLAY, PAUSE_KEYS_DISPLAY)

### Changed
- Shebang updated from macOS-specific path to portable `#!/usr/bin/env python3`
- Key binding logic now uses platform-agnostic keysym sets
- requirements.txt enhanced with system package installation notes for Linux
- Uses Alt key instead of Super/Meta on Linux for better VM compatibility

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
| 3.0.0 | 2025-11-17 | macOS, Linux | Cross-platform support, platform detection |
| 2.0.0 | 2024 | macOS | Volume, pause, improved UX |
| 1.0.0 | Initial | macOS | Core functionality |

## Platform Support

### Current (v3.0.0)
- macOS: Full support (Control + Command + Shift)
- Linux (Kali/Debian/Ubuntu): Full support (Ctrl + Alt + Shift)
- Windows: Not tested (should work with Ctrl + Alt + Shift)

### Planned (v4.0.0)
- Windows: Full tested support
- Custom key binding configuration
- Command-line media file selection
