import pygame, sys, random
import time

def animate():
    pygame.display.flip()

Black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode([640,640])
font = pygame.font.Font(None, 50)

while True:
    animate()
    end_text = font.render("Thanks for playing.",0 , (255, 0, 0))
    screen.blit(end_text,[150,320])
    pygame.display.flip()
    

    time.sleep(2)
    pygame.quit()
