import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(10)
for i in range(2):
    pyautogui.press("k")
    pyautogui.press("a")
    pyautogui.press("i")
    pyautogui.press("s")
    pyautogui.press("a")
    pyautogui.press(" ")
    pyautogui.press("h")
    pyautogui.press("a")
    pyautogui.press("i")
    pyautogui.press("enter")