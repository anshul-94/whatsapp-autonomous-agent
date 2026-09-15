import pyautogui
import time

print("SCREEN SIZE:", pyautogui.size())

while True:
    x, y = pyautogui.position()
    print("X:", x, "Y:", y)
    time.sleep(1)
