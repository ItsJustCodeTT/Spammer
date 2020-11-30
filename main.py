import pyautogui

text = "Insert Your Text here"

#Change the Coordinates here
xAxis = 670
yAxis = 1046

pyautogui.moveTo(xAxis,yAxis)
pyautogui.click()
for i in range(0,10):
    pyautogui.write(text)
    pyautogui.press('enter')