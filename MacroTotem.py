import time
import pydirectinput

pydirectinput.PAUSE = 0.05

#Countdown variable
countdown = reversed(range(1,4))

#Starts Program before time runs out.
for t in countdown:
        print("Starting in", t)
        time.sleep(1)

while True:
    pydirectinput.keyDown("w")
    pydirectinput.keyDown("shift")
    pydirectinput.press("f")