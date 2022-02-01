import datetime
import webbrowser
import time
import pyautogui as jarvis
webbrowser.open('https://apps.skolaro.com/lecture-timetable/user')
time.sleep(3)

crnt_dateandtime=datetime.datetime.now() #diaplays date along with time
#we want only time as skolaro automatically updates date
time=crnt_dateandtime.strftime("%H:%M:%S")
hour=time[0:2]   #SEPERATING HOUR MINUTE AND SECOND
minute=time[3:5]
second=time[6:9]
#converting to integer for comparision
int_hour=int(hour)
int_mins=int(minute)
int_secs=int(second)
if int_hour == 8:
    if int_mins>=20 and int_mins<=25:
        class1_cords=jarvis.locateCenterOnScreen('classes\firstclass.png',confidence=0.8) #for 1st class
        if class1_cords!=None:
            print('cords founded :',class1_cords)
            jarvis.click(class1_cords)
        else:
            print('cords not found...')
    else:
        print('going on next time limit.....')
elif int_hour == 9:
    if int_mins>=10 and int_mins<=15:
        class2_cords=jarvis.locateCenterOnScreen('classes\secondclass.png',confidence=0.8) #2nd class
        if class2_cords!=None: 
            print('cords founded :',class2_cords)
            jarvis.click(class2_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')
elif int_hour== 10:
    if int_mins>=10 and int_mins<=15:
        class3_cords=jarvis.locateCenterOnScreen('classes\thirdclass.png',confidence=0.8) #3rd class
        if class3_cords!=None: 
            print('cords founded :',class3_cords)
            jarvis.click(class3_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')

elif int_hour== 11:
    if int_mins>=0 and int_mins<=5:
        class4_cords=jarvis.locateCenterOnScreen('classes\fourthclass.png',confidence=0.8) #4th class
        if class4_cords!=None: 
            print('cords founded :',class4_cords)
            jarvis.click(class4_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')

elif int_hour== 12:
    if int_mins>=0 and int_mins<=5:
        class5_cords=jarvis.locateCenterOnScreen('classes\fifthclass.png',confidence=0.8) #5th class
        if class5_cords!=None: 
            print('cords founded :',class5_cords)
            jarvis.click(class5_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')

elif int_hour== 1:
    if int_mins>=20 and int_mins<=25:
        class6_cords=jarvis.locateCenterOnScreen('classes\sixthclass.png',confidence=0.8) #6th class
        if class6_cords!=None: 
            print('cords founded :',class6_cords)
            jarvis.click(class6_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')
