# 2 channel to 5 channel converter

def play_in_5_channels(file_name):
    import pyaudio
    import wave
    import numpy as np
    import time
    import sys
    import os

    # Open the file
    wf = wave.open(file_name, 'rb')

    # Read the file
    data = wf.readframes(1024)

    # Create the audio object
    p = pyaudio.PyAudio()

    # Open the stream
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    # Play the file
    while data != b'':
        stream.write(data)
        data = wf.readframes(1024)

    # Close the stream
    stream.stop_stream()
    stream.close()

    # Close the file
    wf.close()

    # Close the audio object
    p.terminate()


play_in_5_channels('filename.wav')