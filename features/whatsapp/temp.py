import pygame._sdl2 as sdl2
import pygame
pygame.init()
is_capture = 0  # zero to request playback devices, non-zero to request recording devices
num = sdl2.get_num_audio_devices(is_capture)
names = [str(sdl2.get_audio_device_name(i, is_capture), encoding="utf-8") for i in range(num)]
print("\n".join(names))
pygame.quit()