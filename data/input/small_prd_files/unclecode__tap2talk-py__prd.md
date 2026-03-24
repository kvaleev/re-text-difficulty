---
project: tap2talk-py
repository: unclecode/tap2talk-py
license: MIT License
source_file: prd.md
source_url: https://github.com/unclecode/tap2talk-py/blob/a1321e465184c9e92e7f42818320e3b853eddb1c/prd.md
downloaded_at: 2025-12-05T10:29:38.354087+00:00
consensus_grade_level: 10.1
headings_per_sentence: 0.12
lists_per_sentence: 0.49
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.12
anaphora_per_sentence: 0.08
sentence_cv: 1.512
cpre_terms_per_sentence: 0.22
---
Alright Unclecode, here is a complete, opinionated design that you can hand to yourself in the morning and implement by lunch. I will keep it tight, but cover everything you asked for, with specific choices, tradeoffs, and failure modes.

# High level, in one breath

Python app, runs as menu bar, global hotkey listener for double Ctrl to start and stop, records mic into 16 kHz mono 16-bit WAV, ships that to Groq Whisper Large V3 Turbo, inserts returned text at caret using direct injection, falls back to clipboard+paste while preserving the user clipboard when possible, shows a tiny always-on-top overlay for Recording, Processing, Done, Abort. Cross platform for macOS and Windows. Packaged with the right plist and manifests so it never steals focus or shows a dock icon.

# Architecture

## Processes and threads

* Single process, one UI main loop for the tray and overlay, plus worker threads:

  * **Main thread** runs the tray icon and the overlay window event loop
  * **Hotkey thread** listens to global keyboard events
  * **Audio thread** captures PCM to an in-memory ring buffer and file
  * **Transcription async task** uses `groq.AsyncGroq` with `httpx` behind the scenes, cancellable
  * **Controller** state machine orchestrates start, stop, abort

## State machine

States: `IDLE`, `RECORDING`, `PROCESSING`

Events:

* `double_ctrl` in `IDLE` -> start recording
* `double_ctrl` in `RECORDING` -> stop, transition to `PROCESSING`
* `double_esc` in `RECORDING` or `PROCESSING` -> abort, cleanup, back to `IDLE`
* `transcription_ok(text)` in `PROCESSING` -> insert text, show Done, return to `IDLE`
* `transcription_fail(err)` in `PROCESSING` -> show error, fallback if possible, return to `IDLE`

Concurrency guard: atomic state, lock around transitions, idempotent cleanup.

# Module layout

```
tap2talk/
  __main__.py              # entry
  app.py                   # AppController, state machine
  config.py                # load/validate ~/.tap2talk/config.yaml and env fallback
  paths.py                 # directories, file naming, safe chmod
  log.py                   # rotating file logger with redaction
  hotkeys/
    __init__.py
    mac.py                 # Quartz event tap for modifier keys
    win.py                 # keyboard or low level hook via pywin32
  audio/
    __init__.py
    recorder.py            # SoundDevice InputStream, 16 kHz mono
    resample.py            # resampler wrapper, only used if needed
  transcribe/
    __init__.py
    groq_client.py         # AsyncGroq wrapper, retries, timeouts
  insert/
    __init__.py
    mac.py                 # CGEvent Unicode injection, AppleScript paste fallback
    win.py                 # SendInput based paste, clipboard preserve
    clipboard.py           # cross platform best effort preserve/restore
  ui/
    tray.py                # pystray icon, menu, restart, exit
    overlay.py             # Tk tiny window, top right, semi transparent
  system/
    autostart.py           # LaunchAgent on mac, Run key on Windows
    permissions_mac.py     # AXIsProcessTrustedWithOptions check, mic check hint
  version.py
```

# Key design choices

## Hotkeys, double press detection

