import pydirectinput
import keyboard
import autoit
import time
from win32gui import FindWindow, GetWindowRect

time.sleep(2)
windowName = "Roblox"

def plant(input):
    autoit.mouse_move(x, y - input,1)
    autoit.mouse_move(x + 600, y - input ,50)


while keyboard.is_pressed("r") == False:
    window_handle = FindWindow(None, windowName)
    window_rect = GetWindowRect(window_handle)  
    rect = window_rect
    
    #Window Size
    #x = rect[2] - rect[0]
    #y = rect[3] - rect[1]
    #print(x,y)

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
    time.sleep(1)
    pydirectinput.keyUp("d")
    pydirectinput.keyDown("w")
    time.sleep(.5)
    pydirectinput.keyUp("w")
    pydirectinput.keyUp("shift")

    