import pyautogui
import Alt_Tab
n=int(input('No of links to be edited : '))
pyautogui.sleep(1)
# Press Alt Tab
Alt_Tab.Alt_Tab()
for i in range(n):
    pyautogui.press('enter')
    pyautogui.press('home')
    for i in range(1,76):
        pyautogui.press('right')
    for i in range(20):
        pyautogui.press('del')
    pyautogui.write('master.m3u8')
    pyautogui.press('enter')