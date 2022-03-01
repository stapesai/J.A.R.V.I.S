import time
import speech_recognition as sr
import multiprocessing as mp
import threading as th
import winsound as ws 
import pyautogui as jarvis
import datetime

import features.whatsapp.main_call as call

# hotword detection
import features.wake_word as wake_word      # pip install pvporcupine
def hotword_detection():
    wake_word.wake_word_detection(music_file='features\chime.wav', model=['voice_model\jarvis_windows.ppn','voice_model\hey-jarvis_windows.ppn'])

# initialize the recognizer
speech = sr.Recognizer()

# initialize the engine
import pyttsx3
engine = pyttsx3.init()     # initialise the engine

voices = engine.getProperty('voices')   
engine.setProperty('voice', voices[1].id)   # set the voice

newVoiceRate = 140
engine.setProperty('rate',newVoiceRate)    # set the speed rate

# sleep function
def sleep(sec):
    time.sleep(sec)

# speech to text
def jarvis_voice_recognise(tout=None, ptlimit=None):
    with sr.Microphone(device_index=1) as source:

        speech.adjust_for_ambient_noise(source, duration=0.5)       # Adjust for ambient noises
        print("Listening........")
        audio = speech.listen(source, timeout=tout, phrase_time_limit=ptlimit)                

        try:
            text = speech.recognize_google(audio, language='en-US').lower()
            print("You said : {}".format(text))
            return text

        except:
            print("Could not understand what you said")
            return "Could not understand what you said".lower()


# text to speech
def jarvis_speak(text):
    print('Jarvis : ', text)
    engine.say(text)
    engine.runAndWait()

# background music
def background_music(signal):
    if signal == 'start':
        ws.PlaySound('music\IronMan_Theme_Song.wav', ws.SND_ASYNC | ws.SND_ALIAS)
        print('Background music started')

    elif signal == 'stop':
        ws.PlaySound(None, ws.SND_ASYNC)
        print('Background music stopped')
    
    return

# reply function
def reply(text): 

    if 'jarvis' == text:
        jarvis_speak('Yes sir')

    elif 'hello' in text:
        jarvis_speak('Hello sir')

    elif 'how are you' in text:
        jarvis_speak('I am fine sir')

    elif 'your name' in text:
        jarvis_speak('My name is jarvis')

    elif 'your age' in text:
        jarvis_speak('My software is still in development mode')

    elif 'your job' in text or 'your profession' in text or 'what do you do' in text or 'who are you' in text:
        jarvis_speak('I am a virtual assistant')

    elif 'your favourite colour' in text:
        jarvis_speak('My favourite colour is blue')

    elif 'your favourite song' in text:
        jarvis_speak('My favourite song is Iron Man Songs')

    elif 'could not understand what you said' in text:
        jarvis_speak('Could not understand what you said')
        print('Could not understand what you said')
    
    # Features
    # 1. attending to calls
    elif 'attend my call' in text or 'respond to my call' in text or 'is there any call' in text or 'respond to call' in text or 'respond to incoming call' in text or 'respond to my call' in text:

        if call.check_incoming_call() == True:
            calling_process = mp.Process(target=call.__main__)

            if calling_process.is_alive() == False:
                calling_process.start()
                jarvis_speak('ok sir, now i am taking your call')
            
            elif calling_process.is_alive() == True:
                jarvis_speak('sir, i am already talking to your call')
        
        else:
            jarvis_speak('sorry sir, there is no new call')

    else:
        jarvis_speak('This is not programmed yet.')

# 2. check new incoming call process
def check_new_call():
    while True:
        chk_call = call.check_incoming_call()
        if chk_call == True:
            jarvis_speak('Sir, there is a new call')
            sleep(5)
        if chk_call == False:
            print('There is no new call')

check_call_process = mp.Process(target=check_new_call)

# main function
def main(count=0):
    while True:
        hotword_detection()

        count += 1
        text = jarvis_voice_recognise(ptlimit=5)
        reply(text)

        print('This is trial number "{}" at "{}"'.format(count, datetime.datetime.now()))

main_process = mp.Process(target=main)



if __name__ == '__main__':
    background_music('start')
    jarvis_speak('welcome back sir , all systems are online')
    background_music('stop')

    main_process.start()
    check_call_process.start()