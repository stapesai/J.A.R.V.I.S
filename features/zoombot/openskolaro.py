import datetime
import webbrowser
import pyautogui as jarvis
webbrowser.open('https://apps.skolaro.com/lecture-timetable/user')

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
        class1_cords=jarvis.locateCenterOnScreen('firstclass.png',confidence=0.8) #for 1st class
        if class1_cords!=None:
            print('cords founded :',class1_cords)
            jarvis.click(class1_cords)
        else:
            print('cords not found...')
    else:
        print('going on next time limit.....')
elif int_hour == 9:
    if int_mins>=10 and int_mins<=15:
        class2_cords=jarvis.locateCenterOnScreen('hoursize.png',confidence=0.8)
        if class2_cords!=None:
            print('cords founded :',class2_cords)
            jarvis.click(class2_cords)
        else:
            print('cords not found')
    else:
        print('going on next time limit...')
elif int_hour== 10:
    if int_mins:
        pass
# to be continued