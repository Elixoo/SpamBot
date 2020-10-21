import time
import pyautogui

time.sleep(5)
f = open("bees", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")