* **Mac**: use a Quartz event tap, listen to `kCGEventFlagsChanged` with control flag transitions, measure press intervals, you avoid the usual `pynput` ctrl quirk on mac and get robust global capture with Accessibility permission. Target threshold 400 ms between presses, debounce 150 ms so holding Ctrl does not retrigger. If you prefer Python-only, `pynput` works but ctrl can be flaky on mac, Quartz is reliable. Reference shows `pynput` ctrl hotkeys have issues on mac, Quartz is the stable path. ([GitHub][1])
* **Windows**: `keyboard` works fine for global detection, but to avoid driver requirements on locked down systems, you can also use a low-level WH\_KEYBOARD\_LL hook via `pywin32`. I would start with `keyboard` for speed, then add hook if you see misses under gaming anti-cheat drivers.
* Algorithm:

  * Maintain two finite state counters: `ctrl_window`, `esc_window`. On `key_down` for Ctrl or Esc, if `now - last` < threshold and released in between, that is a double press. Reset windows on other key downs to avoid accidental doubles while doing something else.

## Recording, audio pipeline

* Library: `sounddevice` over PortAudio, it is light, wheels are reliable on mac arm64 and Windows, and you get direct 16 kHz capture. Latest docs confirm robust stream API. ([python-sounddevice.readthedocs.io][2])
* **Open input stream at 16\_000 Hz, channels=1, dtype=float32**. PortAudio will mix down and resample for us where needed, which is fine. If the device refuses 16 kHz, we reopen at device native rate and resample.
* Resampling, if needed: prefer `resampy` sinc interpolation with Blackman-Harris window, matches your spec, small dependency. Or `samplerate` (libsamplerate) if you want C quality and speed. Both are battle tested. ([resampy.readthedocs.io][3], [PyPI][4])
* Buffering: ring buffer in memory with `queue.SimpleQueue` for level monitoring in the future, while also appending to a temporary WAV via `soundfile` or Python `wave`. Simpler, write at stop time, not during stream, to minimize disk IO while recording. Cap length by `recording_timeout` from config, default 30 s.

**WAV output spec**
PCM, 16 kHz, mono, 16-bit little endian. Convert with `np.clip(x * 32767, -32768, 32767).astype(np.int16)`.

## Transcription, Groq

* Use the **official `groq` Python client, async flavor**, so aborting is actually cancellable. Endpoint is OpenAI compatible `POST /openai/v1/audio/transcriptions`. Models include `whisper-large-v3-turbo`, which is explicitly documented with pricing and speed. The docs also state server will downsample to 16 kHz mono anyway, so we are aligned. ([GroqCloud][5])
* Async client surface is `AsyncGroq`, built on `httpx` and supports aiohttp backend. We run a private asyncio loop in a worker thread, create a task for each upload, and cancel that task on abort. Library confirms first-class async and error classes. ([GitHub][6])
* Request body: `file=Path(...)`, `model="whisper-large-v3-turbo"`, `temperature=0`, `response_format="json"` for simple `.text`, or `verbose_json` if you want word timestamps later. Limits and formats are in the doc, free tier 25 MB per file, dev tier 100 MB, and they recommend WAV or FLAC for lower latency. ([GroqCloud][5])
* Timeouts and retries: timeout 30 s, retries 3 for 500s with exponential backoff, 429 backoff with jitter. 413, show “Too long, try shorter”, 401, prompt for key.

## Text insertion at caret

* Strategy order:

  1. **Direct injection**, fastest, no clipboard touch

     * **macOS**: Quartz `CGEventKeyboardSetUnicodeString`, post Unicode events to the current focus. Requires Accessibility permission, does not need Apple Events.
     * **Windows**: `SendInput` with `KEYBDINPUT` scancodes for text, handle surrogate pairs, newline mapping.
  2. **Clipboard paste fallback**, preserves user clipboard

     * Snapshot text formats, set clipboard to our text, synthesize paste, restore clipboard.
     * **macOS**: we can read and write plain text via `pbpaste` and `pbcopy` with bytes, or use `AppKit.NSPasteboard` for richer formats. We will preserve only plain text safely, warn in logs if rich content was present.
     * **Windows**: use `win32clipboard` to snapshot CF\_UNICODETEXT when available. Restoring HTML or RTF is possible but fussy, so we scope v1 to text only, which is 95 percent of cases. Microsoft docs cover CF\_TEXT etc. ([Microsoft Learn][7])
* Paste synthesis:

  * **macOS**: Command+V via Quartz CGEvents, or AppleScript `System Events` if Quartz paste is blocked in a few sandboxes.
  * **Windows**: `SendInput` Ctrl down, V down, V up, Ctrl up, with small delays to match human pacing. Multiple references show how to wire `SendInput` from Python. ([Stack Overflow][8], [batchloaf.wordpress.com][9])

