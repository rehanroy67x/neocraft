import threading
import time
import ctypes
from ctypes import wintypes

# Constants for key codes
VK_TAB = 0x09
VK_CONTROL = 0x11
VK_SHIFT = 0x10

# Constants for foreground window switching
SWITCH_INTERVAL = 600  # Time in seconds between automatic task switches

user32 = ctypes.WinDLL('user32', use_last_error=True)

def is_foreground_window(hwnd):
    return hwnd == user32.GetForegroundWindow()

def switch_foreground_window():
    user32.keybd_event(VK_CONTROL, 0, 0, 0)
    user32.keybd_event(VK_SHIFT, 0, 0, 0)
    user32.keybd_event(VK_TAB, 0, 0, 0)
    user32.keybd_event(VK_TAB, 0, 2, 0)
    user32.keybd_event(VK_SHIFT, 0, 2, 0)
    user32.keybd_event(VK_CONTROL, 0, 2, 0)

def background_task():
    while True:
        print("Running background task...")
        time.sleep(SWITCH_INTERVAL / 2)

def foreground_task():
    while True:
        print("Running foreground task...")
        if is_foreground_window(user32.GetForegroundWindow()):
            time.sleep(SWITCH_INTERVAL)
            switch_foreground_window()

def main():
    bg_thread = threading.Thread(target=background_task)
    fg_thread = threading.Thread(target=foreground_task)

    bg_thread.start()
    fg_thread.start()

    bg_thread.join()
    fg_thread.join()

if __name__ == "__main__":
    main()