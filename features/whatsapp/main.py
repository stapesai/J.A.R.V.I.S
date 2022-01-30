import time
import pyautogui as jarvis
import emoji
# import os
# Importing Files
import Open_WhatsApp
import Find_Unread_Msg
import Copy_Msg
import Reply_Bot
import jump_to_pw
import randomise_bot_reply

# Call Function
import call
import jarvis_speech_to_text
import jarvis_text_to_speech
import process_call
import incoming_call_user

def Whatsapp_Automate():
    # Basic Functions......
    Open_WhatsApp.Open_WhatsApp()
    time.sleep(3)
    jump_to_pw.jump_to_pw()

    # Reply Messages....
    while True:
        time.sleep(2)
        Find_Unread_Msg.Find_Unread_Msg()
        if Find_Unread_Msg.Find_Unread_Msg()==True:
            Copy_Msg.Copy_Msg()
            Reply_Bot.Bot_Reply()
            print('Bot_msg that came in main_chatbot.py : ',Reply_Bot.Bot_Reply())
            jarvis.write(emoji.emojize(randomise_bot_reply.Randomised_Bot_Reply())+' *-Jarvis*')        # Writes reply
            jarvis.press('enter',presses=2, interval=1)
            jump_to_pw.jump_to_pw()
            import bot_append_new_keywords
            bot_append_new_keywords.Append_Keywords()

        # Attending calls....
        user = incoming_call_user.Caller_Name()
        print(user)
        time.sleep(1)
        call.attend_call()
        
        if call.attend_call_cordinates!=None:
            jarvis_text_to_speech.jarvis_speak('Hello ' + user + 'I am jarvis, AI bot made by swastik')
            while True:
                print('Call Attended........')
                user_said = jarvis_speech_to_text.jarvis_voice_recognition()
                print('User said : ',user_said)
                speak_to_user = process_call.Process_Call(user_said)
                jarvis_text_to_speech.jarvis_speak(speak_to_user)
                print('user has been answered........')
                print('speak to user :',speak_to_user)
                if speak_to_user == 'Good Bye Sir have a nice day':
                    call.cut_call()
                    break

while True:
    Whatsapp_Automate()