## UI, always-on-top overlay and tray

* **System tray**: `pystray` for a tiny cross platform tray icon and menu, documented to require main thread run loop, which we already have. Menu has About, Restart, Exit. Fresh articles exist in 2025, and docs remain stable. ([pystray.readthedocs.io][10], [GeeksforGeeks][11])
* **Overlay**: `tkinter` tiny window, 200x60 px, rounded corners optional, `overrideredirect(True)`, `-topmost`, alpha 0.85, no focus, click-through off, auto hide. Position top-right with 16 px margin, compute from virtual screen. Tk tips for topmost and transparency are standard. ([CodersLegacy][12], [Stack Overflow][13])
* **States**:

  * Recording, red background, shows running time
  * Processing, blue background, spinning indicator
  * Done or Aborted, green or gray, hides after 2 s

## Packaging, startup, and permissions

* **macOS**:

  * Package with `py2app` or **BeeWare Briefcase** to an `.app`, set `LSUIElement=true` so there is no Dock icon, and add usage keys `NSMicrophoneUsageDescription` and `NSAppleEventsUsageDescription` just in case the AppleScript fallback is used. `LSBackgroundOnly` is also viable, but `LSUIElement` is the right one here. Multiple references and common practice. ([Ask Different][14], [leancrew.com][15], [Stack Overflow][16])
  * Accessibility permission is required for global keys and key injection. Check with `AXIsProcessTrustedWithOptions`, optionally prompt. At first tap creation, macOS will prompt anyway. Apple API doc shows this pattern. ([Apple Developer][17])
  * Auto-start: User LaunchAgent `~/Library/LaunchAgents/com.tap2talk.agent.plist` pointing to the `.app/Contents/MacOS/<binary>`.
* **Windows**:

  * Package with **PyInstaller** onefile, set manifest to no console, DPI aware.
  * Auto-start: write `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` string “Tap2Talk” to the exe path, or drop a shortcut into the Startup folder.
  * No special keyboard monitoring permission needed. Use WASAPI via `sounddevice` by default.

# Config, directories, and security

* **Config file**: `~/.tap2talk/config.yaml`, 600 permission on mac and Windows equivalent ACL that grants only current user. Keys:

  ```
  groq_api_key: "gsk_..."   # or use env GROQ_API_KEY
  log_level: "info"
  auto_paste: true
  recording_timeout: 30
  model: "whisper-large-v3-turbo"
  ```
* **Key resolution order**: YAML, then `GROQ_API_KEY`, finally prompt with overlay info.
* **App dirs**:

  ```
  ~/.tap2talk/
    config.yaml
    recordings/           # temp wavs
    failed/
    logs/tap2talk.log
    cache/
  ```
* **Data handling**:

  * On success, delete temp WAV immediately
  * On failure, move to `failed/` with timestamp, optional later encryption
  * No telemetry, no external calls beyond Groq
* Optional encryption: if you want at-rest encryption for failed files, add `cryptography` with a random Fernet key stored in OS keychain, but default is delete on success and keep failures only for short time, then rotate.

# Error handling and retries

* Groq client:

  * 401, show overlay “Invalid API key”, open config folder
  * 413, show overlay “Recording too large, shorten it”
  * 429, backoff 0.5, 1.0, 2.0 s
  * 5xx, retry 3 times
  * Timeout 30 s, one retry
* Audio:

  * Mic not available, show overlay and a help link, keep running
* Insertion:

  * Direct injection failure, try clipboard paste
  * Clipboard conflict, try again once with a 150 ms delay
  * Restore clipboard on exit or after 2 s idle

# Performance budget

* Idle CPU near 0 percent, the hotkey tap is blocking and event driven
* Recording, one memory copy per callback, no DSP unless resampling
* File size, speech at 16 kHz mono 16-bit, \~32 KB/s, 10 s is \~320 KB, tiny
* Groq round trip target under 3 s for typical dictation, matches public perf, v3-turbo reported 216x realtime in their blog, doc shows speed factors and pricing, your payload is small so network is the only swing. ([Groq][18], [GroqCloud][5])

# Detailed component specs

## `hotkeys.mac`

