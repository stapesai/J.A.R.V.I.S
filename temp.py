<<<<<<< Updated upstream
import speech_recognition as sr
speech = sr.Recognizer()
def jarvis_voice_recognise(tout=None, ptlimit=None):
    with sr.Microphone(device_index=1) as source:

        speech.adjust_for_ambient_noise(source, duration=0.5)       # Adjust for ambient noises
        print("Listening........")
        audio = speech.listen(source, timeout=2, phrase_time_limit=10)     #phrase_time_limit=ptlimit to 5 sec ,timeout=tout to 3 sec)

        try:
            text = speech.recognize_google(audio, language='en-US').lower()
            print("You said : {}".format(text))
            return text

        except:
            print("Could not understand what you said")
            return "Could not understand what you said".lower()


jarvis_voice_recognise()

# import speech_recognition as sr
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
=======
import lsHotword.ls as hotword
import os
while True:
    print('Listening........')
    hotword.lsHotword_loop()
    print('i got u')
>>>>>>> Stashed changes
