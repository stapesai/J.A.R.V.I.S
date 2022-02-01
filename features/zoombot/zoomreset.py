import pyautogui as jarvis
def ZoomReset():
    jarvis.sleep(3)
    jarvis.hotkey('ctrl','+')
    zoom_cord = jarvis.locateCenterOnScreen('edge_reset.png',confidence=0.8) or jarvis.locateCenterOnScreen('chrome_reset.png',confidence=0.8)
    if zoom_cord!=None:
        jarvis.click(zoom_cord)
    

ZoomReset()