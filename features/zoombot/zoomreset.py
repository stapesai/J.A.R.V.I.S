import pyautogui as jarvis
def ZoomReset():
    jarvis.sleep(3)
    jarvis.keyDown('ctrl')
    jarvis.press('+')
    zoom_cord = jarvis.locateCenterOnScreen('zoom_reset.png',confidence=0.8)
    if zoom_cord!=None:
        jarvis.click(zoom_cord)
    jarvis.keyUp('ctrl')

ZoomReset()