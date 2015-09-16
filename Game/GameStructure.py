import pygame, random
import time
from Game.Objects.objects import*


        
def animate():
    screen.blit(level_text,[10,10])
    screen.blit(Bg.image,Bg.rect)
    screen.blit(Bg2.image,Bg2.rect)
    screen.blit(Bar.image,Bar.rect)
    screen.blit(B.image,B.rect)
    pygame.display.flip()

def animate2():
    screen.blit(Bg.image,Bg.rect)
    screen.blit(Key.image,Key.rect)
    screen.blit(level_text,[10,10])
    pygame.display.flip()


    
pygame.init()
screen = pygame.display.set_mode([640,640])
B = BClass()
Bar = BarClass()
speed = [0, 30]
Level = 1
correct = 0
font = pygame.font.Font(None, 20)
fon2t = pygame.font.Font(None, 50)
bg2move = False
Bg2 = BKClass()
Bg = LabClass()
Key = keyClass()
black = BlackClass()
ButtonSound = pygame.mixer.Sound('ButtonSound.ogg')
startmusic = pygame.mixer.Sound('musicS.ogg')
music2 = pygame.mixer.Sound('play.ogg')
time_animate = pygame.time.get_ticks()
time_animate2 = pygame.time.get_ticks()
time_now = pygame.time.get_ticks()
running1 = True
running2 = True
screen2 = False
screen1 = True
remove = True
remove2 = True
choose = True
living = True
key1 = True
key2 = True

while True:
    level_text = font.render("Level: " +str(Level), 1, (0, 0, 0))
    correct_text = font.render("Level: " +str(Level), 1, (0, 0, 0))
    while not running2:
        animate()
        speed = B.turn(-9)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
        now = pygame.time.get_ticks()
        if now-time_animate > 2500:
            pygame.mixer.music.play(-1,0.0)
            running2 = True
            running1 = False
        Bg2.move(speed)
        now2 = pygame.time.get_ticks()
        time_animate2 = now2

    while not running1:
        animate()
        speed = B.turn(9)
        B.move(speed)
        Bar.move(speed)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
        now2 = pygame.time.get_ticks()
        if now2-time_animate2 > 2400:
            running1 = True
            screen2 = False
                    
    while not screen2:
        animate()
        x, y = pygame.mouse.get_pos()
        if (x in range(229,391)) and (y in range(470,530)):
            B.image = pygame.image.load("MouseOn.png")
        else:
            B.image = pygame.image.load("startbutton.png")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ( x in range(229,391)) and (y in range(470,530)):
                    B.image = pygame.image.load("push.png")
                    pygame.mixer.music.stop()
                    ButtonSound.play()
                    animate()
                    speed = B.turn(9)
                    screen2 = True
                    remove2 = False
        now = pygame.time.get_ticks()
        time_animate = now
                    
    while not remove2:
        animate()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
        Bg2.move(speed)
        now = pygame.time.get_ticks()
        if now-time_animate > 2300:
            remove2 = True
            now2 = pygame.time.get_ticks()
            time_animate2 = now
            remove = False
            
    while not remove:
        animate()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
        speed = B.turn(-9)
        Bar.move(speed)
        B.move(speed)
        now2 = pygame.time.get_ticks()
        if now2-time_animate2 > 2100:
            remove = True
            screen1 = False
        
    while not screen1:
        music2.play(-1)
        animate2()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
        choose = False
        screen1 = True

    while not living:
        music2.stop()
        Level = 1
        animate2()
        Key.image = pygame.image.load("clear.png")
        Bg.image = pygame.image.load("shock.png")
        animate2()
        time.sleep(1)
        Bg.image = pygame.image.load("lab.png")
        living = True
        now = pygame.time.get_ticks()
        time_animate = now
        startmusic.play()
        running2 = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.mixer.music.stop()
                        import Game.end.py
        
    while not choose:
        time.sleep(1)
        now3 = pygame.time.get_ticks()
        time_now = now3
        type = random.choice(["M1", "M2", "KA", "KE", "KH", "KJ", "KN", "KW"])
        if type=="M1":
            Key.image = pygame.image.load("key1.png")
            choose = True
            key1 = False
        if type=="M2":
            Key.image = pygame.image.load("key2.png")
            choose = True
            key2 = False
        if type=="KA":
            Key.image = pygame.image.load("KA.png")
            choose = True
            key1 = False
        if type=="KE":
            Key.image = pygame.image.load("KE.png")
            choose = True
            key1 = False
        if type=="KH":
            Key.image = pygame.image.load("KH.png")
            choose = True
            key1 = False
        if type=="KJ":
            Key.image = pygame.image.load("KJ.png")
            choose = True
            key1 = False
        if type=="KN":
            Key.image = pygame.image.load("KN.png")
            choose = True
            key1 = False
        if type=="KW":
            Key.image = pygame.image.load("KW.png")
            choose = True
            key1 = False

    while not key1:
        animate2()
        now3 = pygame.time.get_ticks()
        if now3-time_now > 2000:
            key1 = True
            living = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Game.end.py
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
                else:
                    key1 = True
                    living = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Key.image = pygame.image.load("Clear.png")
                    Level = Level + 1
                    animate2()
                    key1 = True
                    choose = False
                else:
                    key1 = True
                    living = False

    while not key2:
        animate2()
        now3 = pygame.time.get_ticks()
        if now3-time_now > 2000:
            key2 = True
            living = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Game.end.py
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    import Game.end.py
                else:
                    key2 = True
                    living = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    Key.image = pygame.image.load("Clear.png")
                    Level = Level + 1
                    animate2()
                    key2 = True
                    choose = False
                else:
                    key2 = True
                    living = False
        
            
        
        
