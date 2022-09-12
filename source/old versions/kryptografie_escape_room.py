# kryptografie escape room
# programmiert von Medea Emch im Rahmen einer Maturaarbeit an der Kantonsschule Alpenquai Luzern im Jahr 2022

#! IMPORTS --------------------------------------------------------------------------------------------------------------------
import pygame, random
from pygame.locals import *


#! SETUP ----------------------------------------------------------------------------------------------------------------------
pygame.init()

screen = pygame.display.set_mode((0,0), FULLSCREEN) # makes a window of the size of the current screen (0, 0) and makes it fullscreen
pygame.display.set_icon(pygame.image.load(r'assets\icon.png')) #changes the icon in the taskbar
pygame.display.set_caption('Kryptografie Escape Room') # changes the window name in the taskbar

clock = pygame.time.Clock() # makes it possible to force a certain frame rate (is mostly useful when in game movements are tied to frames, which isn't the case here)
w, h = screen.get_size() # gets the size of the window so the size of buttons and icons can be done accordingly
running = True # defines whether the main loop gets looped or not


#! LOAD IMAGES ----------------------------------------------------------------------------------------------------------------
uv_light_icon = pygame.transform.scale(pygame.image.load(r'assets\light.png'), (int(w/27*2), int(w/27*2))) # in game icon of the uv lamp

titel = pygame.transform.scale(pygame.image.load(r'assets\titel.png'), (int(w/8*6), int(w/8*6/2000*578))) # title in the main menu
door = pygame.transform.scale(pygame.image.load(r'assets\quit.png'), (int(h/27*3), int(h/27*3))) # quit game icon in the main menu
start_text = pygame.transform.scale(pygame.image.load(r'assets\start.png'), (int(h/27*4/526*1159), int(h/27*4))) # start button text icon in the main menu

continue_text = pygame.transform.scale(pygame.image.load(r'assets\continue.png'), (int(h/27*3/578*1944), int(h/27*3)))
main_menu_text = pygame.transform.scale(pygame.image.load(r'assets\mainmenu.png'), (int(h/27*3/392*1848), int(h/27*3)))

continue_b_text = pygame.transform.scale(pygame.image.load(r'assets\continue_black.png'), (int(h/27*3/578*1944), int(h/27*3)))
main_menu_b_text = pygame.transform.scale(pygame.image.load(r'assets\mainmenu_black.png'), (int(h/27*3/392*1848), int(h/27*3)))
door_b = pygame.transform.scale(pygame.image.load(r'assets\quit_black.png'), (int(h/27*3), int(h/27*3)))

your_time_is_up = pygame.transform.scale(pygame.image.load(r'assets\lost.png'), (int(w/8*6), int(w/8*6/2057*350)))
you_did_it = pygame.transform.scale(pygame.image.load(r'assets\won.png'), (int(w/8*6), int(w/8*6/1297*350)))


#! COLORS ---------------------------------------------------------------------------------------------------------------------
black = (0, 0, 0)
gray = (127, 127, 127)
white = (255, 255, 255)

light_gray = (223, 223, 223)
dark_gray = (31, 31, 31)

red = (255, 0, 0)

uv_color = (127, 0, 255)

dark_theme = [black, white, dark_gray, red] # color theme = [background color, object color, timer background color (slightly grayer than the background), color of the uv reactive substances (with subtractive filter)]
light_theme = [white, black, light_gray, black]

color_theme = light_theme # game switches between these color themes, depending whether the room's lamp is on or off (light theme -> on, dark theme -> off)


#! IMPORTANT RECTANGLES (left edge, upper edge, width, height) ----------------------------------------------------------------
button_uv_light = pygame.Rect(w-w/27*3-w/27, h-h/27*3-w/27, w/27*2, w/27*2) # in game flashlight icon

button_menu_play = pygame.Rect(w/2-w/8, h/27*17, w/4, h/27*4) # main menu button to start game
button_menu_quit = pygame.Rect(w-h/27*4, h-h/27*4, h/27*3, h/27*3) # main menu button to quit game

button_back = pygame.Rect(h/27, h/27, h/27*3, h/27*3) # the back button in the pause menu (also the pause button in game)
timer_rect = pygame.Rect(w/2-h/27*3.5, h/27, h/27*7, h/27*3) # the rectangle around the in game timer
timer_point_upper = pygame.Rect(w/2-2, h/27*2-2, 4, 4)
timer_point_lower = pygame.Rect(w/2-2, h/27*3-2, 4, 4)

