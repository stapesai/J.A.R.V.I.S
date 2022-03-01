import struct
import pyaudio
import pvporcupine
import playsound

porcupine=None
paud=None
audio_stream=None

print('All keywords:', pvporcupine.KEYWORDS)
# C:\Users\swast\AppData\Local\Programs\Python\Python310\Lib\site-packages\pvporcupine

def wake_word_detection(model, music_file = 'chime.wav'):
    try:
        porcupine=pvporcupine.create(
            access_key='+m4ClCWe3QUlLBiYi9bIgjdboyQWIqDdnCkN3gUAnCDuJHF2L9ez8g==',
            keyword_paths=model
            ) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                print("hotword detected")
                # play sound
                playsound.playsound(music_file)    # pip install playsound==1.2.2
                break
                
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

if __name__ == '__main__':
    while True:
        wake_word_detection()