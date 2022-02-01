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
    if int_mins>=20:
        pass