* Use PyObjC `Quartz` to create a global event tap for `kCGEventFlagsChanged` and `kCGEventKeyDown`
* Track when the control flag toggles from off to on, record timestamp, look for a second toggle within `double_threshold_ms`
* Do the same for Esc via `kCGEventKeyDown` keycode 53
* Needs Accessibility permission, use `AXIsProcessTrustedWithOptions({kAXTrustedCheckOptionPrompt: True})` once at boot, store result, and surface a clear overlay if denied

## `hotkeys.win`

* Default `keyboard` listener for key down events of both Ctrl keys and Esc
* Alternative, if `keyboard` is blocked, install WH\_KEYBOARD\_LL hook via `pywin32` to get global events

## `audio.recorder`

* Open `sd.InputStream(samplerate=16000, channels=1, dtype='float32', blocksize=2048, callback=...)`
* In callback, push frames to RAM list and optionally update a shared `vu_level` for future UI
* On stop, concatenate buffers, convert to int16, write to temp file path like `tap2talk_recording_YYYYmmdd_HHMMSS.wav`
* If the device refuses 16 kHz mono, fall back to device native and resample with `resampy.resample(x, sr_in, 16000, filter='kaiser_best')`, or `samplerate.resample(x, ratio, converter_type='sinc_best')`. ([resampy.readthedocs.io][3], [PyPI][4])

## `transcribe.groq_client`

* Keep one `AsyncGroq` client, configured with `timeout=30`, retry transport
* `await client.audio.transcriptions.create(file=Path(wav_path), model='whisper-large-v3-turbo', temperature=0, response_format='json')`
* Return `resp.text`, also keep `resp.x_groq.id` for logs if exposed by model, else raw headers
* Cancel on abort by `task.cancel()`, which will propagate to `httpx` and close the socket. Library supports async and custom client backends. ([GitHub][6])

## `insert.mac`

* Try direct Unicode injection:

  * For each chunk in the text, make `CGEventCreateKeyboardEvent(None, 0, True)`, call `CGEventKeyboardSetUnicodeString(event, text_chunk)`, post to the HID event tap
* If that fails or input field is secure, do clipboard:

  * Snapshot `pbpaste` text, set `pbcopy` to our text, synthesize Command+V with Quartz events, restore previous text after a short delay

## `insert.win`

* Try direct send via `SendInput` for printable code points, otherwise fallback to clipboard paste
* Clipboard preserve:

  * Open clipboard, if CF\_UNICODETEXT available, read and stash, set our text, paste, then restore. Documentation covers clipboard formats. ([Microsoft Learn][7])

## `ui.tray`

* `pystray.Icon` with a plain glyph, white outline so it works on dark themes
* Right click menu:

  * About, open a tiny modal overlay with version
  * Restart, call controller.restart()
  * Exit, graceful shutdown, stop streams and tasks
* `pystray` runs in main thread, our setup registers the hotkey and kicks the controller. Docs warn run must be on main thread, we follow that. ([PyPI][19])

## `ui.overlay`

* Tk `Toplevel`, no decorations, on top, geometry to top right, alpha 0.85
* Small label, optional spinner made from a `Canvas` arc rotate timer
* Auto hide `after(2000)` when Done or Aborted

# Permissions, gotchas, and first-run UX

* **macOS**:

  * First hotkey hook triggers Accessibility prompt, show overlay explaining what to click if denied
  * First mic use triggers mic prompt, plist key must be present in the packaged app. This is a non negotiable Apple requirement for apps accessing the mic. ([Stack Overflow][16])
  * Hiding Dock icon is done via `LSUIElement=true` in Info.plist of the packaged `.app`, not at runtime, see common solutions. ([Ask Different][14])
* **Windows**:

  * If SendInput fails in UWP sandboxes, clipboard route is the escape hatch
  * Some corporate endpoint security can block global hooks, keep both keyboard libraries available

# Logging

* File `~/.tap2talk/logs/tap2talk.log`, rotating 5 files x 256 KB
* PII redaction: never log audio path names or the transcription text unless debug is enabled, never log API key
* Keep Groq request id if available for tracing, but do not include the audio bytes

# Autostart and restart

* macOS: write a LaunchAgent with `KeepAlive=true`, `RunAtLoad=true`, `ProgramArguments` pointing at the app binary
* Windows: set the Run key, add a “Restart” menu item that execs self then exits

