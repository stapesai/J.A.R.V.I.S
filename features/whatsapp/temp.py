import sounddevice

devs = sounddevice.query_devices()
print(devs) # Shows current output and input as well with "<" abd ">" tokens
    
for dev in devs:
    print(dev['name'])

import pygame

pygame.mixer.init(devicename='Hi-Fi Cable Input (VB-Audio Hi-Fi Cable)')
