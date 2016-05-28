'''
import winsound, sys

def beep(sound):
    winsound.PlaySound('%s.mp3' % sound, winsound.SND_FILENAME)

if __name__ == '__main__':
    beep(sys.argv[1])

'''

'''
import os
os.system("start C:\Users\User\James.mp3")
'''
'''
import pygame

import time

file = "stay.mp3"
pygame.init()

pygame.mixer.music.load(file)

pygame.mixer.music.play(0, 0.0)
print ('began')
time.sleep(10)
print ('ended')
'''
#!/usr/bin/env python
import pygame
from Tkinter import *
import time
def playmusic(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
##while pygame.mixer.music.get_busy():
##    pygame.time.Clock().tick(10)
#pygame.event.wait()

def main():
  
    root = Tk()
    file = 'stay.mp3'
    playmusic(file)
    root.mainloop()  


if __name__ == '__main__':
    main()
