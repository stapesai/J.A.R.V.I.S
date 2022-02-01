import datetime
import webbrowser

import pyautogui as jarvis 

#opening obs 
import open_obs
open_obs.openobsstudio() 
jarvis.sleep(3)

#opening skolaro 
webbrowser.open('https://apps.skolaro.com/lecture-timetable/user')

#resetting browser zoom
import zoom_reset
zoom_reset.ZoomReset()
jarvis.sleep(3)

#skolaro extra large
import skolaro_extralarge
skolaro_extralarge.Skolaro_ExtraLarge()

#scrolling down according to time

#checking current date and time
crnt_dateandtime=datetime.datetime.now()  #diaplays date along with time
#we want only time as skolaro automatically updates date
time=crnt_dateandtime.strftime("%H:%M:%S")
hour=time[0:2]   #SEPERATING HOUR MINUTE AND SECOND
minute=time[3:5]
second=time[6:9]
#converting to integer for comparision
int_hour=int(hour)
int_mins=int(minute)
int_secs=int(second)
jarvis.sleep(1)
if int_hour == 8:
    if int_mins>=20 and int_mins<=25:
        class1_cords=jarvis.locateOnScreen('classes\firstclass.png',confidence=0.8) #for 1st class
        jarvis.press('down',presses=17,interval=0.3)
        if class1_cords!=None:
            print('cords founded :',class1_cords)
            jarvis.click(class1_cords)
        else:
            print('cords not found...')
    else:
        print('going on next time limit.....')
elif int_hour == 9:
    if int_mins>=10 and int_mins<=15:
        jarvis.press('down',presses=25,interval=0.3)
        class2_cords=jarvis.locateOnScreen('classes\secondclass.png',confidence=0.8) #2nd class
        if class2_cords!=None: 
            print('cords founded :',class2_cords)
            jarvis.click(class2_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')
elif int_hour== 10:
    if int_mins>=10 and int_mins<=15:
        jarvis.press('down',presses=35,interval=0.3)
        class3_cords=jarvis.locateOnScreen('classes\thirdclass.png',confidence=0.8) #3rd class
        if class3_cords!=None: 
            print('cords founded :',class3_cords)
            jarvis.click(class3_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')

elif int_hour== 11:
    if int_mins>=0 and int_mins<=5:
        jarvis.press('down',presses=45,interval=0.3)
        class4_cords=jarvis.locateOnScreen('classes\fourthclass.png',confidence=0.8) #4th class
        if class4_cords!=None: 
            print('cords founded :',class4_cords)
            jarvis.click(class4_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')

elif int_hour== 12:
    if int_mins>=0 and int_mins<=5:
        jarvis.press('down',presses=62,interval=0.3)
        class5_cords=jarvis.locateOnScreen('classes\fifthclass.png',confidence=0.8) #5th class
        if class5_cords!=None: 
            print('cords founded :',class5_cords)
            jarvis.click(class5_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')

elif int_hour== 13:
    if int_mins>=20 and int_mins<=59:
        jarvis.press('down',presses=73,interval=0.1)
        class6_cords=jarvis.locateOnScreen('classes\sixthclass.png',confidence=0.8) #6th class
        x=class6_cords[0]+85
        y=class6_cords[1]-37
        if class6_cords!=None: 
            print('cords founded :',class6_cords)
            jarvis.click(x,y)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')
else:
    print('currently no classes ')


#now zoom opening along with cam on

import class_join_zoom
class_join_zoom.Class_Join()