button_paused_continue = pygame.Rect(w/2-h/27*8, h/27*18, h/27*16, h/27*3)
button_paused_main_menu = pygame.Rect(w/2-h/27*8, h/27*22, h/27*16, h/27*3)

pause_icon_l = pygame.Rect(h/27/5*8, h/27/5*8, h/27/5*3, h/27/5*3*3)
pause_icon_r = pygame.Rect(h/27/5*14, h/27/5*8, h/27/5*3, h/27/5*3*3)


#! OBJECTS --------------------------------------------------------------------------------------------------------------------
class Shelf():
    '''(shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position, shelf_type = 0):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.type = shelf_type

        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        self.pos5 = self.position*w/50*5
        self.pos6 = self.position*w/50*6

        if self.type == 1:
            self.added_points = [
                (w/50*7.5 + self.pos6, h/50*31),
                (w/50*7.25 + self.pos6, h/50*30),
                (w/50*10.25 + self.pos6, h/50*29.25),
                (w/50*10.75 + self.pos6, h/50*28),
                (w/50*11.75 + self.pos6, h/50*27.75),
                (w/50*12.5 + self.pos6, h/50*30.75),
                (w/50*11.5 + self.pos6, h/50*31),
                (w/50*10.5 + self.pos6, h/50*30.25),
                (w/50*10.75 + self.pos6, h/50*30),
                (w/50*11.25 + self.pos6, h/50*29.75),
                (w/50*11 + self.pos6, h/50*29.25),
                (w/50*10.5 + self.pos6, h/50*29.5),
                (w/50*10.75 + self.pos6, h/50*30),
                (w/50*10.5 + self.pos6, h/50*30.25),
                (w/50*7.5 + self.pos6, h/50*31)
            ]
            
        if self.type == 2:
            self.added_points = [
                (w/50*8.5 + self.pos6, h/50*31),
                (w/50*8.25 + self.pos6, h/50*30.75),
                (w/50*8.5 + self.pos6, h/50*30.5),
                (w/50*9 + self.pos6, h/50*30.5),
                (w/50*9 + self.pos6, h/50*30),
                (w/50*8.5 + self.pos6, h/50*30),
                (w/50*8.5 + self.pos6, h/50*30.5),
                (w/50*8.25 + self.pos6, h/50*30.75),
                (w/50*8 + self.pos6, h/50*30.5),
                (w/50*8 + self.pos6, h/50*30),
                (w/50*8.5 + self.pos6, h/50*29.5),
                (w/50*9 + self.pos6, h/50*29.5),
                (w/50*9.5 + self.pos6, h/50*30),
                (w/50*12 + self.pos6, h/50*30),
                (w/50*12 + self.pos6, h/50*30.5),
                (w/50*11.75 + self.pos6, h/50*31),
                (w/50*11.5 + self.pos6, h/50*30.75),
                (w/50*11.25 + self.pos6, h/50*30.75),
                (w/50*11 + self.pos6, h/50*30.5),
                (w/50*10.75 + self.pos6, h/50*31),
                (w/50*10.5 + self.pos6, h/50*30.5),
                (w/50*10.25 + self.pos6, h/50*30.75),
                (w/50*10 + self.pos6, h/50*30.5),
                (w/50*9.5 + self.pos6, h/50*30.5),
                (w/50*9 + self.pos6, h/50*31),
                (w/50*8.5 + self.pos6, h/50*31)
            ]
            
    def return_drawing(self):
        if self.position <= 2:
            self.polygon = [
                (w/50*7 + self.pos6, h/50*19),
                (w/50*13 + self.pos6, h/50*19),
                (w/50*15 + self.pos5, h/50*20),
                (w/50*15 + self.pos5, h/50*40),
                (w/50*13 + self.pos6, h/50*43),
                (w/50*7 + self.pos6, h/50*43)
            ]

        else:
            self.polygon = [
                (w/50*10 + self.pos5, h/50*20),
                (w/50*7 + self.pos6, h/50*19),
                (w/50*13 + self.pos6, h/50*19),
                (w/50*13 + self.pos6, h/50*43),
                (w/50*7 + self.pos6, h/50*43),
                (w/50*10 + self.pos5, h/50*40)
            ]

        self.lines = [
            (w/50*13 + self.pos6, h/50*43),
            (w/50*7 + self.pos6, h/50*43),
            (w/50*8 + self.pos6, h/50*43),
            (w/50*8 + self.pos6, h/50*39),
            (w/50*9 + self.pos6, h/50*39),
            (w/50*9 + self.pos6, h/50*43),
            (w/50*9 + self.pos6, h/50*40),
            (w/50*10 + self.pos6, h/50*40),
            (w/50*10 + self.pos6, h/50*43),
            (w/50*10 + self.pos6, h/50*38),
            (w/50*12 + self.pos6, h/50*38),
            (w/50*12 + self.pos6, h/50*43),
            (w/50*12 + self.pos6, h/50*39),
            (w/50*13 + self.pos6, h/50*39),
            (w/50*13 + self.pos6, h/50*43), # 14

            (w/50*13 + self.pos6, h/50*37),
            (w/50*7 + self.pos6, h/50*37),
            (w/50*7 + self.pos6, h/50*32),
            (w/50*9 + self.pos6, h/50*32),
            (w/50*9 + self.pos6, h/50*37),
            (w/50*9 + self.pos6, h/50*33),
            (w/50*10 + self.pos6, h/50*33),
            (w/50*10 + self.pos6, h/50*37),
            (w/50*10 + self.pos6, h/50*34),
            (w/50*11 + self.pos6, h/50*34),
            (w/50*11 + self.pos6, h/50*37),
            (w/50*11 + self.pos6, h/50*32),
            (w/50*12 + self.pos6, h/50*32),
            (w/50*12 + self.pos6, h/50*37),
            (w/50*12 + self.pos6, h/50*33),
            (w/50*13 + self.pos6, h/50*33),
            (w/50*13 + self.pos6, h/50*37),
            
            (w/50*13 + self.pos6, h/50*31),
            (w/50*7 + self.pos6, h/50*31),
            (w/50*7 + self.pos6, h/50*28),  # 34
            (w/50*8 + self.pos6, h/50*28),  #
            (w/50*8 + self.pos6, h/50*31),  # 36
            (w/50*8 + self.pos6, h/50*27),  #
            (w/50*10 + self.pos6, h/50*27), #
            (w/50*10 + self.pos6, h/50*31), # 39
            (w/50*10 + self.pos6, h/50*26), #
            (w/50*11 + self.pos6, h/50*26), #
            (w/50*11 + self.pos6, h/50*31), # 42
            (w/50*11 + self.pos6, h/50*28), #
            (w/50*12 + self.pos6, h/50*28), #
            (w/50*12 + self.pos6, h/50*31), # 45
            (w/50*12 + self.pos6, h/50*26), #
            (w/50*13 + self.pos6, h/50*26), # 47
            (w/50*13 + self.pos6, h/50*31),

            (w/50*13 + self.pos6, h/50*25),
            (w/50*7 + self.pos6, h/50*25),
            (w/50*7 + self.pos6, h/50*20),
            (w/50*9 + self.pos6, h/50*20),
            (w/50*9 + self.pos6, h/50*25),
            (w/50*9 + self.pos6, h/50*22),
            (w/50*10 + self.pos6, h/50*22),
            (w/50*10 + self.pos6, h/50*25),
            (w/50*10 + self.pos6, h/50*20),
            (w/50*12 + self.pos6, h/50*20),
            (w/50*12 + self.pos6, h/50*25),
            (w/50*12 + self.pos6, h/50*21),
            (w/50*13 + self.pos6, h/50*21),
            (w/50*13 + self.pos6, h/50*25),

            (w/50*13 + self.pos6, h/50*19),
            (w/50*7 + self.pos6, h/50*19),
            (w/50*7 + self.pos6, h/50*43)
        ]

        if self.type > 0:
            for i in range(34, 48):
                self.lines.pop(34)
            for point in self.added_points:
                self.lines.insert(34, point)
        
        return [self.polygon, self.lines]

class Desk():
    '''(desk_type = 0 is empty; desk_type = 1 has some papers with a hidden message; desk_type = 2 has a caesar cipher wheel; desk_type = 3 has a tabula recta; desk_type = 4 has a whole computer'''
    def __init__(self, position, desk_type = 0):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.type = desk_type

        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        self.pos5 = self.position*w/50*5
        self.pos6 = self.position*w/50*6

        if self.type == 1:
            self.added_points = [
                (w/50*9.75 + self.pos6, h/50*31),
                (w/50*10.75 + self.pos6, h/50*30.75),
                (w/50*10 + self.pos6, h/50*30),
                (w/50*9 + self.pos6, h/50*30.25),
                (w/50*9.75 + self.pos6, h/50*31),
                (w/50*10.75 + self.pos6, h/50*30.75),
                (w/50*9.5 + self.pos6, h/50*30.75),
                (w/50*10.5 + self.pos6, h/50*30.5), #
                (w/50*8.25 + self.pos6, h/50*30.5),
                (w/50*10.25 + self.pos6, h/50*30.25),
                (w/50*9 + self.pos6, h/50*30.25),
                (w/50*9.75 + self.pos6, h/50*31)
            ]

        if self.type == 2:
            self.added_points = [
                (w/50*10 + self.pos6, h/50*31),
                (w/50*10 + self.pos6, h/50*30.75),
                (w/50*10.25 + self.pos6, h/50*30.5),
                (w/50*10 + self.pos6, h/50*30.25),
                (w/50*9.75 + self.pos6, h/50*30.5),
                (w/50*10 + self.pos6, h/50*30.75),
                (w/50*10 + self.pos6, h/50*31),
                (w/50*10.5 + self.pos6, h/50*30.75),
                (w/50*10.5 + self.pos6, h/50*30.25),
                (w/50*10 + self.pos6, h/50*30),
                (w/50*9.5 + self.pos6, h/50*30.25),
                (w/50*9.5 + self.pos6, h/50*30.75),
                (w/50*10 + self.pos6, h/50*31)
            ]

        if self.type == 3:
            self.added_points = [
                (w/50*10.25 + self.pos6, h/50*31),
                (w/50*11 + self.pos6, h/50*30.25),
                (w/50*10 + self.pos6, h/50*30),
                (w/50*9.75 + self.pos6, h/50*30.25),
                (w/50*10.75 + self.pos6, h/50*30.5),
                (w/50*9.75 + self.pos6, h/50*30.25),
                (w/50*9.5 + self.pos6, h/50*30.5),
                (w/50*10.5 + self.pos6, h/50*30.75),
                (w/50*9.5 + self.pos6, h/50*30.5),
                (w/50*9.25 + self.pos6, h/50*30.75),
                (w/50*10.25 + self.pos6, h/50*31)
            ]

        if self.type == 4:
            self.added_points = [
                (w/50*10 + self.pos5, h/50*30),
                (w/50*13.5 + self.pos5, h/50*30),
                (w/50*13.5 + self.pos5, h/50*29.75),
                (w/50*13 + self.pos5, h/50*29.75),
                (w/50*12.75 + self.pos5, h/50*28.75),
                (w/50*14.75 + self.pos5, h/50*28.75),
                (w/50*14.75 + self.pos5, h/50*25.25),
                (w/50*10.25 + self.pos5, h/50*25.25),
                (w/50*10.25 + self.pos5, h/50*28.75),
                (w/50*10.5 + self.pos5, h/50*28.75),
                (w/50*10.5 + self.pos5, h/50*25.5),
                (w/50*14.5 + self.pos5, h/50*25.5),
                (w/50*14.5 + self.pos5, h/50*28.75),
                (w/50*14.25 + self.pos5, h/50*28.5),
                (w/50*14.25 + self.pos5, h/50*28.75),
                (w/50*14.5 + self.pos5, h/50*28.5),
                (w/50*10.5 + self.pos5, h/50*28.5),
                (w/50*10.5 + self.pos5, h/50*29.5),
                (w/50*11.5 + self.pos5, h/50*29.5),
                (w/50*11.5 + self.pos5, h/50*28.5),
                (w/50*11.5 + self.pos5, h/50*28.75),
                (w/50*12.75 + self.pos5, h/50*28.75),
                (w/50*12.25 + self.pos5, h/50*28.75),
                (w/50*12.5 + self.pos5, h/50*29.75),
                (w/50*13 + self.pos5, h/50*29.75),
                (w/50*11.5 + self.pos5, h/50*29.75),
                (w/50*11.5 + self.pos5, h/50*30),
                (w/50*10 + self.pos5, h/50*30),
                (w/50*7 + self.pos6, h/50*31)
            ]

    def return_drawing(self):
        if self.position <= 2:
            self.polygon = [
                (w/50*7 + self.pos6, h/50*31),
                (w/50*10 + self.pos5, h/50*30),
                (w/50*15 + self.pos5, h/50*30),
                (w/50*15 + self.pos5, h/50*40),
                (w/50*13 + self.pos6, h/50*43),
                (w/50*12 + self.pos6, h/50*43),
                (w/50*12 + self.pos6, h/50*32),
                (w/50*11 + self.pos5, h/50*32),
                (w/50*11 + self.pos5, h/50*40),
                (w/50*8 + self.pos6, h/50*43),
                (w/50*7 + self.pos6, h/50*43)
            ]

        else:
            self.polygon = [
                (w/50*10 + self.pos5, h/50*30),
                (w/50*15 + self.pos5, h/50*30),
                (w/50*13 + self.pos6, h/50*31),
                (w/50*13 + self.pos6, h/50*43),
                (w/50*12 + self.pos6, h/50*43),
                (w/50*14 + self.pos5, h/50*40),
                (w/50*14 + self.pos5, h/50*32),
                (w/50*8 + self.pos6, h/50*32),
                (w/50*8 + self.pos6, h/50*43),
                (w/50*7 + self.pos6, h/50*43),
                (w/50*10 + self.pos5, h/50*40)
            ]

        self.lines = [
            (w/50*10 + self.pos5, h/50*30),
            (w/50*7 + self.pos6, h/50*31),
            (w/50*7 + self.pos6, h/50*43),
            (w/50*7 + self.pos6, h/50*31),
            (w/50*13 + self.pos6, h/50*31),
            (w/50*15 + self.pos5, h/50*30),
            (w/50*13 + self.pos6, h/50*31),
            (w/50*13 + self.pos6, h/50*43),
            (w/50*12 + self.pos6, h/50*43),
            (w/50*12 + self.pos6, h/50*32),
            (w/50*8 + self.pos6, h/50*32),
            (w/50*8 + self.pos6, h/50*43)
        ]
        
        if self.type > 0:
            for point in self.added_points:
                self.lines.insert(4, point)

        return [self.polygon, self.lines]

class Door():
    '''a shelf for decoration. (shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right

        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        self.pos5 = self.position*w/50*5
        self.pos6 = self.position*w/50*6

    def return_drawing(self):
        self.polygon = [
            (w/50*10 + self.pos5, h/50*20),
            (w/50*15 + self.pos5, h/50*20),
            (w/50*15 + self.pos5, h/50*40),
            (w/50*10 + self.pos5, h/50*40)
        ]

        self.lines = [
            (w/50*11 + self.pos5, h/50*29),
            (w/50*12 + self.pos5, h/50*29),
            (w/50*12 + self.pos5, h/50*31),
            (w/50*11 + self.pos5, h/50*31),
            (w/50*11 + self.pos5, h/50*29)
        ]
        
        return [self.polygon, self.lines]

class Lamp():
    '''a shelf for decoration. (shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right

        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        self.pos5 = self.position*w/50*5
        self.pos6 = self.position*w/50*6

    def return_drawing(self):
        self.polygon = [
            (w/50*11 + self.pos5, h/50*40),
            (w/50*12 + self.pos5, h/50*38),
            (w/50*12.5 + self.pos5, h/50*31),
            (w/50*12 + self.pos5, h/50*24),
            (w/50*11 + self.pos5, h/50*24),
            (w/50*12 + self.pos5, h/50*20),
            (w/50*13 + self.pos5, h/50*20),
            (w/50*14 + self.pos5, h/50*24),
            (w/50*13 + self.pos5, h/50*24),
            (w/50*12.5 + self.pos5, h/50*31),
            (w/50*13 + self.pos5, h/50*38),
            (w/50*14 + self.pos5, h/50*40)
        ]

        self.lines = [
            (w/50*12 + self.pos5, h/50*38),
            (w/50*13 + self.pos5, h/50*38),
            (w/50*12 + self.pos5, h/50*24),
            (w/50*13 + self.pos5, h/50*24)
        ]
        
        return [self.polygon, self.lines]

class Calendar():
    '''a shelf for decoration. (shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right

        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        self.pos5 = self.position*w/50*5
        self.pos6 = self.position*w/50*6

    def return_drawing(self):
        self.polygon = [
            (w/50*11 + self.pos5, h/50*26),
            (w/50*14 + self.pos5, h/50*26),
            (w/50*14 + self.pos5, h/50*29),
            (w/50*11 + self.pos5, h/50*29)
        ]

        self.lines = [
            (w/50*12 + self.pos5, h/50*26),
            (w/50*12 + self.pos5, h/50*29),
            (w/50*13 + self.pos5, h/50*29),
            (w/50*13 + self.pos5, h/50*26)
        ]
        
        return [self.polygon, self.lines]

#! ROOMS ----------------------------------------------------------------------------------------------------------------------
class Room1():
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.object_list = [
            Shelf(0),
            Door(5),
            Shelf(1),
            Lamp(4),
            Desk(2),
            Desk(3)
        ]

        self.drawing_list = []

        for obj in self.object_list:
            self.drawing_list.append(obj.return_drawing())

    def draw_objects(self):
        for object_drawing in self.drawing_list:
                pygame.draw.polygon(screen, color_theme[0], object_drawing[0])
                pygame.draw.polygon(screen, color_theme[1], object_drawing[0], 2)
                pygame.draw.lines(screen, color_theme[1], False, object_drawing[1], 2)

class Room2():
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.object_list = [
            Door(0),
            Shelf(5),
            Lamp(1),
            Desk(4),
            Calendar(2),
            Desk(3)
        ]

        self.drawing_list = []

        for obj in self.object_list:
            self.drawing_list.append(obj.return_drawing())

    def draw_objects(self):
        for object_drawing in self.drawing_list:
                pygame.draw.polygon(screen, color_theme[0], object_drawing[0])
                pygame.draw.polygon(screen, color_theme[1], object_drawing[0], 2)
                pygame.draw.lines(screen, color_theme[1], False, object_drawing[1], 2)

class Room3():
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.object_list = [
            Desk(0),
            Shelf(5),
            Desk(1),
            Shelf(4),
            Door(2),
            Lamp(3)
        ]

        self.drawing_list = []

        for obj in self.object_list:
            self.drawing_list.append(obj.return_drawing())

    def draw_objects(self):
        for object_drawing in self.drawing_list:
                pygame.draw.polygon(screen, color_theme[0], object_drawing[0])
                pygame.draw.polygon(screen, color_theme[1], object_drawing[0], 2)
                pygame.draw.lines(screen, color_theme[1], False, object_drawing[1], 2)

#! GAME CONSTANTS -------------------------------------------------------------------------------------------------------------
default_timer_time = 0.1*60*60 + 60 # calculated in frames (minutes times 60 times the amount of frames per second) 

words_list = [
    "Diskussion", "Ausgang", "Bedeutung", "Kontext", "Autobahn", "Professor", "Argument", "Hausaufgaben", "Assistent", "Zeichnung", 
    "Situation", "Fahrstuhl", "Spiegelung", "Wissenschaft", "Zugabe", "Organisation", "Eindruck", "Variation", "Anerkennung", "Interaktion", "Chemikalien"]

timer_display_coordinate_left = int(w/2 - h/27*3)
timer_display_coordinate_right = int(w/2 - h/27*2)

timer_display_coordinate_upper = int(h/27*1.5)
timer_display_coordinate_middle = int(h/27*2.5)
timer_display_coordinate_lower = int(h/27*3.5)


#! GAME VARIABLES -------------------------------------------------------------------------------------------------------------
uv_light = 0 # 0 -> do not have it; 1 -> have it but it's off; 2 -> have it and it's on
scene = 0 # 0 -> main menu; 1 -> in the game; 2 -> you won; 3 -> you lost
mbdown, mbup = False, False # these variables show whether there was a mouse button down or mouse button up event in the current frame (if a mouse button got clicked or released)

room = None # contains the current room object 

paused = False # whether the game is paused or not
timer_running = False # whether the timer is running or not
timer_time = default_timer_time # sets the current time to the default starting time


#! FUNCTIONS ------------------------------------------------------------------------------------------------------------------

#! TIMER DIGITS
def timer_zero(modifier):

    pygame.draw.lines(screen, color_theme[1], True, (
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_lower)), 4)


def timer_one(modifier):

    pygame.draw.line(screen, color_theme[1], (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower), 4)


def timer_two(modifier):

    pygame.draw.lines(screen, color_theme[1], False, ((timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower)), 4)


def timer_three(modifier):

    pygame.draw.lines(screen, color_theme[1], False, (
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_lower)), 4)


def timer_four(modifier):

    pygame.draw.lines(screen, color_theme[1], False, (
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower)), 4)


