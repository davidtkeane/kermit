## Kermit Screen Lock - Roadmap & TODO

This document tracks planned features and improvements for the Kermit Screen Lock project.

> **Scope:** Kermit is a fun little screensaver - Kermit typing away on a keyboard, with
> keyboard sounds looping in the background. The "lock" is there to stop a friend messing
> with your computer while you're away, not to be a real security lock. Features are judged
> against that: simple, fun, and hard for a friend to get out of by mashing keys.

---

## v3.1.1 - Bug Fixes ✅ DONE

### Secret Key Combination
- [x] Fix key-release tracking - modifier releases are bound to `<KeyRelease->>` (the `>` key), so Ctrl/Alt/Shift are never cleared and tapping them one at a time exits Kermit
- [x] Replace per-key bindings with one generic `<KeyPress>` / `<KeyRelease>` handler
- [x] Ignore key auto-repeat so holding `P` doesn't toggle pause on and off
- [x] Remove dead `"<Command>"` / `"<Tab>"` check (keysyms never have angle brackets)

### Sound
- [x] Loop audio with `play(loops=-1)` / `music.play(-1)` and remove the sound thread
- [x] Fix sound overlapping after pause/resume
- [x] Hide the pygame "Hello from the pygame community" banner

### Display
- [x] Centre the GIF on screen (currently pinned to the top)
- [x] Overlay the "What's the Secret?" message on the GIF so it's never pushed off-screen
- [x] Use each GIF frame's own duration, with a minimum delay

### Running
- [x] Find `files/` relative to `kermit.py`, so it runs from any directory
- [x] Exit cleanly on Ctrl+C in the terminal

---

## v3.2.0 - Friend-Proofing & Polish

### Friend-Proofing
- [x] Block Cmd+Q (macOS) and the window close button
- [ ] Block Escape
- [x] Block Alt-F4 (Linux) - handled by the close-button block
- [ ] Keep the window on top and grab focus

### On-Screen Feedback
- [ ] Volume level display (fade in/out on change)
- [ ] Pause indicator
- [ ] Mute toggle (M key) with indicator

### Options
- [ ] `--timeout <minutes>` - Auto-exit after a set time
- [ ] `--message <text>` - Custom "What's the Secret?" text
- [ ] `--gif-folder <path>` - Pick a random GIF from a folder

---

## v3.3.0 - Packaging & Code Quality

### Packaging
- [ ] Change exact pins in `requirements.txt` to `>=` (Pillow 10.3.0 has no wheels for Python 3.13+)
- [ ] Add `pyproject.toml` so `pipx install` gives a `kermit` command

### Code Quality
- [ ] Add type hints and docstrings
- [ ] Unit tests for the key-combination logic (no display needed)
- [ ] GitHub Actions workflow - lint + tests

---

## v4.0.0 - Platforms

### Windows Support
- [ ] Test on Windows 10/11
- [ ] Windows-specific key bindings
- [ ] Handle Windows system keys (Win key, etc.)

### Multi-Monitor
- [ ] Black out all screens, not just the main one

### Config
- [ ] Add `config.json` or `kermit.conf` support
- [ ] `--config <path>` - Specify config file location
- [ ] Custom key binding configuration

---

## v3.1.0 - Configuration & Customization ✅ RELEASED

### Command-Line Arguments
- [x] `--gif <path>` - Use custom GIF file
- [x] `--audio <path>` - Use custom audio file
- [x] `--volume <0.0-1.0>` - Set initial volume
- [x] `--no-sound` - Silent mode (no audio)
- [x] `--version` - Display version information
- [x] `--help` - Show help with examples and controls

### Error Handling
- [x] Graceful error messages for missing files
- [x] File validation before fullscreen launch
- [x] Volume range validation (0.0-1.0)
- [x] Helpful suggestions in error messages

---

## Dropped - Out of Scope

These were planned as "real security" features. Kermit is a prank-proof screensaver, not a
security lock, so they add risk (getting locked out of your own Mac) without much benefit.

- [DROPPED] `--lockdown` mode (block Alt-Tab / Cmd-Tab, disable all exits)
- [DROPPED] `--password` / `--pin` to exit
- [DROPPED] Max attempts before lockout, logging failed exit attempts
- [DROPPED] Man page (Linux)

---

## Contributing

Feel free to submit issues or pull requests for any of these features. Priority will be given to:
1. Bug fixes
2. Cross-platform compatibility
3. Fun features and user experience

---

## Version History

| Version | Focus Area | Status |
|---------|-----------|--------|
| 3.0.0 | Cross-platform support | ✅ Released |
| 3.1.0 | Configuration & CLI | ✅ Released |
| 3.1.1 | Bug fixes | ✅ Done |
| 3.2.0 | Friend-proofing & polish | 🔄 Planned |
| 3.3.0 | Packaging & code quality | 🔄 Planned |
| 4.0.0 | Windows, multi-monitor, config | 🔄 Planned |

---

*Last updated: 2026-10-16*
