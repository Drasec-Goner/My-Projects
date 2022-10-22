import mouse
import keyboard
import time

toggle = False

while True:
    if toggle:
        mouse.click("left")
        time.sleep(0.01)
    if keyboard.is_pressed("F"):
        toggle = not toggle
        time.sleep(1)