def timer_five(modifier):

    pygame.draw.lines(screen, color_theme[1], False, (
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_lower)), 4)


def timer_six(modifier):
        
    pygame.draw.lines(screen, color_theme[1], False, (
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_middle)), 4)


def timer_seven(modifier):

    pygame.draw.lines(screen, color_theme[1], False, (
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower)), 4)


def timer_eight(modifier, color = color_theme[1], thickness = 4):

    pygame.draw.lines(screen, color, True, (
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_lower)), thickness)


def timer_nine(modifier):

    pygame.draw.lines(screen, color_theme[1], False, (
        (timer_display_coordinate_right + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_middle),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_upper),
        (timer_display_coordinate_right + modifier, timer_display_coordinate_lower),
        (timer_display_coordinate_left + modifier, timer_display_coordinate_lower)), 4)

timer_draw_functions = [timer_zero, timer_one, timer_two, timer_three, timer_four, timer_five, timer_six, timer_seven, timer_eight, timer_nine]


def menu(): # shows the main menu screen
    global running, scene, paused, room, timer_running, rooms_list, timer_time, color_theme

    screen.fill(black)

    if button_menu_play.collidepoint((mx, my)): # if the cursor is hovering over one of the buttons, it will light up gray
        pygame.draw.rect(screen, gray, button_menu_play)
    if button_menu_quit.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_quit)

    pygame.draw.rect(screen, white, button_menu_play, 2) # draws the outlines of all three buttons in white
    pygame.draw.rect(screen, white, button_menu_quit, 2)

    screen.blit(titel, (w/8, h/27*2)) # draws all the icons and button texts
    screen.blit(door, (w-h/27*4, h-h/27*4))
    screen.blit(start_text, (w/2-h/27*4/526*1159/2, h/27*19-h/27*4/2))
    
    if mbdown and button_menu_play.collidepoint((mx, my)): # if a mouse button is clicked while the cursor is over a button, the scene will switch to the correct one
        scene = 1
        paused = False
        timer_running = True
        rooms_list = [Room1(), Room2(), Room3()] # ADD all the rooms
        room = rooms_list[0]
        timer_time = default_timer_time
        color_theme = light_theme
    if mbdown and button_menu_quit.collidepoint((mx, my)):
        running = not running


