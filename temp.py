import pywhatkit
import datetime
'''
Type:
     jarvis send a message to ayush bansal that i am fine
     jarvis inform ayush bansal that i am fine
     jarvis tell ayush bansal that i am fine
     jarvis inform kshitij that i am fine
     jarvis 
'''

crt_hr = int(datetime.datetime.now().strftime("%H"))
crt_min = int(datetime.datetime.now().strftime("%M"))
pywhatkit.sendwhatmsg(phone_no = '+919560355384', 
message = 'jarvis send a message to ayush bansal that i am fine', 
time_hour = crt_hr, 
time_min = crt_min+2, 
tab_close=True)