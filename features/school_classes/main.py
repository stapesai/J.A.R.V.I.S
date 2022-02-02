# Importing Modules....
import time
import pyautogui as jarvis
import webbrowser
import datetime
jarvis.FAILSAFE = False

def Current_DateTime():
    day = (datetime.datetime.today().strftime('%A')).lower()        # Current Day

    crnt_dateandtime=datetime.datetime.now()      
    time=crnt_dateandtime.strftime("%H:%M:%S")

    hour=time[0:2]
    crt_hour=int(hour)

    minute = time[3:5]
    crt_min = int(minute)

    return day, crt_hour, crt_min

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
    jarvis.hotkey('ctrl','+')
    zoom_cord = jarvis.locateCenterOnScreen('edge_reset.png',confidence=0.8) or jarvis.locateCenterOnScreen('chrome_reset.png',confidence=0.8)
    if zoom_cord!=None:
        jarvis.click(zoom_cord)
        print('Sir zoom has been reseted successfully !!!!')

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
            print('Sir, start virtual camera has been started successfully......')
            break
        else:
            sleep(10)
            print('cannot start virtual camera......')

def Open_Skolaro():
    webbrowser.open('https://apps.skolaro.com/lecture-timetable/user')
    sleep(5)

    # if skoalro is not signed in...
    sign_in_cord=jarvis.locateCenterOnScreen('sign_in.png',confidence=0.8)
    if sign_in_cord != None:
        jarvis.click(sign_in_cord)
        print('signined in successfully...')
        sleep(3)
    
    # Jumping to main class shedule...
    center_cord = (960,540)
    jarvis.click(center_cord)
    jarvis.press('down',presses=5, interval=0.1)
    print('Jumping to main class shedule...')
               
def Find_Class():
    day, crt_hour, crt_min = Current_DateTime()
    print(f'Today Day is "{day}" and hour "{crt_hour}" and min "{crt_min}"')

    initial_cord = (829, 381)
    jarvis.moveTo(initial_cord)
    delta_x = delta_days(day) * 95
    delta_y = 0
    jarvis.moveRel(delta_x,delta_y)
    while True:
        jarvis.moveRel(0,5)
        crt_cord = jarvis.position()
        jarvis.click(crt_cord)
        if jarvis.locateCenterOnScreen('feedback_support.png', confidence =0.5) == None:
            print('Sir class has been opened successfully....')
            break
        else:
            jarvis.press('enter')

def Join_Class():
    # Joining meeting...
    while True:
        open_cord = jarvis.locateCenterOnScreen('edge_zoom_open.png', confidence =0.8) or jarvis.locateCenterOnScreen('chrome_zoom_open.png',confidence=0.8)
        if open_cord !=None:
            jarvis.click(open_cord)
            sleep(10)
            break
    sleep(5)
    # Enter Meeting Passcode...
    while True:
        passcode_box = jarvis.locateCenterOnScreen('enter_passcode.png', confidence =0.8)
        if passcode_box!=None:
            jarvis.click(passcode_box)
            jarvis.write('david')
            sleep(10)
            passcode_box2 = jarvis.locateCenterOnScreen('enter_passcode.png', confidence =0.8)
            if passcode_box2!=None:
                jarvis.click(passcode_box2)
                jarvis.write('am2119')
                sleep(10)
                break
            break
        else:
            break
    
    # Check Waiting Room...
    while True:
        waiting_room = jarvis.locateCenterOnScreen('waiting_room.png', confidence =0.8)
        if waiting_room == None:
            sleep(5)
            print('In waiting Room sir ......')
            start_video = jarvis.locateCenterOnScreen('start_video.png', confidence =0.8)
            if start_video != None:
                break
            break
    
    # Turn ON camera...
    jarvis.hotkey('alt','v')
    start_video = jarvis.locateCenterOnScreen('start_video.png', confidence =0.9)
    while True:
        if start_video == None:
            break
        else:
            jarvis.click(start_video)
            break

# Main Body Of Program
Open_OBS_Studio()       # Starting Virtual Cam
ZoomReset()         

def Main():
    Open_Skolaro()      # Opening Skolaro (Ignoring Homeroom)
    sleep(2)
    Find_Class()
    sleep(2)
    Join_Class()



# Continious Run....
while True:
    crt_time = str(Current_DateTime()[1]) + ':' + str(Current_DateTime()[2])
    crt_day = str(Current_DateTime()[0])
    print('current time is : ',crt_time)

    if crt_day!='monday':
        if '8:0' == crt_time or '8:20' == crt_time or'9:10' == crt_time or'10:10' == crt_time or'11:0' == crt_time or'12:0' == crt_time or'13:20' == crt_time:
            Main()
            class_join_confirm = jarvis.locateCenterOnScreen('class_join_confirm.png', confidence=0.8)
            if class_join_confirm != None:
                print('Sir Class is joined confirmly.....')
                sleep(3000)
    else:
        if '8:0' == crt_time or '9:10' == crt_time or'10:10' == crt_time or'11:0' == crt_time or'12:0' == crt_time or'13:20' == crt_time:
            Main()
            class_join_confirm = jarvis.locateCenterOnScreen('class_join_confirm.png', confidence=0.8)
            if class_join_confirm != None:
                print('Sir Class is joined confirmly.....')
                sleep(3000)
    
    sleep(30)