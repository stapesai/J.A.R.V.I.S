import time
import speech_recognition as sr
import multiprocessing as mp
# import threading as th
import winsound as ws 
# import pyautogui as jarvis
import datetime
# import os

import features.whatsapp.main_call as call

# saving logs
import logging

def initiate_logs():
    logging.info('-------------------------------------'*4)

    logging.info('Jarvis log at {}'.format(datetime.datetime.now()))

logging.basicConfig(
                    filename='logs\log.log',
                    filemode='a', 
                    format='%(name)s - %(levelname)s - %(message)s - %(asctime)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG
                    )

def save_logs(text, type):
    if type == 'error':
        logging.error(text)
    elif type == 'warning':
        logging.warning(text)
    elif type == 'info':
        logging.info(text)
    elif type == 'debug':
        logging.debug(text)
    elif type == 'critical':
        logging.critical(text)
    elif type == 'exception':
        logging.exception(text)
    else:
        logging.warning('No such log type exists, log is : '+ text)

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
        save_logs('Listening........', 'info')
        audio = speech.listen(source, timeout=tout, phrase_time_limit=ptlimit)                

        try:
            text = speech.recognize_google(audio, language='en-US').lower()
            print("You said : {}".format(text))
            save_logs('You said : {}'.format(text), 'info')
            return text

        except:
            print("Could not understand what you said")
            save_logs('Could not understand what you said', 'warning')
            return "Could not understand what you said".lower()


# text to speech
def jarvis_speak(text):
    print('Jarvis : ', text)
    save_logs('Jarvis : {}'.format(text), 'info')
    engine.say(text)
    engine.runAndWait()

# background music
def background_music(signal):
    if signal == 'start':
        ws.PlaySound('music\IronMan_Theme_Song.wav', ws.SND_ASYNC | ws.SND_ALIAS)
        print('Background music started')
        save_logs('Background music started', 'info')

    elif signal == 'stop':
        ws.PlaySound(None, ws.SND_ASYNC)
        print('Background music stopped')
        save_logs('Background music stopped', 'info')
    
    return

# 1. reply function
import reply as rep

# 2. check new incoming call process
def check_new_call():
    while True:
        chk_call = call.check_incoming_call()
        if chk_call == True:
            jarvis_speak('Sir, there is a new call')

            sleep(5)
        if chk_call == False:
            print('There is no new call')
            save_logs('There is no new call', 'info')

check_call_process = mp.Process(target=check_new_call)


# main function
def main(count=0):
    while True:
        hotword_detection()

        count += 1
        text = jarvis_voice_recognise(ptlimit=5)
        ans = rep.reply(text)
        jarvis_speak(ans)

        print('This is trial number "{}" at "{}"'.format(count, datetime.datetime.now()))
        save_logs('This is trial number "{}" at "{}"'.format(count, datetime.datetime.now()), 'debug')
main_process = mp.Process(target=main)



if __name__ == '__main__':
    initiate_logs()
    background_music('start')
    jarvis_speak('welcome back sir , all systems are online')
    background_music('stop')

    main_process.start()
    check_call_process.start()