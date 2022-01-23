def jarvis_voice_recognition1():
    import speech_recognition as jarvis_voice_recognition
    import pyaudio
    speech = jarvis_voice_recognition.Recognizer()
    with jarvis_voice_recognition.Microphone() as source:
        speech.adjust_for_ambient_noise(source, duration=0.2)       # Adjust for ambient noises
        print("Listening Sir..............")
        audio = speech.listen(source, timeout=2, phrase_time_limit=3)
        global text
        text_dict_old = speech.recognize_google(audio,  language='en-US', show_all=True)

        list_check = isinstance(text_dict_old, list)
        if list_check == True:
            text_dict_old = {'alternative': [{'transcript': 'Could Not Understand.... Can You please Repeat it ', 'confidence': 0.92995489}, {'transcript': 'helo'}, {'transcript': 'hallo'}, {'transcript': 'yellow'}, {'transcript': 'hello I'}], 'final': True}
            print('in if loop')
        print(text_dict_old)
        x = list(text_dict_old.values())
        # print(type(x))
        text = list(x[0][0].values())[0]
        print("You said : {}".format(text))
        return text

def jarvis_voice_recognition():
    import speech_recognition as jarvis_voice_recognition
    import pyaudio
    speech = jarvis_voice_recognition.Recognizer()
    with jarvis_voice_recognition.Microphone() as source:
        try:
            speech.adjust_for_ambient_noise(source, duration=0.2)       # Adjust for ambient noises
            print("Listening Sir..............")
            #speech.pause_threshold
            audio = speech.listen(source, timeout=2, phrase_time_limit=2)
            global text
            text_dict_old = speech.recognize_google(audio,  language='en-US', show_all=True)
            x = list(text_dict_old.values())
            text = list(x[0][0].values())[0]
            return "You said : {}".format(text)
        except:
            return 'Could Not Understand.... Can You please Repeat it'

def Check_Microphone():
    import speech_recognition as sr
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def jarvis_speak(my_text):
    from gtts import gTTS
    import os
    from playsound import playsound
    
    '''
    # Using gTTs
    language='en'
    output=gTTS(text=my_text,lang=language,slow=False)
    output.save('output.mp3')
    playsound('output.mp3')
    os.system('start output.mp3')
    os.remove('output.mp3')
    '''

    # Using pyttsx3
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    newVoiceRate = 135
    engine.setProperty('rate',newVoiceRate)
    #newVolume = 1.0
    #engine.setProperty('volume', newVolume)
    engine.say(my_text)
    #engine.save_to_file(my_text,'output.mp3')
    engine.runAndWait()

# Main Body

while True:
    print(jarvis_voice_recognition())
    st = jarvis_voice_recognition().replace(' ','').lower()
    print(st)
    if 'friday' in st:
        print('hello')
        jarvis_speak('Good Evening Boss')