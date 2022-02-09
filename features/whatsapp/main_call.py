# basic imports
import pyautogui as jarvis
jarvis.FAILSAFE=False   # This is to avoid the program to close when the mouse is not found
import time
import pytesseract
import pyautogui
from PIL import ImageGrab
import reply_engine

# sleep function
def sleep(sec):
    time.sleep(sec)

# speech to text
def jarvis_voice_recognise():
    import speech_recognition as sr
    speech = sr.Recognizer()

    with sr.Microphone(device_index=None) as source:

        speech.adjust_for_ambient_noise(source, duration=0.5)       # Adjust for ambient noises
        print("Listening to call..............")
        audio = speech.listen(source)                # set timeout here

        try:
            text = speech.recognize_google(audio, language='en-US')
            print("You said : {}".format(text))
            return text

        except:
            print("Could not understand what you said")
            return "Could not understand what you said"

# just a function to check the microphone
def Check_Microphone():
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# text to speech
def jarvis_speak(text):
    import pyttsx3
    engine = pyttsx3.init()     # initialise the engine

    voices = engine.getProperty('voices')   
    engine.setProperty('voice', voices[1].id)   # set the voice

    newVoiceRate = 135
    engine.setProperty('rate',newVoiceRate)    # set the speed rate

    engine.say(text)
    engine.runAndWait()

# caller name
def Caller_Name():
    while True:
        attend_call_cordinates=pyautogui.locateCenterOnScreen('img\call_attend.png', confidence=0.7)
        if attend_call_cordinates!=None:
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Reinstall Tesseract-OCR in this location 'C:\Program Files\Tesseract-OCR'
            cap = ImageGrab.grab(bbox =(1630, 85, 1910, 130))
            ocr = pytesseract.image_to_string(cap, lang ='eng')
            print('Caller Name : ',ocr)
            return ocr
        else:
            print('No incoming call....')
            sleep(1)

# attend call
def attend_call():
    global attend_call_cordinates
    attend_call_cordinates=jarvis.locateCenterOnScreen('img\call_attend.png', confidence=0.7)
    if attend_call_cordinates!=None:
        print('Attending Call....',attend_call_cordinates)
        x=attend_call_cordinates[0]
        y=attend_call_cordinates[1]
        jarvis.click(x, y)
        jarvis.sleep(1.5)
    else:
        print('Can not find call_attend button...')

# decline call
def decline_call():
    global decline_call_cordinates
    decline_call_cordinates=jarvis.locateCenterOnScreen('img\call_decline.png', confidence=0.7)
    if decline_call_cordinates!=None:
        print('Declining Call....',decline_call_cordinates)
        x=decline_call_cordinates[0]
        y=decline_call_cordinates[1]
        jarvis.click(x, y)
        jarvis.sleep(1)
    else:
        print('Can not find decline_attend button...')

# cut call
def cut_call():
    global cut_call_cordinates
    cut_call_cordinates=jarvis.locateCenterOnScreen('img\call_cut.png', confidence=0.7)
    if cut_call_cordinates!=None:
        print('Cutting Call....',cut_call_cordinates)
        x=cut_call_cordinates[0]
        y=cut_call_cordinates[1]
        jarvis.click(x, y)
        jarvis.sleep(1)

# check if the call is in progress
def check_call():
    global call_in_progress
    call_in_progress=jarvis.locateCenterOnScreen('img\call_in_progress.png', confidence=0.7)
    if call_in_progress!=None:
        print('Call in progress........')
        return True
    else:
        print('No call in progress........')
        return False

# check incoming call
def check_incoming_call():
    attend_call_cordinates=jarvis.locateCenterOnScreen('img\call_attend.png', confidence=0.7)
    if attend_call_cordinates!=None:
        return True
    else:
        print('No incoming call....')
        return False

# main function
def main():
    while True:
        if check_incoming_call() == True:

            user = Caller_Name()    # get the caller name
            attend_call()        # attend the call
            
            if attend_call_cordinates!=None:
                jarvis_speak('Hello ' + user + 'I am jarvis, AI bot. How can I help you?')
                while True:
                    print('Call Attended........')

                    user_said = jarvis_voice_recognise()    # get the user input
                    print('User said : ',user_said)

                    reply = reply_engine.Reply_Engine(msg_input = user_said)   # get the reply
                    jarvis_speak(reply)

                    print('user has been answered........')
                    print('reply to user :',reply)

                    if reply == 'Good Bye Sir have a nice day':
                        cut_call()
                        break

# call main function
main()

'''
FUTURE WORKS:
    1. add a virtual microphone to the program
    2. integrate with main jarvis program
'''