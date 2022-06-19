import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((960, 540))
pygame.display.set_icon(pygame.image.load(r'assets\icon.png'))
pygame.display.set_caption('Kryptografie Escape Room')

clock = pygame.time.Clock()

white = (32, 145, 79)

w, h = screen.get_size()
running = True

pygame.draw.rect(screen, white, (w/50*10, h/50*10, w/50*10*3, h/50*10*3), 2)

pygame.draw.line(screen, white, (0, 0), (w/50*10, h/50*10), 2)
pygame.draw.line(screen, white, (w, 0), (w/50*10*4,  h/50*10), 2)
pygame.draw.line(screen, white, (0, h), (w/50*10, h/50*10*4), 2)
pygame.draw.line(screen, white, (w, h), (w/50*10*4, h/50*10*4), 2)



pygame.display.flip()

while running:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = not running