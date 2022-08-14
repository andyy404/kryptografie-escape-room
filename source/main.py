# kryptografie escape room
# programmiert von Medea Emch im Rahmen einer Maturaarbeit an der Kantonsschule Alpenquai Luzern im Jahr 2022


#! IMPORTS --------------------------------------------------------------------------------------------------------------------
import pygame
from pygame.locals import *
import rooms


#! SETUP ----------------------------------------------------------------------------------------------------------------------
pygame.init()

screen = pygame.display.set_mode((0,0), FULLSCREEN) # makes a window of the size of the current screen (0, 0) and makes it fullscreen
pygame.display.set_icon(pygame.image.load(r'assets\icon.png')) #changes the icon in the taskbar
pygame.display.set_caption('Kryptografie Escape Room') # changes the window name in the taskbar

clock = pygame.time.Clock() # makes it possible to force a certain frame rate (is mostly useful when in game movements are tied to frames, which isn't the case here)
fps = 60
w, h = screen.get_size() # gets the size of the window so the size of buttons and icons can be done accordingly
running = True # defines whether the main loop gets looped or not


#! LOAD IMAGES ----------------------------------------------------------------------------------------------------------------
uv_light_icon = pygame.transform.scale(pygame.image.load(r'assets\light.png'), (int(w/27*2), int(w/27*2))) # in game icon of the uv lamp

titel = pygame.transform.scale(pygame.image.load(r'assets\titel.png'), (int(w/8*6), int(w/8*6/2000*578))) # title in the main menu
info_icon = pygame.transform.scale(pygame.image.load(r'assets\info.png'), (int(h/27*3), int(h/27*3))) # info screen icon in the main menu
door = pygame.transform.scale(pygame.image.load(r'assets\quit.png'), (int(h/27*3), int(h/27*3))) # quit game icon in the main menu
start_text = pygame.transform.scale(pygame.image.load(r'assets\start.png'), (int(h/27*4/526*1159), int(h/27*4))) # start button text icon in the main menu

continue_text = pygame.transform.scale(pygame.image.load(r'assets\continue.png'), (int(h/27*3/578*1944), int(h/27*3)))
main_menu_text = pygame.transform.scale(pygame.image.load(r'assets\mainmenu.png'), (int(h/27*3/392*1848), int(h/27*3)))

continue_b_text = pygame.transform.scale(pygame.image.load(r'assets\continue_black.png'), (int(h/27*3/578*1944), int(h/27*3)))
main_menu_b_text = pygame.transform.scale(pygame.image.load(r'assets\mainmenu_black.png'), (int(h/27*3/392*1848), int(h/27*3)))
door_b = pygame.transform.scale(pygame.image.load(r'assets\quit_black.png'), (int(h/27*3), int(h/27*3)))


#! COLORS ---------------------------------------------------------------------------------------------------------------------
black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)

red = (255, 0, 0)

uv_color = (127, 0, 255)

dark_theme = [black, gray, white, uv_color] # color theme = [background color, middle tone, object color, uv light color, color of uv reactive paint under uv light]
light_theme = [white, gray, black, uv_color]

color_theme = light_theme # game switches between these color themes, depending whether the room's lamp is on or off (light theme -> on, dark theme -> off)


#! IMPORTANT RECTANGLES (left edge, upper edge, width, height) ----------------------------------------------------------------
button_right = pygame.Rect(w/27*26, h/4, w/27, h/2) # in game button to turn 90° right
button_left = pygame.Rect(0, h/4, w/27, h/2) # in game button to turn 90° left
button_uv_light = pygame.Rect(w-w/27*3-w/27, h-h/27*3-w/27, w/27*2, w/27*2) # in game flashlight icon

button_menu_play = pygame.Rect(w/2-w/8, h/27*17, w/4, h/27*4) # main menu button to start game
button_menu_quit = pygame.Rect(w-h/27*4, h-h/27*4, h/27*3, h/27*3) # main menu button to quit game
button_menu_info = pygame.Rect(h/27, h-h/27*4, h/27*3, h/27*3) # main menu button to get to the info screen

button_back = pygame.Rect(h/27, h/27, h/27*3, h/27*3) # the back button in the info screen and the pause menu (also the pause button in game)
timer_rect = pygame.Rect(w/2-h/27*3.5, h/27, h/27*7, h/27*3) # the rectangle around the in game timer

