def init():
    global screen, clock, w, h, running

    import pygame

    pygame.init()
    screen = pygame.display.set_mode((1600, 900)) # makes a window of the size of the current screen (0, 0) and makes it fullscreen
    pygame.display.set_icon(pygame.image.load(r'assets\icon.png')) #changes the icon in the taskbar
    pygame.display.set_caption('Kryptografie Escape Room') # changes the window name in the taskbar

    clock = pygame.time.Clock() # makes it possible to force a certain frame rate (is mostly useful when in game movements are tied to frames, which isn't the case here)
    w, h = screen.get_size() # gets the size of the window so the size of buttons and icons can be done accordingly
    running = True # defines whether the main loop gets looped or not

def colors():
    global black, gray, white, light_gray, dark_gray, red, uv_color, dark_theme, light_theme, color_theme

    black = (0, 0, 0)
    gray = (127, 127, 127)
    white = (255, 255, 255)
    
    light_gray = (223, 223, 223)
    dark_gray = (31, 31, 31)
    
    red = (255, 0, 0)
    
    uv_color = (127, 0, 255)
    
    dark_theme = [black, white, dark_gray, red] # color theme = [background color, object color, timer background color (slightly grayer than the background), color of the uv reactive substances (with subtractive filter)]
    light_theme = [white, black, light_gray, black]
    color_theme = light_theme

def constants():
    global default_timer_time, words_list
    default_timer_time = 15*60*60 + 60 # calculated in frames (minutes times 60 times the amount of frames per second) # FIXME

    words_list = [
        "DISKUSSION", "AUSGANG", "BEDEUTUNG", "KONTEXT", "AUTOBAHN", "PROFESSOR", "ARGUMENT",
        "HAUSAUFGABEN", "ASSISTENT", "ZEICHNUNG", "SITUATION", "FAHRSTUHL", "SPIEGELUNG", "WISSENSCHAFT",
        "ZUGABE", "ORGANISATION", "EINDRUCK", "VARIATION", "ANERKENNUNG", "INTERAKTION", "CHEMIKALIEN"]

def variables():
    global scene, room
    scene = 0 # 0 -> main menu; 1 -> in the game; 2 -> you won; 3 -> you lost
    room = None # contains the current room object

def instances():
    global menu, pause, end_screen, timer
    import Interface, Timer
    menu = Interface.MainMenu()
    pause = Interface.PauseMenu()
    end_screen = Interface.EndScreen()
    timer = Timer.Timer(default_timer_time)

def reset_game():
    global uv_lamp, cipher_wheel, scene, rooms_list, room, color_theme
    import random, Tools, Room, Object, Cryptography
    timer.time = default_timer_time
    uv_lamp = Tools.UVLight()
    cipher_wheel = Tools.CipherWheel()
    scene = 1
    timer.running = True

    room1_code = str(random.randint(1000, 9999))
    room2_code = random.choice(words_list)
    room2_key = str(random.randint(1, 25))
    room3_code = random.choice(words_list)
    room3_key = random.choice(words_list)

    rooms_list = [
        Room.Room([
            Object.Shelf(0, 1),
            Object.Door(5, 0, room1_code),
            Object.Shelf(1),
            Object.Lamp(4),
            Object.Desk(2),
            Object.Desk(3, 1, room1_code)
        ]),
        Room.Room([
            Object.Door(0, 1, room2_code),
            Object.Shelf(5),
            Object.Lamp(1),
            Object.Desk(4, 2),
            Object.Calendar(2, room2_code, room2_key),
            Object.Desk(3)
        ]),
        Room.Room([
            Object.Desk(0, 4, room3_code),
            Object.Shelf(5),
            Object.Desk(1, 3),
            Object.Shelf(4, 2, room3_key),
            Object.Door(2, 0, '55555'),
            Object.Lamp(3)
        ])
    ]
    room = rooms_list[0]
    color_theme = light_theme

    print(room1_code, room2_code, room3_code)

def back_button():
    global scene
    import pygame, Inputs

    button_back = pygame.Rect(h/27, h/27, h/27*3, h/27*3)

    pygame.draw.rect(screen, color_theme[0], button_back)

    if button_back.collidepoint(Inputs.mx, Inputs.my):
        if Inputs.click:
            pygame.draw.rect(screen, color_theme[1], button_back) # when the the mouse is pressed down while hovering over the button, the button will light up in the opposite of the background color
        else:
            pygame.draw.rect(screen, gray, button_back) # when the mouse is hovering over the button, it will light up in the midtone (gray)

        if Inputs.mbdown:
            scene = 1
            room.active_interaction_screen = None
            room.active_uv_drawing = None

    pygame.draw.rect(screen, color_theme[1], button_back, 2) # the button is outlined in the opposite of 
