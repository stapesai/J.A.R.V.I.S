# Importing Modules....
import time
import pyautogui as jarvis
import webbrowser
import datetime

def Current_DateTime():
    day = (datetime.datetime.today().strftime('%A')).lower()        # Current Day

    crnt_dateandtime=datetime.datetime.now()      
    time=crnt_dateandtime.strftime("%H:%M:%S")
    hour=time[0:2]
    crt_hour=int(hour)

    return day, crt_hour

def delta_days(inp_day):
    if inp_day == 'monday':
        return 0
    elif inp_day == 'tuesday':
        return 1
    elif inp_day == 'wednesday':
        return 2
    elif inp_day == 'thursday':
        return 3
    elif inp_day == 'friday':
        return 4
    elif inp_day == 'saturday':
        return 5
    elif inp_day == 'sunday':
        return None

def ZoomReset():
    jarvis.sleep(3)
    jarvis.hotkey('ctrl','+')
    zoom_cord = jarvis.locateCenterOnScreen('edge_reset.png',confidence=0.8) or jarvis.locateCenterOnScreen('chrome_reset.png',confidence=0.8)
    if zoom_cord!=None:
        jarvis.click(zoom_cord)

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
    ZoomReset()

def Join_Class():
    # Before 9 AM


    # After 9 AM
    day, crt_hour = Current_DateTime()
    print(f'Today Day is "{day}" and hour "{crt_hour}"')

    initial_cord = (829, 381)
    jarvis.moveTo(initial_cord)

    






# OneTimeProcess()      # Working Process....
Join_Class()