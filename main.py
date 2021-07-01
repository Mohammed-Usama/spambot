# Automated text messaging

import time
import pyautogui

#coding
def SendMessage():
    time.sleep(10)
    text = open('Movie.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

SendMessage()