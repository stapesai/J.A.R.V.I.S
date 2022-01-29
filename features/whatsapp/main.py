import time
from asyncio import sleep
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
# import live_speech_to_text
# Call Function
import call
import jarvis_speech_to_text
import jarvis_text_to_speech
import process_call
# import time_output
import incoming_call_user


#if 'jarvis' in live_speech_to_text.live_speech_to_text():
while True:
    # starting time
    start = time.time()
    #jarvis_text_to_speech.jarvis_speak('Hello Welcome Back Sir')
    # Basic Functions......
    Open_WhatsApp.Open_WhatsApp()
    time.sleep(3)
    jump_to_pw.jump_to_pw()

    # Reply Messages....
    while True:
    #if 'jarvis' in jarvis_speech_to_text.jarvis_voice_recognition():
        time.sleep(2)
        Find_Unread_Msg.Find_Unread_Msg()
        if Find_Unread_Msg.Unread_Msg!=None:
            Copy_Msg.Copy_Msg()
            Reply_Bot.Bot_Reply()
            print('Bot_msg that came in main_chatbot.py : ',Reply_Bot.Bot_Reply())
            jarvis.write(emoji.emojize(randomise_bot_reply.Randomised_Bot_Reply())+' *-Jarvis*')        # Writes reply
            jarvis.press('enter',presses=2, interval=1)
            jump_to_pw.jump_to_pw()
            import bot_append_new_keywords
            bot_append_new_keywords.Append_Keywords()

        # Attending calls....
        # time.sleep(2)
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
                #time.sleep(time_output.time_sleep())
                if speak_to_user == 'Good Bye Sir have a nice day':
                    #jarvis_text_to_speech.jarvis_speak('Bye Sir. Hope you enjoyed the conversation')
                    call.cut_call()
                    # os.remove('__pycache__')
                    break
        # end time
        end = time.time()

        # total time taken
        print(f"Runtime of the program is {end - start}")