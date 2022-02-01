import pyautogui as jarvis
def Skolaro_ExtraLarge():
    jarvis.sleep(3)
    normal_cord = jarvis.locateCenterOnScreen('skolaro_normal.png')
    if normal_cord!=None:
        x=normal_cord[0]
        y=normal_cord[1]
        jarvis.click(x,y)
        jarvis.press('pagedown')
        jarvis.press('enter')
Skolaro_ExtraLarge()