def uv_light():
    global uv_light

    if button_uv_light.collidepoint(mx, my) and mbdown and uv_light == 1 and not paused: # if the uv light icon gets clicked while the player has the uv light, the light will get turned on
        uv_light = 2

    if uv_light == 2: # when the player is using the light
        pygame.draw.circle(screen, uv_color, (mx, my), h/4) #there's a circle of light around the cursor

        if mbup: # if the player lets the mouse go, the light will turn off again
            uv_light = 1

    if uv_light == 1: # when the light is off, the light icon is drawn in the corner
        screen.blit(uv_light_icon, (w-w/27*3-w/27, h-h/27*3-w/27))


def pause_menu():
    global running, paused, timer_running, scene
    
    screen.fill(gray)

    pygame.draw.rect(screen, color_theme[0], button_paused_continue) # makes all button backgrounds black
    pygame.draw.rect(screen, color_theme[0], button_paused_main_menu)
    pygame.draw.rect(screen, color_theme[0], button_menu_quit)

    if button_paused_continue.collidepoint((mx, my)): # if the cursor is hovering over one of the buttons, it will light up gray
        pygame.draw.rect(screen, gray, button_paused_continue)
    if button_paused_main_menu.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_paused_main_menu)
    if button_menu_quit.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_quit)

    pygame.draw.rect(screen, color_theme[1], button_paused_continue, 2) # draws the outlines of all three buttons in the object color
    pygame.draw.rect(screen, color_theme[1], button_paused_main_menu, 2)
    pygame.draw.rect(screen, color_theme[1], button_menu_quit, 2)
    
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
        timer_running = not paused
    if mbdown and button_paused_main_menu.collidepoint((mx, my)):
        scene = 0
    if mbdown and button_menu_quit.collidepoint((mx, my)):
        running = not running


