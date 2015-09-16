import pygame


class BClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("startbutton.png")
        self.rect = self.image.get_rect()
        self.rect.center = [310, 500]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2: self.angle = -9
        if self.angle >  2: self.angle =  9
        center = self.rect.center
        self.image = pygame.image.load("startbutton.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 70 - abs(self.angle) * 2]
        return speed 

    def move(self, speed):
        self.rect.centery = self.rect.centery + speed[0]
        if self.rect.centery < -49:
            self.rect.centery = -53
        if self.rect.centery > 499:
            self.rect.centery = 500

class BKClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("start.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320,320]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2: self.angle = -9
        if self.angle >  2: self.angle =  9
        center = self.rect.center
        self.image = pygame.image.load("startbutton.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 70 - abs(self.angle) * 2]
        return speed 

    def move(self, speed):
        self.rect.centerx = self.rect.centerx + speed[0]
        if self.rect.centerx < 320: self.rect.centerx = 320
        if self.rect.centerx > 935:
            self.rect.centerx = 935

class BarClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Bar.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 500]
        self.angle = 0

    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2: self.angle = -9
        if self.angle >  2: self.angle =  9
        center = self.rect.center
        self.image = pygame.image.load("startbutton.png")
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 70 - abs(self.angle) * 2]
        return speed 

    def move(self, speed):
        self.rect.centery = self.rect.centery + speed[0]
        if self.rect.centery < -49: self.rect.centery = -53
        if self.rect.centery > 499:
            self.rect.centery = 500
		
class LabClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("lab.png")
        self.rect = self.image.get_rect()
    
class BlackClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("test.png")
        self.rect = self.image.get_rect()

class keyClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("clear.png")
        self.rect = self.image.get_rect()
        self.rect.center = [550,450]






