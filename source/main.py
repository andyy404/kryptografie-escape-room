# IMPORTS ----------------------------------------------------------------
import pygame, random
from pygame.locals import *
import rooms

# SETUP ------------------------------------------------------------------
pygame.init()

screen = pygame.display.set_mode((0,0), FULLSCREEN)
pygame.display.set_icon(pygame.image.load(r'assets\icon.png'))
pygame.display.set_caption('Kryptografie Escape Room')

clock = pygame.time.Clock()

w, h = screen.get_size()

# LOAD IMAGES ------------------------------------------------------------
uv_light_icon = pygame.transform.scale(pygame.image.load(r'assets\light.png'), (int(w/27*2), int(w/27*2)))

titel = pygame.transform.scale(pygame.image.load(r'assets\titel.png'), (int(w/8*6), int(w/8*6/2000*578)))
info_icon = pygame.transform.scale(pygame.image.load(r'assets\info.png'), (int(h/27*3), int(h/27*3)))
door = pygame.transform.scale(pygame.image.load(r'assets\quit.png'), (int(h/27*3), int(h/27*3)))

start_text = pygame.transform.scale(pygame.image.load(r'assets\start.png'), (int(h/27*4/526*1159), int(h/27*4)))

# COLORS -----------------------------------------------------------------
black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)

uv_color = (127, 0, 255)
uv_color_light = (191, 127, 255)
uv_color_dark = (63, 0, 127)
neon_color = (127, 255, 0)


dark_theme = [black, gray, white, uv_color_dark]
light_theme = [white, gray, black, uv_color_light]

color_theme = dark_theme # color theme = [background, middle tone, main color, uv]

# BUTTONS ----------------------------------------------------------------
button_right = pygame.Rect(w/27*26, h/4, w/27, h/2)
button_left = pygame.Rect(0, h/4, w/27, h/2)
button_menu_play = pygame.Rect(w/2-w/8, h/27*17, w/4, h/27*4)
button_menu_quit = pygame.Rect(w-h/27*4, h-h/27*4, h/27*3, h/27*3)
button_menu_info = pygame.Rect(h/27, h-h/27*4, h/27*3, h/27*3)
button_uv_light = pygame.Rect(w-w/27*3-w/27, h-h/27*3-w/27, w/27*2, w/27*2)

# GAME VARIABLES ---------------------------------------------------------
uv_light = 1 # 0 -> do not have it; 1 -> have it but it's off; 2 -> have it and it's  on
room1_code = random.randint(10000, 99999)
scene = 0 # 0 -> main menu; -1 -> info screen; x -> in room number x
running = True
looking_at_wall = 0
room = None
mbdown = False
mdup = False

room1 = [
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[0], 0],
    [pygame.Rect(w/9, h/9, w/9, h/9), color_theme[0], 0],
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[0], 1],
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[0], 2],
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[0], 3]
    ]


def menu():
    global running, scene

    screen.fill(black)

    if button_menu_play.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_play)
    if button_menu_info.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_info)
    if button_menu_quit.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_quit)

    pygame.draw.rect(screen, white, button_menu_play, 2)
    pygame.draw.rect(screen, white, button_menu_info, 2)
    pygame.draw.rect(screen, white, button_menu_quit, 2)

    screen.blit(titel, (w/8, h/27*2))
    screen.blit(info_icon, (h/27, h-h/27*4))
    screen.blit(door, (w-h/27*4, h-h/27*4))
    screen.blit(start_text, (w/2-h/27*4/526*1159/2, h/27*19-h/27*4/2))
    
    if mbdown and button_menu_play.collidepoint((mx, my)):
        scene = 1
    if mbdown and button_menu_info.collidepoint((mx, my)):
        scene = -1
    if mbdown and button_menu_quit.collidepoint((mx, my)):
        running = not running

def info_screen():
    pass

def userinterface():
    global uv_light
    # SIDE BUTTONS
    pygame.draw.rect(screen, color_theme[0], button_right)
    pygame.draw.rect(screen, color_theme[0], button_left)

    if button_right.collidepoint(mx, my):
        if click:
            pygame.draw.rect(screen, color_theme[2], button_right)
        else:
            pygame.draw.rect(screen, color_theme[1], button_right)
        if mbdown:
            room.turn_right()

    if button_left.collidepoint(mx, my):
        if click:
            pygame.draw.rect(screen, color_theme[2], button_left)
        else:
            pygame.draw.rect(screen, color_theme[1], button_left)
        if mbdown:
            room.turn_left()
    
    pygame.draw.rect(screen, color_theme[2], button_right, 2)
    pygame.draw.rect(screen, color_theme[2], button_left, 2)

    # UV LIGHT BUTTON
    if button_uv_light.collidepoint(mx, my) and click:
        uv_light = 2
        pygame.draw.circle(screen, color_theme[3], (w-w/27*3, h-h/27*3), w/27)
    if uv_light > 0:
        screen.blit(uv_light_icon, (w-w/27*3-w/27, h-h/27*3-w/27))

while running:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = not running
        if ev.type == MOUSEBUTTONDOWN:  
            mbdown = True
        if ev.type == MOUSEBUTTONUP:
            mbup = True

    mx, my = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    screen.fill(color_theme[0])
    
    if scene > 0:
        #room.render()
        userinterface()
    if scene == 0:
        menu()
    if scene == -1:
        info_screen()

    mbdown, mbup = False, False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()