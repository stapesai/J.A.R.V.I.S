import time
import speech_recognition as sr
# import winsound as ws 
from playsound import playsound  # for background sound

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
    with sr.Microphone(device_index=None) as source:

        speech.adjust_for_ambient_noise(source, duration=0.5)       # Adjust for ambient noises
        print("Listening........")
        audio = speech.listen(source, timeout=tout, phrase_time_limit=ptlimit)                # set timeout here

        try:
            text = speech.recognize_google(audio, language='en-US').lower()
            print("You said : {}".format(text))
            return text

        except:
            print("Could not understand what you said")
            return "Could not understand what you said".lower()

# just a function to check the microphone
def Check_Microphone():
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# text to speech
def jarvis_speak(text):
    print('Jarvis : ', text)
    engine.say(text)
    engine.runAndWait()

# background sound
def background_sound():
    import multiprocessing

    def play_sound():
        from playsound import playsound     # pip install playsound==1.2.2
        playsound('music\IronMan_Theme_Song.wav')
    if __name__ == '__main__':
        bgsound = multiprocessing.Process(target=play_sound)
        return bgsound



def main():
    background_sound.start()
    jarvis_speak('welcome back sir , all systems are online')
    background_sound.kill()

    while True:
        text = jarvis_voice_recognise()
        if 'jarvis' in text:
            jarvis_speak('Yes sir')

        elif 'hello' in text:
            jarvis_speak('Hello sir')

        elif 'how are you' in text:
            jarvis_speak('I am fine sir')

        elif 'what is your name' in text:
            jarvis_speak('My name is jarvis')

        elif 'what is your age' in text:
            jarvis_speak('My software is still in development mode')

        elif 'what is your job' in text:
            jarvis_speak('I am a virtual assistant')

        elif 'what is your favourite colour' in text:
            jarvis_speak('My favourite colour is blue')

        elif 'what is your favourite song' in text:
            jarvis_speak('My favourite song is Iron Man Songs')

        elif 'Could not understand what you said' in text:
            print('Could not understand what you said')


        # Features
        elif 'attend my call' or 'respond my call' in text:
            continue
        
        else:
            jarvis_speak('This is not programmed yet.')


main()