button_paused_continue = pygame.Rect(w/2-h/27*8, h/27*18, h/27*16, h/27*3)
button_paused_main_menu = pygame.Rect(w/2-h/27*8, h/27*22, h/27*16, h/27*3)

pause_icon_l = pygame.Rect(h/27/5*8, h/27/5*8, h/27/5*3, h/27/5*3*3)
pause_icon_r = pygame.Rect(h/27/5*14, h/27/5*8, h/27/5*3, h/27/5*3*3)


#! GAME CONSTANTS -------------------------------------------------------------------------------------------------------------
info_screen_text = [''] # the text shown on the info screen (every new list in the list is a new tab, every new item within that is a new line)
default_timer_time = 15*60*fps # calculated in frames (minutes times 60 times the amount of frames per second)

words_list = [
    "Diskussion", "Ausgang", "Bedeutung", "Kontext", "Autobahn", "Professor", "Argument", "Hausaufgaben", "Assistent", "Zeichnung", "Situation", "Fahrstuhl", "Spiegelung", "Wissenschaft", "Zugabe", "Organisation", "Eindruck", "Variation", "Anerkennung", "Interaktion"]

rooms_list = [rooms.Room1, rooms.Room2, rooms.Room3]


#! GAME VARIABLES -------------------------------------------------------------------------------------------------------------
uv_light = 1 # 0 -> do not have it; 1 -> have it but it's off; 2 -> have it and it's on
scene = 0 # 0 -> main menu; -1 -> info screen; x -> in room x of the game
looking_at_wall = 0 # which way you are facing (there is 4 walls, 0, 1, 2 & 3) you start looking at wall 0 and the door is always on wall 0
mbdown, mbup= False, False # these variables show whether there was a mouse button down or mouse button up event in the current frame (if a mouse button got clicked or released)

room = None # contaims the current room object

paused = False # whether the game is paused or not
timer_running = False # whether the timer is running or not
timer_time = default_timer_time # sets the current time to the default starting time


#! FUNCTIONS ------------------------------------------------------------------------------------------------------------------

def menu(): # shows the main menu screen
    global running, scene, paused

    screen.fill(black)

    if button_menu_play.collidepoint((mx, my)): # if the cursor is hovering over one of the buttons, it will light up gray
        pygame.draw.rect(screen, gray, button_menu_play)
    if button_menu_info.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_info)
    if button_menu_quit.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_quit)

    pygame.draw.rect(screen, white, button_menu_play, 2) # draws the outlines of all three buttons in white
    pygame.draw.rect(screen, white, button_menu_info, 2)
    pygame.draw.rect(screen, white, button_menu_quit, 2)

    screen.blit(titel, (w/8, h/27*2)) # draws all the icons and button texts
    screen.blit(info_icon, (h/27, h-h/27*4))
    screen.blit(door, (w-h/27*4, h-h/27*4))
    screen.blit(start_text, (w/2-h/27*4/526*1159/2, h/27*19-h/27*4/2))
    
    if mbdown and button_menu_play.collidepoint((mx, my)): # if a mouse button is clicked while the cursor is over a button, the scene will switch to the correct one
        scene = 1
        paused = False
        room = rooms_list[0]
    if mbdown and button_menu_info.collidepoint((mx, my)):
        scene = -1
    if mbdown and button_menu_quit.collidepoint((mx, my)):
        running = not running


def info_screen():
    global running, scene

    screen.fill(black)

    # BACK BUTTON
    if button_back.collidepoint((mx, my)): # if the cursor is hovering over the back button, it will light up gray
        pygame.draw.rect(screen, gray, button_back)

    pygame.draw.rect(screen, white, button_back, 2) # draws the outlines of the button in white
    
    if mbdown and button_back.collidepoint((mx, my)): # if a mouse button is clicked while the cursor is over the button, the scene will switch back to the main menu
        scene = 0

    #? TEXT #ADDHERE text rendering (actually fuck text rendering. you're allowed to do it without the text rendering)
    pass


