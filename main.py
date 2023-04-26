import pyautogui as gui
import keyboard as kb
import time as t
import sys
cps = int(input("Enter cps: "))
key = input("Enter key input and key output: ")
if len(key) >= 2:
    while True:
        if kb.is_pressed(key[0]) == True:
            for x in range(cps):
                gui.press(key[1])
        elif kb.is_pressed("q") == True:
            sys.exit()
                
        else: continue
else:
    sys.exit()
