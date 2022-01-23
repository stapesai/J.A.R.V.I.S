''' 
Dependencies....      
1. pip install SpeechRecognition
2. pip install pyaudio
'''

def jarvis_voice_recognition():
    import speech_recognition as jarvis_voice_recognition
    import pyaudio
    speech = jarvis_voice_recognition.Recognizer()
    with jarvis_voice_recognition.Microphone() as source:
        #speech.adjust_for_ambient_noise(source, duration=0.2)       # Adjust for ambient noises
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

#jarvis_voice_recognition()
#Check_Microphone()