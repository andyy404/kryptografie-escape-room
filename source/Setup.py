def init():
    global screen, clock, w, h, running

    import pygame

    pygame.init()
    screen = pygame.display.set_mode((800, 450)) # makes a window of the size of the current screen (0, 0) and makes it fullscreen
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
    
    color_theme = light_theme # game switches between these color themes, depending whether the room's lamp is on or off (light theme -> on, dark theme -> off)

def constants():
    global default_timer_time, words_list
    default_timer_time = 15*60*60 + 60 # calculated in frames (minutes times 60 times the amount of frames per second) # FIXME

    words_list = [
        "Diskussion", "Ausgang", "Bedeutung", "Kontext", "Autobahn", "Professor", "Argument", "Hausaufgaben", "Assistent", "Zeichnung", 
        "Situation", "Fahrstuhl", "Spiegelung", "Wissenschaft", "Zugabe", "Organisation", "Eindruck", "Variation", "Anerkennung", "Interaktion", "Chemikalien"]

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
    import Tools, Room, Object
    timer.time = default_timer_time
    uv_lamp = Tools.UVLight()
    cipher_wheel = Tools.CipherWheel()
    scene = 1
    timer.running = True
    rooms_list = [
        Room.Room([
            Object.Shelf(0),
            Object.Door(5, 0),
            Object.Shelf(1),
            Object.Lamp(4),
            Object.Desk(2),
            Object.Desk(3)
        ]),
        Room.Room([
            Object.Door(0, 1),
            Object.Shelf(5),
            Object.Lamp(1),
            Object.Desk(4),
            Object.Calendar(2),
            Object.Desk(3)
        ]),
        Room.Room([
            Object.Desk(0),
            Object.Shelf(5),
            Object.Desk(1),
            Object.Shelf(4),
            Object.Door(2, 0),
            Object.Lamp(3)
        ])
    ]
    room = rooms_list[0]
    color_theme = light_theme




