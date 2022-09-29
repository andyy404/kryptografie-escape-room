import pygame, Setup, Inputs, Surfaces

class MainMenu():
    def __init__(self):
        self.text_titel1 = Surfaces.Text(Surfaces.gothic, "Kryptografie", Setup.white, "width", Setup.w/3, [0, Setup.h/27*2], ["center", "top"]) # title in the main menu
        self.text_titel2 = Surfaces.Text(Surfaces.gothic, "Escape Room", Setup.white, "width", Setup.w/8*6, [0, Setup.h/27*5], ["center", "top"]) # title in the main menu
        self.text_start = Surfaces.Text(Surfaces.gothic, "Start Game", Setup.white, "height", Setup.h/27*4, [0, Setup.h/27*20], ["center", "top"]) # start button text icon in the main menu

        self.icon_quit = Surfaces.Image(r'assets\quit.png', "height", Setup.h/27*3, [Setup.h/27, Setup.h/27], ["right", "bottom"]) # quit game icon in the main menu

    def update(self):
        Setup.screen.fill(Setup.black)

        if self.text_start.get_rect().collidepoint((Inputs.mx, Inputs.my)): # if the cursor is hovering over one of the buttons, it will light up gray
            pygame.draw.rect(Setup.screen, Setup.gray, self.text_start.get_rect())
        if self.icon_quit.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            pygame.draw.rect(Setup.screen, Setup.gray, self.icon_quit.get_rect())

        pygame.draw.rect(Setup.screen, Setup.white, self.text_start.get_rect(), 2) # draws the outlines of all three buttons in white
        pygame.draw.rect(Setup.screen, Setup.white, self.icon_quit.get_rect(), 2)

        self.text_titel1.draw() # draws all the icons and button texts
        self.text_titel2.draw()
        self.text_start.draw()
        self.icon_quit.draw()

        if Inputs.mbdown and self.text_start.get_rect().collidepoint((Inputs.mx, Inputs.my)): # if a mouse button is clicked while the cursor is over a button, the scene will switch to the correct one
            Setup.reset_game()
        if Inputs.mbdown and self.icon_quit.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            Setup.running = not Setup.running

