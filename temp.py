def jarvis_voice_recognise():
    import speech_recognition as sr
    speech = sr.Recognizer()

    with sr.Microphone(device_index=2) as source:

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
while True:
    jarvis_voice_recognise()