def userinterface(): # draws the user interface over everything if you are in game
    global running, uv_light, paused, timer_running, scene
    
    #! UV LIGHT
    if button_uv_light.collidepoint(mx, my) and mbdown and uv_light == 1 and not paused: # if the uv light icon gets clicked while the player has the uv light, the light will get turned on
        uv_light = 2

    if uv_light == 2: # when the player is using the light
        pygame.draw.circle(screen, color_theme[3], (mx, my), h/4) #there's a circle of light around the cursor

        if mbup: # if the player lets the mouse go, the light will turn off again
            uv_light = 1

    if uv_light == 1: # when the light is off, the light icon is drawn in the corner
        screen.blit(uv_light_icon, (w-w/27*3-w/27, h-h/27*3-w/27))

    #! PAUSE MENU
    if paused:
        screen.fill(color_theme[1])

        pygame.draw.rect(screen, color_theme[0], button_paused_continue) # makes all button backgrounds black
        pygame.draw.rect(screen, color_theme[0], button_paused_main_menu)
        pygame.draw.rect(screen, color_theme[0], button_menu_quit)

        if button_paused_continue.collidepoint((mx, my)): # if the cursor is hovering over one of the buttons, it will light up gray
            pygame.draw.rect(screen, gray, button_paused_continue)
        if button_paused_main_menu.collidepoint((mx, my)):
            pygame.draw.rect(screen, gray, button_paused_main_menu)
        if button_menu_quit.collidepoint((mx, my)):
            pygame.draw.rect(screen, gray, button_menu_quit)

        pygame.draw.rect(screen, color_theme[2], button_paused_continue, 2) # draws the outlines of all three buttons in the object color
        pygame.draw.rect(screen, color_theme[2], button_paused_main_menu, 2)
        pygame.draw.rect(screen, color_theme[2], button_menu_quit, 2)
    
        if color_theme == dark_theme:
            screen.blit(continue_text, (w/2-h/27*3/578*1944/2, h/27*18)) # draws all the icons and button texts
            screen.blit(main_menu_text, (w/2-h/27*3/392*1848/2, h/27*22))
            screen.blit(door, (w-h/27*4, h-h/27*4))

        elif color_theme == light_theme:
            screen.blit(continue_b_text, (w/2-h/27*3/578*1944/2, h/27*18)) # draws all the icons and button texts
            screen.blit(main_menu_b_text, (w/2-h/27*3/392*1848/2, h/27*22))
            screen.blit(door_b, (w-h/27*4, h-h/27*4))
        
        if mbdown and button_paused_continue.collidepoint((mx, my)): # if a mouse button is clicked while the cursor is over a button, the scene will switch to the correct one
            paused = False
        if mbdown and button_paused_main_menu.collidepoint((mx, my)):
            scene = 0
        if mbdown and button_menu_quit.collidepoint((mx, my)):
            running = not running

    #! PAUSE BUTTON
    pygame.draw.rect(screen, color_theme[0], button_back)

    if button_back.collidepoint(mx, my):
        if click:
            pygame.draw.rect(screen, color_theme[2], button_back) # when the the mouse is pressed down while hovering over the button, the button will light up in the opposite of the background color
        else:
            pygame.draw.rect(screen, color_theme[1], button_back) # when the mouse is hovering over the button, it will light up in the midtone (gray)

        if mbdown:
            paused = not paused
            timer_running = not paused
        
    pygame.draw.rect(screen, color_theme[2], pause_icon_l)
    pygame.draw.rect(screen, color_theme[2], pause_icon_r)
    
    pygame.draw.rect(screen, color_theme[2], button_back, 2) # the button is outlined in the opposite of the background color

    #! TIMER
    pygame.draw.rect(screen, color_theme[0], timer_rect)
    pygame.draw.rect(screen, color_theme[2], timer_rect, 2)
    #? #ADDHERE timer stuff
    pass


#! MAIN LOOP ------------------------------------------------------------------------------------------------------------------
while running:
    for ev in pygame.event.get(): # gets inputs for the frame
        if ev.type == QUIT: # checks whether the window has been closed -> stops the main loop
            running = not running
        if ev.type == MOUSEBUTTONDOWN: # checks whether a mouse button has been pressed down during the current frame
            mbdown = True
        if ev.type == MOUSEBUTTONUP: # checks whether a mouse button has been released during the current frame
            mbup = True

    mx, my = pygame.mouse.get_pos() # gets current cursor coordinates
    click = pygame.mouse.get_pressed()[0] # checks  wether the left mouse button is currently pressed down or not

    screen.fill(color_theme[0])
    
    if scene > 0: # if this is true, it means you are in game
        #? room.render() #FIXME once the room stuff works, remove the comment
        userinterface()
        #? room.render_uv_stuff() #FIXME once the room stuff works, remove the comment 
    if scene == 0: # renders the main menu
        menu()
    if scene == -1: # render the info screen
        info_screen()


    mbdown, mbup = False, False # reset mouse button variables

    pygame.display.flip() # put everything on the screen

    clock.tick(fps)

pygame.quit()