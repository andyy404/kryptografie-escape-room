import pygame, Setup, Inputs

class UVLight():
    def __init__(self):
        self.icon = pygame.transform.scale(pygame.image.load(r'assets\light.png'), (int(Setup.w/27*2), int(Setup.w/27*2))) # in game icon of the uv lamp
        self.button = pygame.Rect(Setup.w-Setup.w/27*3-Setup.w/27, Setup.h-Setup.h/27*3-Setup.w/27, Setup.w/27*2, Setup.w/27*2) # in game flashlight icon$

        self.state = 0

    def update(self):
        if self.button.collidepoint(Inputs.mx, Inputs.my) and Inputs.mbdown and self.state == 1 and Setup.timer.running: # if the uv light icon gets clicked while the player has the uv light, the light will get turned on
            self.state = 2

        if self.state == 2: # when the player is using the light
            pygame.draw.circle(Setup.screen, Setup.uv_color, (Inputs.mx, Inputs.my), Setup.h/4) #there's a circle of light around the cursor
    
            if Inputs.mbup: # if the player lets the mouse go, the light will turn off again
                self.state = 1
    
        if self.state == 1: # when the light is off, the light icon is drawn in the corner
            Setup.screen.blit(self.icon, (Setup.w-Setup.w/27*3-Setup.w/27, Setup.h-Setup.h/27*3-Setup.w/27))

class CipherWheel():
    def __init__(self):
        pass

    def update(self):
        pass