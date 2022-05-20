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
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
purble = (255, 0, 255)

def main_menu():
    play_button = pygame.Rect(w/2-w/8, h/27*17, w/4, h/27*4)

    info_button = pygame.Rect(h/27, h-h/27*4, h/27*3, h/27*3)
    quit_button = pygame.Rect(w-h/27*4, h-h/27*4, h/27*3, h/27*3)

    titel = pygame.image.load(r'assets\titel.png')
    info_icon = pygame.image.load(r'assets\info.png')
    door = pygame.image.load(r'assets\quit.png')
    start_text = pygame.image.load(r'assets\start.png')

    titel = pygame.transform.scale(titel, (int(w/8*6), int(w/8*6/2000*578)))
    info_icon = pygame.transform.scale(info_icon, (int(h/27*3), int(h/27*3)))
    door = pygame.transform.scale(door, (int(h/27*3), int(h/27*3)))
    
    start_text = pygame.transform.scale(start_text, (int(h/27*4/526*1159), int(h/27*4)))

    while True:
        mx, my = pygame.mouse.get_pos()

        screen.fill(black)

        if play_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, gray, play_button)

        if info_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, gray, info_button)
        
        if quit_button.collidepoint((mx, my)):
            pygame.draw.rect(screen, gray, quit_button)

        pygame.draw.rect(screen, white, play_button, 2)
        pygame.draw.rect(screen, white, info_button, 2)
        pygame.draw.rect(screen, white, quit_button, 2)

        screen.blit(titel, (w/8, h/27*2))
        screen.blit(info_icon, (h/27, h-h/27*4))
        screen.blit(door, (w-h/27*4, h-h/27*4))
        screen.blit(start_text, (w/2-h/27*4/526*1159/2, h/27*19-h/27*4/2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and play_button.collidepoint((mx, my)):
                room1()
            if event.type == pygame.MOUSEBUTTONDOWN and info_button.collidepoint((mx, my)):
                info()
            if event.type == pygame.MOUSEBUTTONDOWN and quit_button.collidepoint((mx, my)):
                pygame.quit()
                sys.exit()
        
        clock.tick(60)

def room1():
    offset = w*3
    rotating = False

    left_button = pygame.Rect(0, int(h/3), int(w/16), int(h/3))
    right_button = pygame.Rect(int(w/16*15), int(h/3), int(w/16), int(h/3))

    standard_height = h/6*4

    while True:
        mx, my = pygame.mouse.get_pos()

        screen.fill(black)

        room_corners = [pygame.Rect(int(-w/8*23+offset), int(h/6), 1, int(h/6*4)),
                    pygame.Rect(int(-w/8*17+offset), int(h/6), 1, int(h/6*4)),
                    pygame.Rect(int(-w/8*11+offset), int(h/6), 1, int(h/6*4)),
                    pygame.Rect(int(-w/8*5+offset), int(h/6), 1, int(h/6*4)),
                    pygame.Rect(int(w/8+offset), int(h/6), 1, int(h/6*4)),
                    pygame.Rect(int(w/8*7+offset), int(h/6), 1, int(h/6*4))]

        onscreen_line = pygame.Rect(0, int(h/2), w, 1)

        onscreen_corners = []

        for corner in room_corners:
            if corner.colliderect(onscreen_line):
                pygame.draw.rect(screen, white, corner)
                onscreen_corners.append(corner)

        if len(onscreen_corners) == 1:
            pygame.draw.lines(screen, white, False, ((0,0), (onscreen_corners[0].left, onscreen_corners[0].top), (w, 0)))
            pygame.draw.lines(screen, white, False, ((0,h), (onscreen_corners[0].left, onscreen_corners[0].bottom), (w, h)))

        if len(onscreen_corners) == 2:
            pygame.draw.lines(screen, white, False, ((0,0), (onscreen_corners[0].left, onscreen_corners[0].top), (onscreen_corners[1].left, onscreen_corners[1].top), (w, 0)))
            pygame.draw.lines(screen, white, False, ((0,h), (onscreen_corners[0].left, onscreen_corners[0].bottom), (onscreen_corners[1].left, onscreen_corners[1].bottom), (w, h)))

        pygame.draw.rect(screen, black, left_button)
        pygame.draw.rect(screen, black, right_button)

        if left_button.collidepoint(mx, my):
            pygame.draw.rect(screen, gray, left_button)
            if rotating:
                pygame.draw.rect(screen, white, left_button)
                offset += 10
                if offset >= w*3:
                    offset = offset - w*3

        if right_button.collidepoint(mx, my):
            pygame.draw.rect(screen, gray, right_button)
            if rotating:
                pygame.draw.rect(screen, white, right_button)
                offset -= 10
                if offset <= 0:
                    offset = w*3 - offset

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if left_button.collidepoint(mx, my) or right_button.collidepoint(mx, my):
                    rotating = True

            if event.type == MOUSEBUTTONUP and rotating:
                rotating = not rotating

        pygame.draw.rect(screen, white, left_button, 2)
        pygame.draw.rect(screen, white, right_button, 2)            

        pygame.display.flip()
        
        clock.tick(60)

def ciphers():
    pass

def info():
    pass

main_menu()