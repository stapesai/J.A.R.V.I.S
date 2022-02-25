import pygame
import time
time.sleep(1)
pygame.mixer.init()
pygame.mixer.music.load('output.wav')
pygame.mixer.music.play()
time.sleep(1)
print('Done')
time.sleep(1)