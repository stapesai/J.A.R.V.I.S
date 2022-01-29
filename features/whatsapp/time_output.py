# function to convert the seconds into readable format
def time_sleep():
    from mutagen.mp3 import MP3
    audio = MP3('output.mp3')
    audio_info = audio.info
    length_in_secs = int(audio_info.length)
    return length_in_secs