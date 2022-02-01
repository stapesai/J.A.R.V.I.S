import datetime

now=datetime.datetime.now()
time=now.strftime("%H:%M:%S")
hour=time[0:2]   #SEPERATING HOUR MINUTE AND SECOND
minute=time[3:5]
second=time[6:9]
print(time)
int_hour=int(hour)
int_mins=int(minute)
int_secs=int(second)
print(int(hour))
print(int(minute))
print(int(second))
#if int_hour > 
