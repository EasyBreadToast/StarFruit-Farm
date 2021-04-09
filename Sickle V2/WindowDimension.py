import pydirectinput
import keyboard
import autoit
import time
from win32gui import FindWindow, GetWindowRect

pydirectinput.PAUSE = 0.02
time.sleep(2)
windowName = "Roblox"

def plant(input):
    autoit.mouse_move(x, y - input,1)
    for i in range(20):
        pydirectinput.move(30,0)


while keyboard.is_pressed("r") == False:
    window_handle = FindWindow(None, windowName)
    window_rect = GetWindowRect(window_handle)  
    rect = window_rect

    #Offsets
    x = rect[0] + 110
    y = rect[3] - 110

    #Switch to sickle
    pydirectinput.press("2")
    pydirectinput.mouseDown()
    time.sleep(4)
    pydirectinput.mouseUp()

    #Plant seeds
    pydirectinput.press("1")
    pydirectinput.press('`')

    plant(0)
    plant(60)
    plant(120)
    plant(170)
    plant(230)
    plant(280)
    plant(330)
    plant(380)
    plant(420)

    pydirectinput.press('`')

    #Move next
    pydirectinput.keyDown("shift")
    pydirectinput.keyDown("d")
    time.sleep(1.2)
    pydirectinput.keyUp("d")
    pydirectinput.keyDown("w")
    time.sleep(.3)
    pydirectinput.keyUp("w")
    pydirectinput.keyUp("shift")

    