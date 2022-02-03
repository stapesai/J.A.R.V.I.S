import time
import pyautogui as jarvis
import webbrowser
import datetime
jarvis.FAILSAFE = False
def Join_Class():
    # Joining meeting...
    '''
    while True:
        open_cord = jarvis.locateCenterOnScreen('edge_zoom_open.png', confidence =0.8) or jarvis.locateCenterOnScreen('chrome_zoom_open.png',confidence=0.8)
        if open_cord !=None:
            jarvis.click(open_cord)
            jarvis.jarvis.sleep(10)
            break
    '''
    # Checking waiting for host....
    waiting_for_host = jarvis.locateCenterOnScreen('waiting_for_host.png', confidence =0.8)
    while True:
        if waiting_for_host == None:
            jarvis.jarvis.sleep(5)
            break            
        else:
            print('waiting for host to start this meeting....')
            jarvis.jarvis.sleep(5)
            i=0
            # Closing Zoom after 9 min....
            if i==108:     # this is set in reference of 5 secs jarvis.jarvis.sleep 
                center_cord = (960,540)
                jarvis.click(center_cord)
                jarvis.jarvis.sleep(1)
                jarvis.hotkey('alt','f4')
                print('zoom closed successfully....')
                return
                
            else:
                i+=1
    # Enter Meeting Passcode...
    while True:
        passcode_box = jarvis.locateCenterOnScreen('enter_passcode.png', confidence =0.8)
        if passcode_box!=None:
            jarvis.click(passcode_box)
            jarvis.write('david')
            join_meeting = jarvis.locateCenterOnScreen('join_meeting.png', confidence =0.8)
            jarvis.click(join_meeting)
            jarvis.sleep(10)
            passcode_box2 = jarvis.locateCenterOnScreen('enter_passcode.png', confidence =0.8)
            if passcode_box2!=None:
                jarvis.click(passcode_box2)
                jarvis.write('am2119')
                join_meeting = jarvis.locateCenterOnScreen('join_meeting.png', confidence =0.8)
                jarvis.click(join_meeting)
                jarvis.sleep(10)
                break
            break
        else:
            break
    
    # Check Waiting Room...
    while True:
        waiting_room = jarvis.locateCenterOnScreen('waiting_room.png', confidence =0.8)
        jarvis.hotkey('winleft','up')
        print('In waiting Room sir ......')
        # Join with video....
        join_with_video = jarvis.locateCenterOnScreen('join_with_video.png', confidence =0.8)
        if join_with_video != None:
            jarvis.click(join_with_video)
            jarvis.sleep(5)
        if waiting_room == None:
            jarvis.sleep(5)
            print('Out of waiting room ......')
            start_video = jarvis.locateCenterOnScreen('start_video.png', confidence =0.8)
            if start_video != None:
                break
            break
        else:
            continue           

jarvis.sleep(5)
Join_Class()
Main()