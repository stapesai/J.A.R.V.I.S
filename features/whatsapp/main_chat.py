# Chat Functions
import pyautogui as jarvis
jarvis.FAILSAFE=False   # This is to avoid the program to close when the mouse is not found
import time

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
        #jarvis.sleep(1)
    else:
        print('Can not jump to PW....')
message='sample'
import pyperclip
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
    else:
        print('None')

def Bot_Reply():
    # CSV Synthesize...
    import csv
    bot_data_open = open('bot_data_lst.csv')
    bot_data_reader = csv.reader(bot_data_open)
    list_bot_data = list(bot_data_reader)
    #print(list_bot_data)
    print('--'*50)
    global bot_user_input
    bot_user_input=Copy_Msg.message
    print('Bot Input is : ',bot_user_input)
    global bot_msg
    bot_msg=['No Such Keyword found in directory']
    print('Pointer is at 1st position')
    for data in list_bot_data:
        print('Pointer is in 1st for loop')
        #print(data)
        all_keyword = data[0]
        # Converting str all_keywords to list all_keywords
        import ast
        lst_bot_keyword = ast.literal_eval(all_keyword)
        print(type(lst_bot_keyword))
        print('All Keywords are',lst_bot_keyword)
        all_reply = data[1]
        bot_input = (bot_user_input.lower())
        for temp_keyword in lst_bot_keyword:
            print('temp keyword is : ',temp_keyword)
            for bot_keyword in temp_keyword.split():
                print('Comparing :',bot_keyword.lower(),'       with :',bot_user_input.lower())            
                # Bugs can be here...
                if bot_keyword.lower() in bot_input:
                    print('Comparing Successful.....')
                    #global bot_msg          # This statement is not working...
                    bot_msg=all_reply
                    print('Reply to User  is : ',bot_msg)
                    return bot_msg               
                else:
                    print('The Loop has jumped in else statement')      # Error: The Loop is jumping to else...
            #print('Bot msg on Pos-01 : ',bot_msg)
        #print('Pointer is at last position')
    bot_data_open.close()
    print('--'*50)
    
    return bot_msg
def Append_Keywords():
    # Importing necessary files...
    import Reply_Bot
    bot_msg = Reply_Bot.bot_msg
    bot_user_input = Reply_Bot.bot_user_input
    
    if bot_msg==['No Such Keyword found in directory']:
        # If the keyword is not found in directory then appending keyword in bot_data.csv
        # By r+ mode in temp file....
        bot_data_open2 = open('bot_new_keywords_data.txt','a')
        new_keyword = str(bot_user_input.lower())
        print('New Keyword is : ',new_keyword)
        # Removing Emoji
        # new_keyword_unicode = new_keyword.encode('ascii','ignore')
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
    return 'Keywords are appended'
def Give_Reply(message):
    print()

# Main Code to chat....
Open_WhatsApp()

# Main Body of main.py
# jarvis_chat()
# Open_WhatsApp()