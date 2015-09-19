import pygame
import os
import tools

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '{},{}'.format(300,55)
CAPTION = 'The Challenge!'
SCREENSIZE = (800,640)
SCREEN = pygame.display.set_mode(SCREENSIZE)
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
SFX   = tools.load_all_sfx(os.path.join("resources", "sound"))
GFX   = tools.load_all_gfx(os.path.join("resources", "graphics"))
