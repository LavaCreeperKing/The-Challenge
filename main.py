

import pygame
import prepare

class Game:
    def __init__(self):
        self.bg = prepare.GFX['lab']
        self.bg_rect = self.bg.get_rect()
        self.btn_sound = prepare.SFX['ButtonSound']
        self.bg_music = pygame.mixer.music.load(prepare.MUSIC['musicC'])
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play()
        
    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.btn_sound.play()
            
    def render(self, screen):
        screen.blit(self.bg, self.bg_rect)
        

class Control:
    def __init__(self):
        pygame.display.set_caption(prepare.CAPTION)
        self.done = False
        self.screen = prepare.SCREEN
        self.game = Game()
        
    def main_loop(self):
        while not self.done:
            self.get_event()
            self.update()
            self.render()
            pygame.display.update()
            
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.game.get_event(event)
                
    def update(self):
        pass
        
    def render(self):
        self.game.render(self.screen)

app = Control()
app.main_loop()
