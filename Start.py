x = 300
y = 55
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
import sys
import pygame
import time
from Game.GameStructure1 import GameMain

class StartUp:
    def __init__(self):
        self.screenSize = (640, 640)

    def showStartScreen(self):
        self.screen = pygame.display.set_mode(self.screenSize)

    def run(self):
        while True:
            Play = GameMain()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            time.sleep(2.6)
            Play.New()
            
            
            

    def init(self):
        pygame.init()
        pygame.display.set_caption("The Challenge!")
        startmusic = pygame.mixer.Sound('musicS.ogg')
        startmusic.play()

    def finish(self):
        pygame.quit()

    def New(self):
        self.init()
        self.showStartScreen()
        self.run()
        self.finish()

setUp = StartUp()

setUp.New()
            
            
        

