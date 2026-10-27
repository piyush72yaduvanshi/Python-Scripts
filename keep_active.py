import time
import random
import datetime
import sys
import ctypes

# Windows console UTF-8 encoding support
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Optional PyAutoGUI support
try:
    import pyautogui
    pyautogui.FAILSAFE = False  # Avoid crash if cursor is at corner
    HAS_PYAUTOGUI = True
except ImportError:
    HAS_PYAUTOGUI = False

# Windows API Constants
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

MOUSEEVENTF_MOVE = 0x0001
VK_SHIFT = 0x10
KEYEVENTF_KEYUP = 0x0002

def prevent_screen_sleep():
    """Windows OS ko sleep aur display lock hone se rokta hai."""
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(
            ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
        )
    except Exception:
        pass

def simulate_mouse_activity():
    """Cursor ko thoda sa hila kar wapas layega taaki activity register ho."""
    try:
        # Move +3, +3 then -3, -3
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, 3, 3, 0, 0)
        time.sleep(0.05)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, -3, -3, 0, 0)
    except Exception:
        if HAS_PYAUTOGUI:
            pyautogui.moveRel(3, 3, duration=0.1)
            pyautogui.moveRel(-3, -3, duration=0.1)

def simulate_keyboard_activity():
    """Safe key (Shift) press karta hai jisse kisi text editor me koi unwanted letter type na ho."""
    try:
        ctypes.windll.user32.keybd_event(VK_SHIFT, 0, 0, 0)           # Key Down
        time.sleep(0.05)
        ctypes.windll.user32.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0) # Key Up
    except Exception:
        if HAS_PYAUTOGUI:
            pyautogui.press('shift')

def main():
    print("=" * 65)
    print(">>> Auto Mouse & Keyboard Activity Simulator Running")
    print("=" * 65)
    print("📌 Settings:")
    print("   - Cursor Activity : Subtle relative nudge (+3px / -3px)")
    print("   - Keyboard Activity: Safe key (Shift tap)")
    print("   - Variable Interval: 15s se 50s (Under 1 min, Random)")
    print("   - Loop             : Infinite (Chalta rahega)")
    print("🛑 Kaise Rokein       : Terminal me 'Ctrl + C' dabayein")
    print("=" * 65 + "\n")

    action_count = 0

    try:
        while True:
            # Prevent Windows screen sleep
            prevent_screen_sleep()

            # Perform Mouse & Keyboard simulation
            simulate_mouse_activity()
            simulate_keyboard_activity()

            action_count += 1
            now = datetime.datetime.now().strftime("%H:%M:%S")

            # Variable time under 1 minute (15 to 50 seconds)
            next_wait = random.randint(15, 50)
            print(f"[{now}] Action #{action_count:03d} executed | Next action in {next_wait} seconds...")

            # 1-second chunks for instant response to Ctrl+C
            for remaining in range(next_wait, 0, -1):
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n" + "=" * 65)
        print("🛑 Script ko manually stop kar diya gaya hai (Ctrl + C).")
        print("=" * 65)
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
