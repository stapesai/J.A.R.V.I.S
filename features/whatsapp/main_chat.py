# Chat Functions
import pyautogui as jarvis
jarvis.FAILSAFE=False   # This is to avoid the program to close when the mouse is not found
import time
import reply_engine
message='sample'
import pyperclip

# Defineing Functions
def sleep(n):
    time.sleep(n)

def Open_WhatsApp():
    jarvis.press('winleft')
    sleep(1)
    jarvis.write('WhatsApp')
    sleep(1)
    jarvis.press('enter')

def Find_Unread_Msg():
    Unread_Msg=jarvis.locateCenterOnScreen('img\green_dot.png', confidence=0.7) # This is to find the green dot
    print('Unread message Location : ',Unread_Msg)
    if Unread_Msg!=None:
        print('There is a new Message ....')
        x=Unread_Msg[0]-30
        y=Unread_Msg[1]
        jarvis.click(x, y)
    else:
        print('No New Message Found....')

def jump_to_pw():
    pw_cordinates=jarvis.locateCenterOnScreen('img\pw_logo.png', confidence=0.5)
    if pw_cordinates!=None:
        print('Jumpinging To PW....',pw_cordinates)
        x=pw_cordinates[0]
        y=pw_cordinates[1]
        jarvis.click(x, y)
    else:
        print('Can not jump to PW....')

def Copy_Msg():
    Copy_Msg=jarvis.locateCenterOnScreen('img\smiley.png', confidence=0.5)
    if Copy_Msg!=None:
        x=Copy_Msg[0]+30
        y=Copy_Msg[1]-70
        jarvis.moveTo(x,y)
        jarvis.tripleClick()
        jarvis.keyDown('ctrl')
        jarvis.write('c')
        jarvis.keyUp('ctrl')
        global message
        message = pyperclip.paste()
        jarvis.click()
        print("message received: " + message)
        
        # Clicking on text box
        Click_On_Text_Box=jarvis.locateCenterOnScreen('img/textbox.png', confidence=0.5)
        if Click_On_Text_Box!=None:
            jarvis.click(Click_On_Text_Box[0], Click_On_Text_Box[1])
        
        return message
    else:
        print('None')

def Append_Keywords(msg, file = 'bot_new_keywords_data.txt'):
    bot_data_open2 = open(file,'a')
    new_keyword = str(msg.lower())
    print('New Keyword is : ',new_keyword)

    # Removing Emoji
    import re
    emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
    u"\U00002500-\U00002BEF"  # chinese char
    u"\U00002702-\U000027B0"
    u"\U00002702-\U000027B0"
    u"\U000024C2-\U0001F251"
    u"\U0001f926-\U0001f937"
    u"\U00010000-\U0010ffff"
    u"\u2640-\u2642" 
    u"\u2600-\u2B55"
    u"\u200d"
    u"\u23cf"
    u"\u23e9"
    u"\u231a"
    u"\ufe0f"  # dingbats
    u"\u3030"
                "]+", re.UNICODE)
    new_keyword_unicode = emoji_pattern.sub(r'', new_keyword)
    print('Keyword after removing emoji : ', new_keyword_unicode)
    bot_data_open2.write(new_keyword_unicode+'\n')
    print('Message appended : ', new_keyword)
    bot_data_open2.close()
    print('Keywords are appended') 


# Defining Main Function
def main():
    jump_to_pw()
    Find_Unread_Msg()
    msg = Copy_Msg()
    reply_engine.Reply_Engine(msg)
    jarvis.write(msg)
    sleep(1)
    jarvis.press('enter', presses=2, interval=0.5)

    if msg == 'No Such Keyword found in directory':
        print('Appending Keywords....')
        Append_Keywords(msg)

# Calling Main Function
Open_WhatsApp()
while True:
    main()
