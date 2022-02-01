import pyautogui as jarvis
def Class_Join():
    # Joining meeting....
    open_cord = jarvis.locateCenterOnScreen('zoom_open.png', confidence =0.8)
    jarvis.click(open_cord)

    # Turn on camera.....
    cam_cord = jarvis.locateCenterOnScreen('camera.png', confidence =0.8)
    jarvis.click(cam_cord)