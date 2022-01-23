def jarvis_speak(my_text):
    from gtts import gTTS
    import os
    from playsound import playsound
    
    # USing gTTs
    #language='en'
    #output=gTTS(text=my_text,lang=language,slow=False)
    #output.save('output.mp3')
    #playsound('output.mp3')

    # Using pyttsx3
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    newVoiceRate = 135
    engine.setProperty('rate',newVoiceRate)
    #newVolume = 1.0
    #engine.setProperty('volume', newVolume)
    engine.say(my_text)
    #engine.save_to_file(my_text,'output.mp3')
    engine.runAndWait()

    # Common Steps...
    #os.system('start output.mp3')
    #os.remove('output.mp3')
    
#jarvis_speak('Swastik Tablet')