import keyboard
import pydirectinput

pydirectinput.PAUSE = 0.001

while True:
    if keyboard.is_pressed("j"):
        pydirectinput.click()