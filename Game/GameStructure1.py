import pygame, random
import time
from Game.Objects.objects import*

class GameMain:
    def __init__(self):
        self.screenSize = (640, 640)

    def init(self):
        pygame.init()
        self.Bg = LabClass()
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.mixer.music.load('musicC.ogg')
        pygame.mixer.music.play(-1,0.0)

    def animate(self):
        self.screen.blit(self.Bg.image,self.Bg.rect)
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def New(self):
        self.init()
        self.animate()
        self.run()

