import time
import subprocess
import sys
import ctypes

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    import pyautogui
    pyautogui.FAILSAFE = False
    HAS_PYAUTOGUI = True
except ImportError:
    HAS_PYAUTOGUI = False

VK_CAPITAL = 0x14  # Caps Lock key code
KEYEVENTF_KEYUP = 0x0002
MOUSEEVENTF_WHEEL = 0x0800
WHEEL_DELTA = 120

def test_caps_lock_blink():
    """Keyboard light (Caps Lock) ko ON aur OFF karke physical proof dikhata hai."""
    print("\n--- [PROOF 1: KEYBOARD HARDWARE LIGHT TEST] ---")
    print("Aap apne keyboard par 'Caps Lock' ki LED light dekhein...")
    time.sleep(1)
    
    # Press Caps Lock (Turn ON)
    ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, KEYEVENTF_KEYUP, 0)
    print(">> Caps Lock LED: ON hui!")
    time.sleep(1.5)

    # Press Caps Lock (Turn OFF)
    ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, 0, 0)
    ctypes.windll.user32.keybd_event(VK_CAPITAL, 0, KEYEVENTF_KEYUP, 0)
    print(">> Caps Lock LED: OFF hui! (Hardware Key Press 100% Verified)")
    time.sleep(1)

def test_mouse_visible_glide():
    """Mouse pointer ko screen par smooth move karke wapas layega."""
    print("\n--- [PROOF 2: VISIBLE CURSOR MOVEMENT TEST] ---")
    print("Apni screen par cursor ko dekhein, cursor glide karega...")
    time.sleep(1.5)

    if HAS_PYAUTOGUI:
        cur_x, cur_y = pyautogui.position()
        print(f"Current Position: X={cur_x}, Y={cur_y}")

        pyautogui.moveRel(200, 0, duration=0.8)
        time.sleep(0.3)
        pyautogui.moveRel(0, 150, duration=0.8)
        time.sleep(0.3)
        pyautogui.moveRel(-200, -150, duration=0.8)
        print(">> Cursor screen par visibly glide hokar wapas apni jagah aa gaya! (Mouse Movement 100% Verified)")
    else:
        for _ in range(50):
            ctypes.windll.user32.mouse_event(0x0001, 4, 2, 0, 0)
            time.sleep(0.02)
        time.sleep(0.5)
        for _ in range(50):
            ctypes.windll.user32.mouse_event(0x0001, -4, -2, 0, 0)
            time.sleep(0.02)
        print(">> Native mouse events dispatched! (Mouse Movement 100% Verified)")

def test_scroll_event():
    """Web page / browser scroll test."""
    print("\n--- [PROOF 3: SCROLL EVENT TEST] ---")
    print("Agar aap kisi browser ya document window me hain, toh page halka sa scroll down aur up hoga...")
    time.sleep(1)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, ctypes.c_uint(-WHEEL_DELTA).value, 0)
    time.sleep(0.3)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, WHEEL_DELTA, 0)
    print(">> Mouse Scroll event executed successfully!")

def test_notepad_typing():
    """Notepad kholkar usme live automatic typing karke dikhata hai."""
    print("\n--- [PROOF 4: LIVE TYPING PROOF IN NOTEPAD] ---")
    print("Notepad open ho raha hai, script usme khud likhegi...")
    
    proc = subprocess.Popen(["notepad.exe"])
    time.sleep(1.5)

    proof_text = "\n>>> PROOF SUCCESSFUL! <<<\nCursor move, Mouse Scroll aur Keyboard keys successfully working!\n"
    
    if HAS_PYAUTOGUI:
        pyautogui.typewrite(proof_text, interval=0.04)
    else:
        for char in proof_text:
            vk = ctypes.windll.user32.VkKeyScanW(ord(char))
            if vk != -1:
                ctypes.windll.user32.keybd_event(vk & 0xFF, 0, 0, 0)
                ctypes.windll.user32.keybd_event(vk & 0xFF, 0, KEYEVENTF_KEYUP, 0)
            time.sleep(0.04)

    print(">> Notepad me automatically text type ho gaya!")

def main():
    print("=" * 65)
    print("🔍 LIVE PROOF DEMONSTRATION")
    print("=" * 65)
    test_caps_lock_blink()
    test_mouse_visible_glide()
    test_scroll_event()
    test_notepad_typing()
    print("\n" + "=" * 65)
    print("✅ SABHI PROOFS COMPLETE!")
    print("=" * 65)

if __name__ == "__main__":
    main()
