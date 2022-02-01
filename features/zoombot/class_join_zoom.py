import pyautogui as jarvis
def Class_Join():
    while True:
        # Joining meeting....
        jarvis.sleep(2)
        open_cord = jarvis.locateCenterOnScreen('zoom_open.png', confidence =0.8) or jarvis.locateCenterOnScreen('chrome_zoom_open.png',confidence=0.8)
        if open_cord !=None:
            jarvis.click(open_cord)
            break

    # Turn on camera using hotkey.....
    #now appending waiting room pic 
    waiting_rm_cords=jarvis.locateCenterOnScreen('waiting_room.png',confidence=0.8)
    if waiting_rm_cords == None:
        jarvis.sleep(10)
        jarvis.hotkey('alt','v')       