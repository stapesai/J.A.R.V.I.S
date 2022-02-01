import pyautogui as jarvis
def Skolaro_ExtraLarge():
    jarvis.sleep(1)
    normal_cord = jarvis.locateCenterOnScreen('skolaro_normal.png',confidence=0.8)
    if normal_cord!=None:
        x=normal_cord[0]
        y=normal_cord[1]
        jarvis.click(x,y)
        jarvis.sleep(1)
        jarvis.press('pagedown')
        jarvis.sleep(1)
        jarvis.press('enter')
        
        #now clicking on the blank space in order to get keydown access
        jarvis.click(960,540)
        
    else:
        print('cant find..')
 