# Auto Activity Simulator (Keep-Active)

A lightweight, non-intrusive, and undetectable activity simulation utility for Windows. It keeps your system, web portals (PHP/JavaScript), and collaboration tools (Microsoft Teams, Slack, Skype, Zoom) active without disrupting your ongoing tasks or typing unwanted characters into your open documents.

---

## 🚀 Key Features

- **Micro Mouse Nudge**: Moves the cursor slightly (+3px / -3px) and immediately restores it. Keeps the cursor in place while triggering native OS and browser `mousemove` events.
- **Micro-Scroll (Down & Up)**: Gently scrolls 1 notch down and immediately returns up. Triggers web portal `scroll` / `wheel` activity without moving the page out of view.
- **Safe Keyboard Activity**: Simulates a momentary tap of the `Shift` key. Prevents any accidental characters or commands from being typed into open editors or active inputs.
- **Variable Random Intervals**: Runs on an unpredictable timer between **15 to 50 seconds** (strictly under 1 minute) to avoid robotic fixed-interval pattern detection.
- **Native OS Sleep Prevention**: Calls the Windows kernel API (`SetThreadExecutionState`) to prevent the display from locking and stop the computer from entering sleep mode.
- **Zero-Dependency Native Support**: Built using Windows `ctypes` (`user32` and `kernel32`). Works out of the box with pure Python; optionally uses `pyautogui` if installed.
- **Infinite Loop with Graceful Exit**: Runs continuously until manually terminated via `Ctrl + C`.

---

## 📁 Repository Structure

```text
├── keep_active.py       # Main production script (stealth mode)
├── demo_proof.py        # Visual proof demonstration script
├── LICENSE              # MIT License
└── README.md            # Documentation
```

---

## 🛠️ Prerequisites

- **Operating System**: Windows 10 / 11
- **Python**: Version 3.8 or higher

*(Optional)* If you wish to use PyAutoGUI for auxiliary handling:
```bash
pip install pyautogui
```

---

## 💻 How to Run

### 1. Standard Mode (Interactive Console)
Open PowerShell, Command Prompt, or your IDE terminal in this folder and run:

```bash
python keep_active.py
```

- Real-time status logs with timestamps and countdowns will be displayed in the terminal.
- To stop the script at any time, press **`Ctrl + C`**.

---

### 2. Silent / Background Mode (No Black Console Window)
If you prefer the script to run invisibly in the background without keeping a terminal window open:

1. Rename `keep_active.py` to **`keep_active.pyw`** (or make a copy).
2. Double-click `keep_active.pyw`. The script will now run quietly in the background.
3. **To stop it**: Open **Task Manager** (`Ctrl + Shift + Esc`), locate **Python** under Background Processes, and click **End Task**.

---

### 3. Visual Proof & Hardware Verification Mode
If you want to physically verify that your mouse is gliding, keys are pressing, and the scroll is firing:

```bash
python demo_proof.py
```

This test will:
1. **Blink Caps Lock LED**: Toggles your physical keyboard's Caps Lock light on and off.
2. **Smooth Cursor Glide**: Smoothly animates the mouse pointer across 200 pixels and returns.
3. **Scroll Test**: Executes a visible scroll event.
4. **Notepad Auto-Typing**: Launches Notepad and automatically types a test confirmation string.

---

## 🌐 Optimization for PHP / Web-Based Portals

For company web portals, CRMs, or ticket systems running in Google Chrome, Microsoft Edge, or Mozilla Firefox:
1. Keep the browser tab containing the portal **open and in focus** (do not minimize the browser window).
2. Place the mouse pointer anywhere over a neutral, blank area of the portal page.
3. The script will automatically dispatch the necessary `mousemove`, `wheel`, and `keydown` events to ensure your session remains active.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for complete details.

