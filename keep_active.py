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
MOUSEEVENTF_WHEEL = 0x0800
WHEEL_DELTA = 120

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
    """Cursor ko thoda sa hila kar wapas layega taaki web page par mousemove trigger ho."""
    try:
        # Move +3, +3 then -3, -3
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, 3, 3, 0, 0)
        time.sleep(0.05)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, -3, -3, 0, 0)
    except Exception:
        if HAS_PYAUTOGUI:
            pyautogui.moveRel(3, 3, duration=0.1)
            pyautogui.moveRel(-3, -3, duration=0.1)

def simulate_scroll_activity():
    """Web page ko halka sa scroll down aur turant up karega taaki scroll event register ho."""
    try:
        # Scroll down 1 notch (-120), wait 0.1s, scroll back up (+120)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, ctypes.c_uint(-WHEEL_DELTA).value, 0)
        time.sleep(0.1)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, WHEEL_DELTA, 0)
    except Exception:
        if HAS_PYAUTOGUI:
            pyautogui.scroll(-1)
            time.sleep(0.1)
            pyautogui.scroll(1)

def simulate_keyboard_activity():
    """Safe key (Shift) press karta hai jisse koi unwanted letter type na ho."""
    try:
        ctypes.windll.user32.keybd_event(VK_SHIFT, 0, 0, 0)           # Key Down
        time.sleep(0.05)
        ctypes.windll.user32.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0) # Key Up
    except Exception:
        if HAS_PYAUTOGUI:
            pyautogui.press('shift')

def main():
    print("=" * 68)
    print(">>> Auto Mouse, Keyboard & Web Scroll Activity Simulator Running")
    print("=" * 68)
    print("📌 Active Features:")
    print("   - Cursor Activity  : Micro-nudge (+3px / -3px) -> Triggers mousemove")
    print("   - Scroll Activity  : Micro-scroll (Down & Up) -> Triggers web scroll")
    print("   - Keyboard Activity: Safe key (Shift tap)     -> Triggers keydown")
    print("   - Variable Interval: 15s se 50s (Random, strictly under 1 min)")
    print("   - Loop             : Infinite (Chalta rahega)")
    print("🛑 Kaise Rokein       : Terminal me 'Ctrl + C' dabayein")
    print("=" * 68)
    print("💡 Tip for PHP Web App: Browser tab samne open rakhein aur cursor page par chhod dein.\n")

    action_count = 0

    try:
        while True:
            # 1. Prevent Windows screen sleep
            prevent_screen_sleep()

            # 2. Mouse Move
            simulate_mouse_activity()

            # 3. Mouse Scroll (Down then Up)
            simulate_scroll_activity()

            # 4. Keyboard Shift Tap
            simulate_keyboard_activity()

            action_count += 1
            now = datetime.datetime.now().strftime("%H:%M:%S")

            # Variable time under 1 minute (15 to 50 seconds)
            next_wait = random.randint(15, 50)
            print(f"[{now}] Action #{action_count:03d} (Move + Scroll + Key) done | Agla action ~{next_wait}s baad...")

            # 1-second chunks for instant response to Ctrl+C
            for remaining in range(next_wait, 0, -1):
                time.sleep(1)

    except KeyboardInterrupt:
        print("\n" + "=" * 68)
        print("🛑 Script ko manually stop kar diya gaya hai (Ctrl + C).")
        print("=" * 68)
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
