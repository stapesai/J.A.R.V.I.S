#Import Files
import pyautogui
import Alt_Tab
import Ctrl_C
import Ctrl_V
# Sleep Code
n=int(input('No of links to be pasted : '))
pyautogui.sleep(1)

# Primary Steps:
# 0.Press Alt Tab
Alt_Tab.Alt_Tab()
# 1.Open Software
pyautogui.click(x=1, y=1, clicks=1)
pyautogui.write('hd')
pyautogui.press('enter')
pyautogui.sleep(15)

# 2.Click Download Button
pyautogui.click(x=844, y=765, clicks=1)


# Paste Links:

for i in range(n):
    # Click New Download Button
    pyautogui.click(x=511, y=271, clicks=1)
    # Press Alt Tab
    Alt_Tab.Alt_Tab()
    # Press Ctrl+C
    Ctrl_C.Ctrl_C()
    # Press Alt Tab
    Alt_Tab.Alt_Tab()
    # Press Ctrl+V
    Ctrl_V.Ctrl_V()
    # Click Analyze Button
    pyautogui.click(x=1179, y=274, clicks=1)
    pyautogui.sleep(10)
    # Click OK Button
    pyautogui.click(x=1096, y=853, clicks=1)
    pyautogui.sleep(2)
    # Press Alt Tab
    Alt_Tab.Alt_Tab()
    # Next Link
    pyautogui.press('enter')
    pyautogui.press('enter')
    # Press Alt Tab
    Alt_Tab.Alt_Tab()
