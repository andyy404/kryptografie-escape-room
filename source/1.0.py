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
    left_button = pygame.Rect(0, int(h/3), int(w/24), int(h/3))
    right_button = pygame.Rect(int(w/24*23), int(h/3), int(w/24), int(h/3))

    door1 = 0

    def wall_n():
        #room
        pygame.draw.rect(screen, white, (int(w/5), int(h/5), int(w/5*3), int(h/5*3)), 1)

        pygame.draw.line(screen, white, (0, 0), (int(w/5), int(h/5)))
        pygame.draw.line(screen, white, (w, 0), (int(w/5*4), int(h/5)))
        pygame.draw.line(screen, white, (0, h), (int(w/5), int(h/5*4)))
        pygame.draw.line(screen, white, (w, h), (int(w/5*4), int(h/5*4)))

        pygame.draw.rect(screen, white, (int(w/7*3), int(h/5*2), int(w/7), int(h/5*2)), 1)
        pygame.draw.rect(screen, red, (int(w/48*28), int(h/20*9), int(w/25), int(w/25)), 1)
        pygame.draw.rect(screen, red, (int(w/48*28+w/75), int(h/20*9), int(w/75), int(w/75*4)), 1)
        pygame.draw.rect(screen, red, (int(w/48*28), int(h/20*9+w/75), int(w/75*3), int(w/75)), 1)

        if door1 == 0:
            pygame.draw.ellipse(screen, white, (int(w/48*26), int(h/20*11), int(w/75), int(h/30)), 1)
            pygame.draw.rect(screen, white, (int(w/48*26), int(h/30*17), int(w/75), int(h/60)))


    def wall_w():
        pygame.draw.rect(screen, white, (int(w/5), int(h/5), int(w/5*3), int(h/5*3)), 1)

        pygame.draw.line(screen, white, (0, 0), (int(w/5), int(h/5)))
        pygame.draw.line(screen, white, (w, 0), (int(w/5*4), int(h/5)))
        pygame.draw.line(screen, white, (0, h), (int(w/5), int(h/5*4)))
        pygame.draw.line(screen, white, (w, h), (int(w/5*4), int(h/5*4)))


    while True:
        mx, my = pygame.mouse.get_pos()

        screen.fill(black)

        pygame.draw.rect(screen, black, left_button)
        pygame.draw.rect(screen, black, right_button)

        if left_button.collidepoint(mx, my):
            pygame.draw.rect(screen, gray, left_button)

        if right_button.collidepoint(mx, my):
            pygame.draw.rect(screen, gray, right_button)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if left_button.collidepoint(mx, my):
                    pass
                if right_button.collidepoint(mx, my):
                    pass
        
        wall_n()

        pygame.draw.rect(screen, white, left_button, 2)
        pygame.draw.rect(screen, white, right_button, 2)            

        pygame.display.flip()
        
        clock.tick(60)

def ciphers():
    pass

def info():
    pass

main_menu()