class PauseMenu():
    def __init__(self):
        self.text_continue = Surfaces.Text(Surfaces.gothic, "Continue", Setup.white, "height", Setup.h/27*3, [0, Setup.h/27*18], ["center", "top"])
        self.text_continue_b = Surfaces.Text(Surfaces.gothic, "Continue", Setup.black, "height", Setup.h/27*3, [0, Setup.h/27*18], ["center", "top"])

        self.text_main_menu = Surfaces.Text(Surfaces.gothic, "Main Menu", Setup.white, "height", Setup.h/27*3, [0, Setup.h/27*22], ["center", "top"])
        self.text_main_menu_b = Surfaces.Text(Surfaces.gothic, "Main Menu", Setup.black, "height", Setup.h/27*3, [0, Setup.h/27*22], ["center", "top"])

        self.icon_quit = Surfaces.Image(r'assets\quit.png', "height", Setup.h/27*3, [Setup.h/27, Setup.h/27], ["right", "bottom"]) # quit game icon in the main menu
        self.icon_quit_b = Surfaces.Image(r'assets\quit_black.png', "height", Setup.h/27*3, [Setup.h/27, Setup.h/27], ["right", "bottom"])

        self.button_pause = pygame.Rect(Setup.h/27, Setup.h/27, Setup.h/27*3, Setup.h/27*3) # the pause button in game
        self.icon_pause_l = pygame.Rect(Setup.h/27/5*8, Setup.h/27/5*8, Setup.h/27/5*3, Setup.h/27/5*3*3)
        self.icon_pause_r = pygame.Rect(Setup.h/27/5*14, Setup.h/27/5*8, Setup.h/27/5*3, Setup.h/27/5*3*3)

    def button(self):
        pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.button_pause)

        if self.button_pause.collidepoint(Inputs.mx, Inputs.my):
            pygame.draw.rect(Setup.screen, Setup.gray, self.button_pause) # when the mouse is hovering over the button, it will light up in the midtone (gray)

            if Inputs.mbdown:
                Setup.scene = 4

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.icon_pause_l)
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.icon_pause_r)

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_pause, 2) # the button is outlined in the opposite of the background color

    def update(self):
        Setup.screen.fill(Setup.gray)

        pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.text_continue.get_rect()) # makes all button backgrounds black
        pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.text_main_menu.get_rect())
        pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.icon_quit.get_rect())

        if self.text_continue.get_rect().collidepoint((Inputs.mx, Inputs.my)): # if the cursor is hovering over one of the buttons, it will light up gray
            pygame.draw.rect(Setup.screen, Setup.gray, self.text_continue.get_rect())
        if self.text_main_menu.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            pygame.draw.rect(Setup.screen, Setup.gray, self.text_main_menu.get_rect())
        if self.icon_quit.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            pygame.draw.rect(Setup.screen, Setup.gray, self.icon_quit.get_rect())

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.text_continue.get_rect(), 2) # draws the outlines of all three buttons in the object color
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.text_main_menu.get_rect(), 2)
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.icon_quit.get_rect(), 2)

        if Setup.color_theme == Setup.dark_theme:
            self.text_continue.draw()
            self.text_main_menu.draw()
            self.icon_quit.draw()

        elif Setup.color_theme == Setup.light_theme:
            self.text_continue_b.draw()
            self.text_main_menu_b.draw()
            self.icon_quit_b.draw()

        if Inputs.mbdown and self.text_continue.get_rect().collidepoint((Inputs.mx, Inputs.my)): # if a mouse button is clicked while the cursor is over a button, the scene will switch to the correct one
            Setup.scene = 1
        if Inputs.mbdown and self.text_main_menu.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            Setup.scene = 0
        if Inputs.mbdown and self.icon_quit.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            Setup.running = not Setup.running
        
class EndScreen():
    def __init__(self):
        self.text_main_menu = Surfaces.Text(Surfaces.gothic, "Main Menu", Setup.white, "height", Setup.h/27*3, [0, Setup.h/27*18], ["center", "top"])
        self.icon_quit = Surfaces.Image(r'assets\quit.png', "height", Setup.h/27*3, [Setup.h/27, Setup.h/27], ["right", "bottom"]) # quit game icon in the main menu

        self.text_your_time_is_up = Surfaces.Text(Surfaces.gothic, "your time is up!", Setup.white, "width", Setup.w/8*6, [0, Setup.h/27*7], ["center", "top"])
        self.text_you_did_it = Surfaces.Text(Surfaces.gothic, "you did it!", Setup.white, "width", Setup.w/8*6, [0, Setup.h/27*7], ["center", "top"])

    def update(self, won):
        if self.text_main_menu.get_rect().collidepoint((Inputs.mx, Inputs.my)): #if the mouse is hovering over a button, it lights up gray
            pygame.draw.rect(Setup.screen, Setup.gray, self.text_main_menu.get_rect())
        if self.icon_quit.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            pygame.draw.rect(Setup.screen, Setup.gray, self.icon_quit.get_rect())

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.text_main_menu.get_rect(), 2) # draws the outlines of all three buttons in white
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.icon_quit.get_rect(), 2)

        if won == True:
            self.text_you_did_it.draw()

            Setup.timer.draw()

        elif won == False:
            self.text_your_time_is_up.draw()

        self.text_main_menu.draw()
        self.icon_quit.draw()

        if Inputs.mbdown and self.text_main_menu.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            Setup.scene = 0
        if Inputs.mbdown and self.icon_quit.get_rect().collidepoint((Inputs.mx, Inputs.my)):
            Setup.running = not Setup.running
