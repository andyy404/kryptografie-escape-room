import pygame, Setup, Inputs

class MainMenu():
    def __init__(self):
        self.text_titel = pygame.transform.scale(pygame.image.load(r'assets\titel.png'), (int(Setup.w/8*6), int(Setup.w/8*6/2000*578))) # title in the main menu
        self.icon_quit = pygame.transform.scale(pygame.image.load(r'assets\quit.png'), (int(Setup.h/27*3), int(Setup.h/27*3))) # quit game icon in the main menu
        self.text_start = pygame.transform.scale(pygame.image.load(r'assets\start.png'), (int(Setup.h/27*4/526*1159), int(Setup.h/27*4))) # start button text icon in the main menu

        self.button_play = pygame.Rect(Setup.w/2-Setup.w/8, Setup.h/27*17, Setup.w/4, Setup.h/27*4) # main menu button to start game
        self.button_quit = pygame.Rect(Setup.w-Setup.h/27*4, Setup.h-Setup.h/27*4, Setup.h/27*3, Setup.h/27*3) # main menu button to quit game

    def update(self):
        Setup.screen.fill(Setup.black)

        if self.button_play.collidepoint((Inputs.mx, Inputs.my)): # if the cursor is hovering over one of the buttons, it will light up gray
            pygame.draw.rect(Setup.screen, Setup.gray, self.button_play)
        if self.button_quit.collidepoint((Inputs.mx, Inputs.my)):
            pygame.draw.rect(Setup.screen, Setup.gray, self.button_quit)

        pygame.draw.rect(Setup.screen, Setup.white, self.button_play, 2) # draws the outlines of all three buttons in white
        pygame.draw.rect(Setup.screen, Setup.white, self.button_quit, 2)

        Setup.screen.blit(self.text_titel, (Setup.w/8, Setup.h/27*2)) # draws all the icons and button texts
        Setup.screen.blit(self.icon_quit, (Setup.w-Setup.h/27*4, Setup.h-Setup.h/27*4))
        Setup.screen.blit(self.text_start, (Setup.w/2-Setup.h/27*4/526*1159/2, Setup.h/27*19-Setup.h/27*4/2))

        if Inputs.mbdown and self.button_play.collidepoint((Inputs.mx, Inputs.my)): # if a mouse button is clicked while the cursor is over a button, the scene will switch to the correct one
            Setup.reset_game()
        if Inputs.mbdown and self.button_quit.collidepoint((Inputs.mx, Inputs.my)):
            Setup.running = not Setup.running