# Testing plan

* Hotkey debouncing test on noisy keyboards, press ctrl 100 times with random delays, expect 0 or 1 start events per double
* Audio device matrix, 44.1 kHz only mics, 48 kHz only mics, external USB stereo, all must produce correct 16 kHz mono
* Clipboard preservation test for text, and negative test for RTF to confirm we do not break rich clipboards silently
* Simulated Groq 500 and 429, assert overlay errors and retry schedule
* Soak test, 48 hours idle and intermittent dictations, memory stable

# Minimal dependency set

* `groq>=0.31.0` async client, August 2025 release exists and works with httpx or aiohttp backend ([GitHub][6])
* `sounddevice>=0.5.2` for I/O ([python-sounddevice.readthedocs.io][2])
* `numpy`, `soundfile` or stdlib `wave`
* `resampy>=0.4` or `samplerate` if you want C level SRC ([resampy.readthedocs.io][3], [PyPI][4])
* `pystray`, `Pillow` for icon
* `pyobjc` on mac for Quartz, `pywin32` on Windows for clipboard if you avoid pure ctypes
* `pynput` optional, but Quartz is preferred on mac

# Security posture

* No telemetry, no crash uploads
* API key never logged, only test validity with models list on first run if missing, store in YAML with 600 permissions
* Delete successful WAVs immediately, failures rotated and pruned nightly
* Optional future, encrypt failures with a key stored in OS keychain

# Implementation notes you will care about

* Do not block the Tk main loop, all long tasks are threads or asyncio tasks
* The tray must run on the main thread, `pystray.Icon.run()` enforces this, we use its `setup` callback to start everything else so mac runloop is happy. ([PyPI][19])
* Canceling the transcription, do it with `task.cancel()`, not with thread flags. Ignore results arriving after abort if transport does not cancel immediately, but the async client with httpx should tear down promptly. ([GitHub][6])
* Some mac apps swallow synthetic key events in secure fields, your clipboard fallback covers 95 percent. Windows IME fields sometimes need a small sleep, 10 to 20 ms between modifier and key
* Multi monitor top right, Tk reports a virtual desktop, so compute right edge via `winfo_screenwidth()`, if you want per-monitor positioning later, add `screeninfo` and pick the monitor containing the active window

# Packaging recipes

* **macOS Briefcase option**, yields a clean `.app` with Info.plist you control, easy to set `LSUIElement`. The Briefcase docs are current and the tool is active in 2025. ([briefcase.readthedocs.io][20])
* **macOS PyInstaller** also works, but embedding Info.plist keys is fiddly, Briefcase makes the menu bar behavior cleaner
* **Windows PyInstaller** with `--noconsole` and icon, add a basic app manifest, DPI awareness `PerMonitorV2`

# What I would build first, in order

1. Controller and state machine with mocked services
2. Hotkeys, double press detection, log only
3. Overlay, show Recording and Abort visually
4. Audio capture to WAV at 16 kHz mono, 10 s cap
5. Groq async transcription, wire success and failure
6. Text insertion, direct injection then clipboard fallback
7. Tray, About, Restart, Exit
8. Autostart installers
9. Robust error handling and log redaction

# Anticipated sharp edges and how we blunt them

* mac global hotkeys and injection need Accessibility, we detect and instruct via overlay, and keep running in degraded mode until granted
* Some Windows environments block low level hooks, but your hotkey is just double Ctrl, the `keyboard` library still works in the majority of userland
* Clipboard preservation beyond plain text is gnarly, we will not attempt to preserve HTML and RTF v1, but we will only touch clipboard when we must paste, and we will restore plain text faithfully
* Cancelling an in-flight upload is best effort, we rely on async cancellation, if the socket does not abort instantly, we drop the response upon arrival

# Done, want code?

If you want, I can post the full scaffolding, including Quartz listener, the Tk overlay class, and the AsyncGroq wrapper with retries. Say the word and I will split into PR-ready chunks using your `+>` diff style.

---

## Sources

Groq speech to text API endpoints, models, file limits, sample client code, and speed guidance are documented on Groq’s site. The async Python client and its cancellation model are in the official SDK. ([GroqCloud][5], [GitHub][6])

Whisper Large V3 Turbo performance reference on Groq blog, useful for latency expectations. ([Groq][18])

