def live_speech_to_text():
    import speech_recognition as sr

    # Initialize the recognizer 
    r = sr.Recognizer() 
    # Loop infinitely for user to speak
    while True:    
        # Exception handling to handle
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer to adjust the energy threshold based on the surrounding noise level 
                #this is the edited line test by codemasterayush
                r.adjust_for_ambient_noise(source2, duration=0.2)
                #listens for the user's input 
                try:
                    audio2 = r.listen(source2, timeout=None, phrase_time_limit=1)
                    # Using google to recognize audio
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    print("Did you say "+MyText)
                except:
                    MyText = 'Not recognized'
                    print('Not recognized')

                #audio2 = r.listen(source2, timeout=3)

                

        # exceptions at the runtime          
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured")

        # Wake Word
        if 'jarvis' in MyText:
            return MyText
            #break

        
#live_speech_to_text()
