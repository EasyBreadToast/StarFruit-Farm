import win32gui, win32ui, win32con
import time
import keyboard

def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)
        print("######################################")



while True:
        if keyboard.is_pressed("g"):
                list_window_names()
                time.sleep(5)
        pass