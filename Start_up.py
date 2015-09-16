x = 300
y = 55
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame
pygame.init()
screen = pygame.display.set_mode((100,100))
import time



pygame.init()
pygame.display.set_caption("The Challenge!")
screen = pygame.display.set_mode([640,640])
startmusic = pygame.mixer.Sound('musicS.ogg')
pygame.mixer.music.load('musicC.ogg')
startmusic.play()
time.sleep(2.6)
startmusic.stop()
pygame.mixer.music.play(-1,0.0)

while True:
    import Game.GameStructure
        
                
        
    
