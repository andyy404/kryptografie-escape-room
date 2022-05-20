# IMPORTS ----------------------------------------------------------------
import pygame, random
from pygame.locals import *

# SETUP ------------------------------------------------------------------
pygame.init()

screen = pygame.display.set_mode((0,0), FULLSCREEN)
pygame.display.set_icon(pygame.image.load(r'assets\icon.png'))
pygame.display.set_caption('Kryptografie Escape Room')

clock = pygame.time.Clock()

w, h = screen.get_size()

uv_light_icon = pygame.transform.scale(pygame.image.load(r'assets\light.png'), (int(w/27*2), int(w/27*2)))

# COLORS -----------------------------------------------------------------
black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)

uv_color = (127, 0, 255)
uv_color_light = (191, 127, 255)
uv_color_dark = (63, 0, 127)
neon_color = (127, 255, 0)

dark_theme = [black, white]
light_theme = [white, black]

color_theme = light_theme

# BUTTONS ----------------------------------------------------------------
button_right = pygame.Rect(w/27*26, h/4, w/27, h/2)
button_left = pygame.Rect(0, h/4, w/27, h/2)
button_menu_play = pygame.Rect(w/2-w/8, h/27*17, w/4, h/27*4)
button_menu_quit = pygame.Rect(w-h/27*4, h-h/27*4, h/27*3, h/27*3)
button_menu_info = pygame.Rect(h/27, h-h/27*4, h/27*3, h/27*3)
button_uv_light = pygame.Rect(w-w/27*3-w/27, h-h/27*3-w/27, w/27*2, w/27*2)

# GAME VARIABLES ---------------------------------------------------------
uv_light = 2 # 0 -> do not have it; 1 -> have it but it's off; 2 -> have it and it's  on
room1_code = random.randint(10000, 99999)
in_menu = False
running = True
looking_at_wall = 0

room1 = [
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[1], 0],
    [pygame.Rect(w/9, h/9, w/9, h/9), color_theme[1], 0],
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[1], 1],
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[1], 2],
    [pygame.Rect(w/3, h/3, w/3, h/3), color_theme[1], 3]
    ]

def render_hud():
    mx, my = pygame.mouse.get_pos()

    # SIDE BUTTONS
    pygame.draw.rect(screen, color_theme[0], button_right)
    pygame.draw.rect(screen, color_theme[0], button_left)

    if button_right.collidepoint(mx, my):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, color_theme[1], button_right)
        else:
            pygame.draw.rect(screen, gray, button_right)

    if button_left.collidepoint(mx, my):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, color_theme[1], button_left)
        else:
            pygame.draw.rect(screen, gray, button_left)
    
    pygame.draw.rect(screen, color_theme[1], button_right, 2)
    pygame.draw.rect(screen, color_theme[1], button_left, 2)

    # UV LIGHT BUTTON
    if uv_light == 2:
        pygame.draw.circle(screen, uv_color, (w-w/27*3, h-h/27*3), w/27)
    elif uv_light == 1:
        pygame.draw.circle(screen, color_theme[0], (w-w/27*3, h-h/27*3), w/27)

    if uv_light > 0:
        if button_uv_light.collidepoint(mx, my):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.circle(screen, uv_color, (w-w/27*3, h-h/27*3), w/27)

            screen.blit(uv_light_icon, (w-w/27*3-w/27, h-h/27*3-w/27))



def menu():
    pass # TODO

while running:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = not running
    
    mx, my = pygame.mouse.get_pos()

    screen.fill(black)
    
    if in_menu:
        menu()
    if not in_menu:
        render_hud()

    pygame.display.flip()

pygame.quit()