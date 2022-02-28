# initialize the engine
import pyttsx3
engine = pyttsx3.init()     # initialise the engine

voices = engine.getProperty('voices')   
engine.setProperty('voice', voices[1].id)   # set the voice

newVoiceRate = 140
engine.setProperty('rate',newVoiceRate)    # set the speed rate

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
                r.adjust_for_ambient_noise(source2, duration=0.2)
                #listens for the user's input 
                try:
                    print("Listening........")
                    audio2 = r.listen(source2, phrase_time_limit=5)
                    # Using google to recognize audio
                    print('Recognizing........')
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
            engine.say('Yes sir')
            engine.runAndWait()
            print('Jarvis : Yes sir')

live_speech_to_text()