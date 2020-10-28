import keyboard
import mouse
import time
import os
import pyautogui

time.sleep(10)
distance = 700

while distance > 2:

        pyautogui.dragRel(distance, 0, duration=0.0000)   # move right

        distance -= 7

        pyautogui.dragRel(0, distance, duration=0.0000)   # move down

        pyautogui.dragRel(-distance, 0, duration=0.000)  # move left

        distance -= 7

        pyautogui.dragRel(0, -distance, duration=0.000)  # move up
