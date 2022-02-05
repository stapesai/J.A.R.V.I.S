#!/usr/bin/env python3
# Path: temp.py
import pygame
pygame.mixer.init(frequency=44000, size=-16,channels=2, buffer=4096)
m = pygame.mixer.Sound('song.mp3')
channel = m.play()
channel.set_volume(1.0, 0.0)
print(channel.get_busy())
while channel.get_busy():
    pygame.time.delay(10)
pygame.quit()