# Importing Modules....
import time
import pyautogui as jarvis
import webbrowser

def sleep(n):
    time.sleep(n)

def Open_OBS_Studio():

    # Opening OBS....
    jarvis.press('winleft')
    jarvis.sleep(1)
    jarvis.write('obs')
    jarvis.sleep(1)
    jarvis.press('enter')
    
    # Starting Virtual Cam
    while True:
        cords=jarvis.locateCenterOnScreen('start_virtual_cam.png',confidence=0.8)
        if cords!=None:
            print('cords founded',cords)
            jarvis.click(cords)
            break
        else:
            print('cannot start virtual camera......')

def Open_Skolaro():
    webbrowser.open('https://apps.skolaro.com/lecture-timetable/user')
    sleep(5)

    # if skoalro is not signed in...
    sign_in_cord=jarvis.locateCenterOnScreen('sign_in.png',confidence=0.8)
    if sign_in_cord != None:
        print('signing in..')
        jarvis.click(sign_in_cord)
        sleep(3)
    
    # Jumping to main class shedule...
    center_cord = (960,540)
    jarvis.click(center_cord)
    jarvis.press('down',presses=5, interval=0.1)

# Main Body Of Program
def OneTimeProcess():
    Open_OBS_Studio()         # Starting Virtual Cam
    Open_Skolaro()            # Opening Skolaro (Ignoring Homeroom)

OneTimeProcess()