class PauseMenu():
    def __init__(self):
        self.text_continue = pygame.transform.scale(pygame.image.load(r'assets\continue.png'), (int(Setup.h/27*3/578*1944), int(Setup.h/27*3)))
        self.text_main_menu = pygame.transform.scale(pygame.image.load(r'assets\mainmenu.png'), (int(Setup.h/27*3/392*1848), int(Setup.h/27*3)))
        self.icon_quit = pygame.transform.scale(pygame.image.load(r'assets\quit.png'), (int(Setup.h/27*3), int(Setup.h/27*3))) # quit game icon in the main menu

        self.text_continue_b = pygame.transform.scale(pygame.image.load(r'assets\continue_black.png'), (int(Setup.h/27*3/578*1944), int(Setup.h/27*3)))
        self.text_main_menu_b = pygame.transform.scale(pygame.image.load(r'assets\mainmenu_black.png'), (int(Setup.h/27*3/392*1848), int(Setup.h/27*3)))
        self.icon_quit_b = pygame.transform.scale(pygame.image.load(r'assets\quit_black.png'), (int(Setup.h/27*3), int(Setup.h/27*3)))

        self.button_continue = pygame.Rect(Setup.w/2-Setup.h/27*8, Setup.h/27*18, Setup.h/27*16, Setup.h/27*3)
        self.button_main_menu = pygame.Rect(Setup.w/2-Setup.h/27*8, Setup.h/27*22, Setup.h/27*16, Setup.h/27*3)
        self.button_quit = pygame.Rect(Setup.w-Setup.h/27*4, Setup.h-Setup.h/27*4, Setup.h/27*3, Setup.h/27*3) # main menu button to quit game

        self.button_pause = pygame.Rect(Setup.h/27, Setup.h/27, Setup.h/27*3, Setup.h/27*3) # the pause button in game
        self.icon_pause_l = pygame.Rect(Setup.h/27/5*8, Setup.h/27/5*8, Setup.h/27/5*3, Setup.h/27/5*3*3)
        self.icon_pause_r = pygame.Rect(Setup.h/27/5*14, Setup.h/27/5*8, Setup.h/27/5*3, Setup.h/27/5*3*3)

    def button(self):
        pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.button_pause)

        if self.button_pause.collidepoint(Inputs.mx, Inputs.my):
            if Inputs.click:
                pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_pause) # when the the mouse is pressed down while hovering over the button, the button will light up in the opposite of the background color
            else:
                pygame.draw.rect(Setup.screen, Setup.gray, self.button_pause) # when the mouse is hovering over the button, it will light up in the midtone (gray)

            if Inputs.mbdown:
                Setup.timer.running = not Setup.timer.running

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.icon_pause_l)
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.icon_pause_r)

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_pause, 2) # the button is outlined in the opposite of the background color

    def update(self):
        if Setup.timer.running == False:
            Setup.screen.fill(Setup.gray)

            pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.button_continue) # makes all button backgrounds black
            pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.button_main_menu)
            pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.button_quit)

            if self.button_continue.collidepoint((Inputs.mx, Inputs.my)): # if the cursor is hovering over one of the buttons, it will light up gray
                pygame.draw.rect(Setup.screen, Setup.gray, self.button_continue)
            if self.button_main_menu.collidepoint((Inputs.mx, Inputs.my)):
                pygame.draw.rect(Setup.screen, Setup.gray, self.button_main_menu)
            if self.button_quit.collidepoint((Inputs.mx, Inputs.my)):
                pygame.draw.rect(Setup.screen, Setup.gray, self.button_quit)

            pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_continue, 2) # draws the outlines of all three buttons in the object color
            pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_main_menu, 2)
            pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_quit, 2)

            if Setup.color_theme == Setup.dark_theme:
                Setup.screen.blit(self.text_continue, (Setup.w/2-Setup.h/27*3/578*1944/2, Setup.h/27*18)) # draws all the icons and button texts
                Setup.screen.blit(self.text_main_menu, (Setup.w/2-Setup.h/27*3/392*1848/2, Setup.h/27*22))
                Setup.screen.blit(self.icon_quit, (Setup.w-Setup.h/27*4, Setup.h-Setup.h/27*4))

            elif Setup.color_theme == Setup.light_theme:
                Setup.screen.blit(self.text_continue_b, (Setup.w/2-Setup.h/27*3/578*1944/2, Setup.h/27*18)) # draws all the icons and button texts
                Setup.screen.blit(self.text_main_menu_b, (Setup.w/2-Setup.h/27*3/392*1848/2, Setup.h/27*22))
                Setup.screen.blit(self.icon_quit_b, (Setup.w-Setup.h/27*4, Setup.h-Setup.h/27*4))

            if Inputs.mbdown and self.button_continue.collidepoint((Inputs.mx, Inputs.my)): # if a mouse button is clicked while the cursor is over a button, the scene will switch to the correct one
                Setup.timer.running = True
            if Inputs.mbdown and self.button_main_menu.collidepoint((Inputs.mx, Inputs.my)):
                Setup.scene = 0
            if Inputs.mbdown and self.button_quit.collidepoint((Inputs.mx, Inputs.my)):
                Setup.running = not Setup.running
        
        self.button()

class EndScreen():
    def __init__(self):
        self.text_main_menu = pygame.transform.scale(pygame.image.load(r'assets\mainmenu.png'), (int(Setup.h/27*3/392*1848), int(Setup.h/27*3)))
        self.icon_quit = pygame.transform.scale(pygame.image.load(r'assets\quit.png'), (int(Setup.h/27*3), int(Setup.h/27*3))) # quit game icon in the main menu

        self.text_your_time_is_up = pygame.transform.scale(pygame.image.load(r'assets\lost.png'), (int(Setup.w/8*6), int(Setup.w/8*6/2057*350)))
        self.text_you_did_it = pygame.transform.scale(pygame.image.load(r'assets\won.png'), (int(Setup.w/8*6), int(Setup.w/8*6/1297*350)))

        self.button_main_menu = pygame.Rect(Setup.w/2-Setup.h/27*8, Setup.h/27*22, Setup.h/27*16, Setup.h/27*3)
        self.button_quit = pygame.Rect(Setup.w-Setup.h/27*4, Setup.h-Setup.h/27*4, Setup.h/27*3, Setup.h/27*3) # main menu button to quit game

    def update(self, won):
        global running, scene

        if self.button_main_menu.collidepoint((Inputs.mx, Inputs.my)): #if the mouse is hovering over a button, it lights up gray
            pygame.draw.rect(Setup.screen, Setup.gray, self.button_main_menu)
        if self.button_quit.collidepoint((Inputs.mx, Inputs.my)):
            pygame.draw.rect(Setup.screen, Setup.gray, self.button_quit)

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_main_menu, 2) # draws the outlines of all three buttons in white
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_quit, 2)

        if won == True:
            Setup.screen.blit(self.text_you_did_it, (Setup.w/8, Setup.h/27*7))

            Setup.timer.draw()

        elif won == False:
            Setup.screen.blit(self.text_your_time_is_up, (Setup.w/8, Setup.h/27*7))

        Setup.screen.blit(self.text_main_menu, (Setup.w/2-Setup.h/27*3/392*1848/2, Setup.h/27*22))
        Setup.screen.blit(self.icon_quit, (Setup.w-Setup.h/27*4, Setup.h-Setup.h/27*4))

        if Inputs.mbdown and self.button_main_menu.collidepoint((Inputs.mx, Inputs.my)):
            scene = 0
        if Inputs.mbdown and self.button_quit.collidepoint((Inputs.mx, Inputs.my)):
            running = not running
