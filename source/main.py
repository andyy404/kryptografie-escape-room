import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((0,0), FULLSCREEN)
pygame.display.set_icon(pygame.image.load(r'assets\icon.png'))
pygame.display.set_caption('Kryptografie Escape Room')

clock = pygame.time.Clock()

w, h = screen.get_size()

black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)

red = (255, 127, 127)
#yellow = (255, 255, 127)
#green = (127, 255, 127)
#cyan = (127, 255, 255)
#blue = (127, 127, 255)
purble = (255, 127, 255)

def exit():
    pygame.quit()
    sys.exit()

def render_frame():
    pass