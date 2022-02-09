import time
import speech_recognition as sr
import winsound as ws   # for background sound

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
def jarvis_voice_recognise():
    with sr.Microphone(device_index=None) as source:

        speech.adjust_for_ambient_noise(source, duration=0.5)       # Adjust for ambient noises
        print("Listening........")
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
    engine.say(text)
    engine.runAndWait()


def main():
    ws.PlaySound('music\IronMan_Theme_Song.mp3')
    jarvis_speak('welcome back sir , all systems are online')

main()