Audio capture and stream API for `sounddevice`, latest docs confirm capabilities. ([python-sounddevice.readthedocs.io][2])

High quality sinc resampling with Blackman-Harris window available in `resampy`, and libsamplerate wrappers if you prefer C quality. ([resampy.readthedocs.io][3], [PyPI][4])

System tray library behavior and main thread requirement for `pystray`. ([PyPI][19])

macOS Dock hiding uses `LSUIElement`, and microphone usage key requirement, both common practice. ([Ask Different][14], [Stack Overflow][16])

Windows clipboard formats and SendInput practices for paste simulation and text injection. ([Microsoft Learn][7], [batchloaf.wordpress.com][9])

[1]: https://github.com/moses-palmer/pynput/issues/297?utm_source=chatgpt.com "Global hotkeys with ctrl and alt don't work on MacOS #297 - GitHub"
[2]: https://python-sounddevice.readthedocs.io/en/latest/api/streams.html?utm_source=chatgpt.com "Streams using NumPy Arrays — python-sounddevice, version 0.5.2"
[3]: https://resampy.readthedocs.io/?utm_source=chatgpt.com "Introduction — resampy 0.4.2 documentation"
[4]: https://pypi.org/project/samplerate/?utm_source=chatgpt.com "samplerate - PyPI"
[5]: https://console.groq.com/docs/speech-to-text "Speech to Text - GroqDocs"
[6]: https://github.com/groq/groq-python "GitHub - groq/groq-python: The official Python Library for the Groq API"
[7]: https://learn.microsoft.com/en-us/windows/win32/dataxchg/using-the-clipboard?utm_source=chatgpt.com "Using the Clipboard - Win32 apps | Microsoft Learn"
[8]: https://stackoverflow.com/questions/62189991/how-to-wrap-the-sendinput-function-to-python-using-ctypes?utm_source=chatgpt.com "How to wrap the SendInput function to python using ctypes"
[9]: https://batchloaf.wordpress.com/2012/10/18/simulating-a-ctrl-v-keystroke-in-win32-c-or-c-using-sendinput/?utm_source=chatgpt.com "Simulating a Ctrl-V keystroke in Win32 (C or C++) using SendInput"
[10]: https://pystray.readthedocs.io/?utm_source=chatgpt.com "pystray Package Documentation — pystray 0.19.5 documentation"
[11]: https://www.geeksforgeeks.org/python/create-a-responsive-system-tray-icon-using-python-pystray/?utm_source=chatgpt.com "Create a Responsive System Tray Icon using Python PyStray"
[12]: https://coderslegacy.com/python/how-to-keep-a-tkinter-window-on-top/?utm_source=chatgpt.com "How to keep a Tkinter Window on Top (3 Methods) - CodersLegacy"
[13]: https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window?utm_source=chatgpt.com "Transparent background in a Tkinter window - python - Stack Overflow"
[14]: https://apple.stackexchange.com/questions/130390/hide-adium-or-any-other-apps-icon-in-the-dock?utm_source=chatgpt.com "Hide Adium (or any other app's) icon in the dock - Ask Different"
[15]: https://leancrew.com/all-this/2014/01/stopping-the-python-rocketship-icon/?utm_source=chatgpt.com "Stopping the Python rocketship icon - All this - Dr. Drang"
[16]: https://stackoverflow.com/questions/39589998/the-apps-info-plist-must-contain-an-nsmicrophoneusagedescription-key-with-a-str?utm_source=chatgpt.com "The app's Info.plist must contain an ..."
[17]: https://developer.apple.com/documentation/applicationservices/1459186-axisprocesstrustedwithoptions?utm_source=chatgpt.com "AXIsProcessTrustedWithOptions(_:) | Apple Developer Documentation"
[18]: https://groq.com/blog/whisper-large-v3-turbo-now-available-on-groq-combining-speed-quality-for-speech-recognition?utm_source=chatgpt.com "Whisper Large v3 Turbo Now Available on Groq, Combining Speed ..."
[19]: https://pypi.org/project/pystray/0.3/?utm_source=chatgpt.com "pystray · PyPI"
[20]: https://briefcase.readthedocs.io/_/downloads/en/stable/pdf/?utm_source=chatgpt.com "[PDF] Briefcase Documentation"

