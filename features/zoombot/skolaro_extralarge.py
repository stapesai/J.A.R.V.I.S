import pyautogui as jarvis
def Skolaro_ExtraLarge():
    jarvis.sleep(3)
    normal_cord = jarvis.locateCenterOnScreen('skolaro_normal.png',confidence=0.8)
    if normal_cord!=None:
        x=normal_cord[0]
        y=normal_cord[1]
        jarvis.click(x,y)
        jarvis.press('pagedown')
        jarvis.press('enter')

        #now scrolling to down to find classes
        jarvis.click(960,540)
        
    else:
        print('cant find..')
 