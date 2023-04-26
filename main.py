import pyautogui as gui
import keyboard as kb
import time as t
import sys
key = input("Enter key input and key output")
if len(key) >= 2:
    while True:
        if kb.is_pressed(key[0]) == True:
            gui.press(key[1])
        else: continue
else:
    sys.exit()
