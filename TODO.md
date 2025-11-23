# Kermit Screen Lock - Roadmap & TODO

This document tracks planned features and improvements for the Kermit Screen Lock project.

---

## v3.1.0 - Configuration & Customization ✅ RELEASED

### Config File Support
- [ ] Add `config.json` or `kermit.conf` support
- [ ] Load settings from config file on startup
- [ ] Custom key binding configuration
- [x] Default volume level setting (via `--volume` flag)
- [ ] Custom message text and duration

### Command-Line Arguments
- [x] `--gif <path>` - Use custom GIF file
- [x] `--audio <path>` - Use custom audio file
- [x] `--volume <0.0-1.0>` - Set initial volume
- [x] `--no-sound` - Silent mode (no audio)
- [ ] `--config <path>` - Specify config file location
- [x] `--version` - Display version information
- [x] `--help` - Show help with examples and controls

### Error Handling
- [x] Graceful error messages for missing files
- [x] File validation before fullscreen launch
- [x] Volume range validation (0.0-1.0)
- [x] Helpful suggestions in error messages

---

## v3.2.0 - Security & Lock Mode

### Timeout Feature
- [ ] `--timeout <minutes>` - Auto-exit after specified time
- [ ] On-screen countdown timer (optional)
- [ ] Warning before auto-exit

### Lockdown Mode (USE WITH CAUTION)
- [ ] `--lockdown` - Disable emergency exits, true screen lock
- [ ] Block Escape key
- [ ] Block Alt-Tab / Cmd-Tab
- [ ] Block Alt-F4 / Cmd-Q
- [ ] Prevent window minimize/close
- [ ] Only secret key combination can exit
- [ ] Display warning on startup when lockdown is enabled

### Password Protection
- [ ] `--password` - Require password to exit
- [ ] `--pin <4-6 digits>` - Require PIN to exit
- [ ] Configurable max attempts before lockout
- [ ] Log failed exit attempts

---

## v3.3.0 - Visual Feedback & UX

### On-Screen Indicators
- [ ] Volume level display (fade in/out on change)
- [ ] Pause indicator overlay
- [ ] Mute indicator
- [ ] Current time display (optional)

### User Hints
- [ ] Show exit hint after X seconds of inactivity
- [ ] Customizable hint text
- [ ] Fade-in hint animation

### Loading & Startup
- [ ] Loading/splash screen
- [ ] Validate files exist before fullscreen
- [ ] Graceful error messages (not crashes)

---

## v4.0.0 - Platform Support & Polish

### Windows Support
- [ ] Test on Windows 10/11
- [ ] Windows-specific key bindings
- [ ] Handle Windows system keys (Win key, etc.)

### Code Quality
- [ ] Add type hints throughout
- [ ] Comprehensive docstrings
- [ ] Logging system for debugging
- [ ] Unit tests for key functions

### Documentation
- [ ] Video demo/GIF in README
- [ ] Installation script
- [ ] Man page (Linux)

---

## Security Warnings

### Lockdown Mode Considerations

**USE WITH EXTREME CAUTION:**

1. **Risk of lockout** - If you forget the secret key combination, you may need to force restart your computer
2. **System recovery** - Keep a note of the exit keys somewhere safe
3. **Legal/Ethical use** - Only use on your own devices
4. **Not for malicious purposes** - This is for personal screen lock use only
5. **Emergency exit** - Consider always having a backup exit method

**Recommended Safety Measures:**
- Always test without `--lockdown` first
- Use `--timeout` with lockdown mode as a safety net
- Keep physical access to power button
- Document your key combination somewhere secure

---

## Contributing

Feel free to submit issues or pull requests for any of these features. Priority will be given to:
1. Security improvements (with appropriate safeguards)
2. Cross-platform compatibility
3. User experience enhancements

---

## Version History

| Version | Focus Area | Status |
|---------|-----------|--------|
| 3.0.0 | Cross-platform support | ✅ Released |
| 3.1.0 | Configuration & CLI | ✅ Released |
| 3.2.0 | Security features | 🔄 Planned |
| 3.3.0 | Visual feedback | 🔄 Planned |
| 4.0.0 | Windows & polish | 🔄 Planned |

---

*Last updated: 2025-11-17*
