import os
import time
import pyautogui
os.system("clear")

default = 0000

for i in range(9999):
    default = str(default + 1)
    if len(default) == 1:
        default = "000" + str(default)
    elif len(default) == 2:
        default = "00" + str(default)
    if len(default) == 3:
        default = "0" + str(default)

    pyautogui.write(default)
    pyautogui.hotkey("enter")
    default = int(default)
