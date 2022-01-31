import speech_recognition 
import pyttsx3
import Threads
# Initialising modules....
jarvis_ear = speech_recognition.Recognizer()
jarvis_mouth = pyttsx3.init()

# Chinging voice....
voices = jarvis_mouth.getProperty('voices')
jarvis_mouth.setProperty('voice', voices[1].id)

# Jarvis Text to speech
def jarvis_speak(text):
    print("Jarvis: " + text)
    jarvis_mouth.say(text)
    jarvis_mouth.runAndWait()

# Jarvis Speech to text
def jarvis_listen():
    try:
        with speech_recognition.Microphone() as mic:
            print("Jarvis: I'm Listening Sir")
            audio = jarvis_ear.listen(mic,timeout=6 )
            
        you = jarvis_ear.recognize_google(audio)  
        you = you.lower()
        if "jarvis" in you:
            you = you.replace("jarvis", "")
    except:
        you = "Cannot Recognize......"
        pass

    return you

def main():
    you = jarvis_listen()
    print("Boss: " + you) 
    
    if "hello" or 'wake up' in you:
        return 'hello'

    elif "bye"  or 'goodbye' or 'you need a break' or 'shutdown' in you :
        return 'Bye Sir, but you can call me anytime.....'
        
    elif 'whatsapp' in you:
        Threads.Whatsapp()
    else:
        return 'Sir You have not programmed any such function in me....'

while True:
    jarvis_speak(main())
    if main()=='Bye Sir, but you can call me anytime.....':
        break