def pause_button():
    global paused, timer_running

    pygame.draw.rect(screen, color_theme[0], button_back)

    if button_back.collidepoint(mx, my):
        if click:
            pygame.draw.rect(screen, color_theme[1], button_back) # when the the mouse is pressed down while hovering over the button, the button will light up in the opposite of the background color
        else:
            pygame.draw.rect(screen, gray, button_back) # when the mouse is hovering over the button, it will light up in the midtone (gray)

        if mbdown:
            paused = not paused
            timer_running = not paused
        
    pygame.draw.rect(screen, color_theme[1], pause_icon_l)
    pygame.draw.rect(screen, color_theme[1], pause_icon_r)
    
    pygame.draw.rect(screen, color_theme[1], button_back, 2) # the button is outlined in the opposite of the background color


def timer_update():
    global timer_list

    pygame.draw.rect(screen, color_theme[0], timer_rect)
    pygame.draw.rect(screen, color_theme[1], timer_rect, 2)
    
    timer_seconds = ((timer_time - timer_time % 60) / 60) % 60
    timer_single_seconds = timer_seconds % 10
    timer_ten_seconds = (timer_seconds - timer_seconds % 10) / 10

    timer_minutes = (((timer_time - timer_time % 60) / 60) - timer_seconds) / 60
    timer_single_minutes = timer_minutes % 10
    timer_ten_minutes = (timer_minutes - timer_minutes % 10) / 10

    timer_list = [int(timer_ten_minutes), int(timer_single_minutes), int(timer_ten_seconds), int(timer_single_seconds)]

    for i, time in enumerate(timer_list):
        if i <= 1:
            modifier = int(i * h/27*1.5)
        else:
            modifier = int(i * h/27*1.5 + h/27*0.5)

        timer_eight(modifier, color_theme[2], 4)
        timer_draw_functions[time](modifier)

    if (((timer_time - timer_time % 30) / 30) % 60) % 2 == 0:
        pygame.draw.rect(screen, color_theme[1], timer_point_upper)
        pygame.draw.rect(screen, color_theme[1], timer_point_lower)


