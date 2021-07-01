'''@Author:- Mohammed Usama, created on 01-07-2021, 20:10. ''' 
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
