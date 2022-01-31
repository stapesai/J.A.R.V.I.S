import pyautogui as zoombot

def openskolaro():
    zoombot.press('winleft')
    zoombot.sleep(1)
    zoombot.write('chrome')
    zoombot.press('enter')
    zoombot.sleep(5)
    zoombot.hotkey('ctrl','t')
    print('--opening new tab')
    zoombot.write('skolaro')
    zoombot.press('enter')
    zoombot.sleep(3)
    zoombot.press('tab',presses=1)
    zoombot.press('enter',presses=2,interval=0.4)
    
def opentimetable():
   
    
    
openskolaro()