def userinterface(): # draws the user interface over everything if you are in game
    
    uv_light()

    if paused:
        pause_menu()

    pause_button()

    timer_update()


def check_inputs():
    global running, mbdown, mbup, mx, my, click

    mbdown, mbup = False, False # reset mouse button variables

    for ev in pygame.event.get(): # gets inputs for the frame
        if ev.type == QUIT: # checks whether the window has been closed -> stops the main loop
            running = not running
        if ev.type == MOUSEBUTTONDOWN: # checks whether a mouse button has been pressed down during the current frame
            mbdown = True
        if ev.type == MOUSEBUTTONUP: # checks whether a mouse button has been released during the current frame
            mbup = True

    mx, my = pygame.mouse.get_pos() # gets current cursor coordinates
    click = pygame.mouse.get_pressed()[0] # checks  wether the left mouse button is currently pressed down or not


def end(won):
    global running, scene

    if button_paused_main_menu.collidepoint((mx, my)): #if the mouse is hovering over a button, it lights up gray
        pygame.draw.rect(screen, gray, button_paused_main_menu)
    if button_menu_quit.collidepoint((mx, my)):
        pygame.draw.rect(screen, gray, button_menu_quit)

    pygame.draw.rect(screen, color_theme[1], button_paused_main_menu, 2) # draws the outlines of all three buttons in white
    pygame.draw.rect(screen, color_theme[1], button_menu_quit, 2)
    
    if won == True:
        screen.blit(you_did_it, (w/8, h/27*7))

        pygame.draw.rect(screen, color_theme[1], timer_rect, 2)

        for i, time in enumerate(timer_list):
            if i <= 1:
                modifier = int(i * h/27*1.5)
            else:
                modifier = int(i * h/27*1.5 + h/27*0.5)

            timer_eight(modifier, color_theme[2], 4)
            timer_draw_functions[time](modifier)

    elif won == False:
        screen.blit(your_time_is_up, (w/8, h/27*7))

    screen.blit(main_menu_text, (w/2-h/27*3/392*1848/2, h/27*22))
    screen.blit(door, (w-h/27*4, h-h/27*4))
    
    if mbdown and button_paused_main_menu.collidepoint((mx, my)):
        scene = 0
    if mbdown and button_menu_quit.collidepoint((mx, my)):
        running = not running


def room_lines():
    pygame.draw.rect(screen, color_theme[1], (w/50*10, h/50*10, w/50*10*3, h/50*10*3), 2)

    pygame.draw.line(screen, color_theme[1], (0, 0), (w/50*10, h/50*10), 2)
    pygame.draw.line(screen, color_theme[1], (w, 0), (w/50*10*4,  h/50*10), 2)
    pygame.draw.line(screen, color_theme[1], (0, h), (w/50*10, h/50*10*4), 2)
    pygame.draw.line(screen, color_theme[1], (w, h), (w/50*10*4, h/50*10*4), 2)

#! MAIN LOOP ------------------------------------------------------------------------------------------------------------------
while running:
    check_inputs()

    screen.fill(color_theme[0])
    
    if scene == 1: # if this is true, it means you are in game
        room_lines()
        room.draw_objects()
        userinterface()
    if scene == 0: # renders the main menu
        menu()
    if scene == 2:
        end(True)
    if scene == 3:
        end(False)

    if timer_running:
        timer_time -= 1 # count down the timer

    if timer_time < 0:
        scene = 3
        color_theme = dark_theme
        timer_time = 0
        timer_running = False

    pygame.display.flip() # put everything on the screen

    clock.tick(60)

pygame.quit()