#call functions
import pyautogui as jarvis
jarvis.FAILSAFE=False   # This is to avoid the program to close when the mouse is not found
import time

'''
# Call Function
import call
import jarvis_speech_to_text #
import jarvis_text_to_speech #
import process_call #
import incoming_call_user
'''
#picking up call
def call_pick():
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

#jarvis_sppech to text

def jarvis_voice_recognition():
    import speech_recognition as jarvis_voice_recognition
    import pyaudio
    speech = jarvis_voice_recognition.Recognizer()
    with jarvis_voice_recognition.Microphone(device_index=None) as source:
        speech.adjust_for_ambient_noise(source, duration=0.2)       # Adjust for ambient noises
        print("Listening to call..............")
        #audio = speech.listen(source, timeout=2)
        audio = speech.listen(source)
        global text
        text_dict_old = speech.recognize_google(audio,  language='en-US', show_all=True)

        list_check = isinstance(text_dict_old, list)
        if list_check == True:
            text_dict_old = {'alternative': [{'transcript': 'Could Not Understand.... Can You please Repeat it ', 'confidence': 0.92995489}, {'transcript': 'helo'}, {'transcript': 'hallo'}, {'transcript': 'yellow'}, {'transcript': 'hello I'}], 'final': True}
            print('in if loop')
        print(text_dict_old)
        # print('type text_dict_old is : ',type(text_dict_old))
        #print('Dict Keys are : ',text.values())
        x = list(text_dict_old.values())
        # print(type(x))
        text = list(x[0][0].values())[0]
        print("You said : {}".format(text))
        return text

def Check_Microphone():
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


#jarvis text to speech 

def jarvis_speak(my_text):
    from gtts import gTTS
    from playsound import playsound
    
    # USing gTTs
    #language='en'
    #output=gTTS(text=my_text,lang=language,slow=False)
    #output.save('output.mp3')
    #playsound('output.mp3')

    # Using pyttsx3
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    newVoiceRate = 135
    engine.setProperty('rate',newVoiceRate)
    #newVolume = 1.0
    #engine.setProperty('volume', newVolume)
    engine.say(my_text)
    #engine.save_to_file(my_text,'output.mp3')
    engine.runAndWait()

    # Common Steps...
    #os.system('start output.mp3')
    #os.remove('output.mp3')

#process call
def Process_Call(text_input):
    import randomise_voice_reply
    # CSV Synthesize...
    import csv
    bot_data_open = open('bot_data_lst.csv')
    bot_data_reader = csv.reader(bot_data_open)
    list_bot_data = list(bot_data_reader)
    #print(list_bot_data)

    print('--'*50)
    global bot_user_input
    bot_user_input=text_input
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
                    bot_reply = randomise_voice_reply.Randomised_Bot_Reply(bot_msg)
                    return bot_reply                
                else:
                    print('The Loop has jumped in else statement')      # Error: The Loop is jumping to else...
            print('Bot msg on Pos-01 : ',bot_msg)
        print('Pointer is at last position')

    bot_data_open.close()
    print('--'*50)
    
    bot_reply = randomise_voice_reply.Randomised_Bot_Reply(bot_msg)
    return bot_reply 
    
#caller_name
import pytesseract
import pyautogui
from PIL import ImageGrab

def Caller_Name():
    attend_call_cordinates=pyautogui.locateCenterOnScreen('img\call_attend.png', confidence=0.7)
    if attend_call_cordinates!=None:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Reinstall Tesseract-OCR in this location 'C:\Program Files\Tesseract-OCR'
        cap = ImageGrab.grab(bbox =(1630, 85, 1910, 130))
        ocr = pytesseract.image_to_string(cap, lang ='eng')
        return ocr
    else:
        return 'No incoming call user....'