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
    crt_hour=hour

    minute = time[3:5]
    crt_min = minute #changing here
    
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

def start_virtual_cam():            #no need in main as integrated with open obs studio
    # Starting Virtual Cam
    while True:
        cords=jarvis.locateCenterOnScreen('start_virtual_cam.png',confidence=0.8) or jarvis.locateCenterOnScreen('start_video_fullscreen.png',confidence=0.8)
        if cords!=None:
            print('cords founded',cords)
            jarvis.click(cords)
            print('Sir, virtual camera has been started successfully......')
            break
        else:
            sleep(10)
            print('cannot start virtual camera......')
            continue

def Open_OBS_Studio():

    # Opening OBS....
    jarvis.press('winleft')
    jarvis.sleep(1)
    jarvis.write('obs')
    jarvis.sleep(1)
    jarvis.press('enter')
    jarvis.sleep(1)
    obs_already_running=jarvis.locateCenterOnScreen('obs_already_running.png',confidence=0.8)
    while True:        
        if obs_already_running != None:
            break
        elif obs_already_running == None:
            
            start_virtual_cam()
            continue


def Open_Skolaro():
    webbrowser.open('https://apps.skolaro.com/lecture-timetable/user')
    sleep(10)
    jarvis.hotkey('winleft','up')
    sleep(3)
    ZoomReset()

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
            sleep(1)
            jarvis.press('enter')

def Join_Class():
    # Joining meeting...
    while True:
        open_cord = jarvis.locateCenterOnScreen('edge_zoom_open.png', confidence =0.8) or jarvis.locateCenterOnScreen('chrome_zoom_open.png',confidence=0.8)
        if open_cord !=None:
            jarvis.click(open_cord)
            sleep(10)
            break

    # Enter Meeting Passcode...
    while True:
        passcode_box = jarvis.locateCenterOnScreen('enter_passcode.png', confidence =0.8)
        if passcode_box!=None:
            jarvis.click(passcode_box)
            jarvis.write('david')
            join_meeting = jarvis.locateCenterOnScreen('join_meeting.png', confidence =0.8)
            jarvis.click(join_meeting)
            sleep(10)
            passcode_box = jarvis.locateCenterOnScreen('enter_passcode.png', confidence =0.8)
            if passcode_box!=None:
                jarvis.click(passcode_box)
                jarvis.write('am2119')
                join_meeting = jarvis.locateCenterOnScreen('join_meeting.png', confidence =0.8)
                jarvis.click(join_meeting)
                sleep(10)
                
            break
        else:
            break
    
    # Checking waiting for host....
    waiting_for_host = jarvis.locateCenterOnScreen('waiting_for_host.png', confidence =0.8)
    while True:
        if waiting_for_host == None:
            sleep(5)
            break            
        else:
            print('waiting for host to start this meeting....')
            sleep(5)
            i=0
            # Closing Zoom after 9 min....
            if i==108:     # this is set in reference of 5 secs sleep 
                center_cord = (960,540)
                jarvis.click(center_cord)
                sleep(1)
                jarvis.hotkey('alt','f4')
                print('zoom closed successfully....')
                return
                
            else:
                i+=1
    
    # Check Waiting Room...
    while True:
        jarvis.hotkey('winleft','up')
        waiting_room = jarvis.locateCenterOnScreen('waiting_room.png', confidence =0.8)        
        print('In waiting Room sir ......')
        # Join with video....
        sleep(1)
        join_with_video = jarvis.locateCenterOnScreen('join_with_video.png', confidence =0.8)
        if join_with_video != None:
            jarvis.click(join_with_video)
            sleep(5)
        elif waiting_room == None:
            sleep(5)
            print('Out of waiting room ......')
            start_video = jarvis.locateCenterOnScreen('start_video.png', confidence =0.8)
            if start_video != None:
                sleep(1)
                jarvis.hotkey('alt','v')     # Turn ON camera...
                print('Sir camera has been started.....')
            break
        else:
            continue
         
def Main():
    Open_OBS_Studio()
    sleep(2)
    Open_Skolaro()      # Opening Skolaro (Ignoring Homeroom)
    sleep(2)
    Find_Class()
    sleep(2)
    Join_Class()
    jarvis.hotkey('winleft','up')


# Main Body Of Program
crt_time = str(Current_DateTime()[1]) + ':' + str(Current_DateTime()[2])
crt_day = str(Current_DateTime()[0])

if crt_time >='08:00' and crt_time <'14:00' and crt_day != 'sunday':

  #  Open_OBS_Studio()       # Starting Virtual Cam #integrated it
    while True:
        crt_time = str(Current_DateTime()[1]) + ':' + str(Current_DateTime()[2])
        crt_day = str(Current_DateTime()[0])
        print('current time is : ',crt_time)

        if crt_day =='sunday':
            print('No Class Today Sir....')
            break

        
        elif crt_day == 'monday' and crt_time >='08:00' and crt_time <'08:10':
            Main()    #why this thing not working
            class_join_confirm = jarvis.locateCenterOnScreen('class_join_confirm.png', confidence=0.8)
            if class_join_confirm != None:
                print('Sir Test is joined confirmly and you might need to submit your test answer sheet.....')
                print('sir I am going to sleep for 1.05 hrs...')
                sleep(3900)

            elif (crt_time >='08:00' and crt_time <'08:10'):
                Main()
                while True:
                    class_join_confirm = jarvis.locateCenterOnScreen('class_join_confirm.png', confidence=0.8)
                    if class_join_confirm != None:
                        jarvis.click(class_join_confirm)
                        jarvis.hotkey('winleft','up')
                        sleep(1)            
                        print('Sir homeroom Class is joined confirmly.....')
                        print('sir I am going to sleep for 20 mins....')
                        sleep(1200)
                        break

        elif ( 
        crt_time >='08:20' and crt_time <'09:00' or 
        crt_time >='09:10' and crt_time <'09:50' or 
        crt_time >='10:10' and crt_time <'10:50'or 
        crt_time >='11:00' and crt_time <'11:40' or 
        crt_time >='12:00' and crt_time <'12:40'or 
        crt_time >='13:20' and crt_time <'14:00'):
            Main()
            while True:
                class_join_confirm = jarvis.locateCenterOnScreen('class_join_confirm.png', confidence=0.8)
                if class_join_confirm != None:
                    jarvis.click(class_join_confirm)
                    jarvis.hotkey('winleft','up')
                    sleep(1)            
                    print('Sir Class is joined confirmly.....')
                    print('sir I am going to sleep for 50 mins....')
                    sleep(3000)
                    break

        sleep(30)
# code comple