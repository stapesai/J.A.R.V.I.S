import pyautogui as jarvis
def Class_Join():
    # Joining meeting....
    open_cord = jarvis.locateCenterOnScreen('zoom_open.png', confidence =0.8) or jarvis.locateCenterOnScreen('chrome_zoom_open.png',confidence=0.8)
    jarvis.click(open_cord)

    # Turn on camera using hotkey.....
    #now appending waiting room pic 
    waiting_rm_cords=jarvis.locateCenterOnScreen('waiting_room.png',confidence=0.8)
    if waiting_rm_cords == None:
        jarvis.sleep(10)
        jarvis.hotkey('alt','v')          