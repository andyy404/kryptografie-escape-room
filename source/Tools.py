import pygame, Setup, Inputs, Surfaces

class UVLight():
    def __init__(self):
        self.icon = Surfaces.Image(r'assets\light.png', "width", Setup.w/27*2, [Setup.w/27, Setup.w/27], ["right", "bottom"]) # in game icon of the uv lamp

        self.state = 0
        self.light_surface = pygame.Surface((Setup.w, Setup.h))

    def update(self):
        self.light_surface.fill((0, 0, 0))

        if self.icon.get_rect().collidepoint(Inputs.mx, Inputs.my) and Inputs.mbdown and self.state == 1: # if the uv light icon gets clicked while the player has the uv light, the light will get turned on
            self.state = 2

        if self.state == 2: # when the player is using the light
            pygame.draw.circle(self.light_surface, Setup.uv_color, (Inputs.mx, Inputs.my), Setup.h/4)
            Setup.screen.blit(self.light_surface, (0, 0), None, pygame.BLEND_ADD)
    
            if Inputs.mbup: # if the player lets the mouse go, the light will turn off again
                self.state = 1
    
        if self.state == 1: # when the light is off, the light icon is drawn in the corner
            self.icon.draw()

class CipherWheel():
    def __init__(self):
        self.icon_back = Surfaces.Image(r'assets\cipher_wheel.png', "width", Setup.w/27*2, [Setup.w/27*4, Setup.w/27], ["right", "bottom"])
        self.icon_front = Surfaces.Image(r'assets\cipher_wheel.png', "width", Setup.w/27*2/7*4.5, [Setup.w/27*4 + Setup.w/27*2/7*1.25, Setup.w/27 + Setup.w/27*2/7*1.25], ["right", "bottom"])
        self.icon_gear = Surfaces.Image(r'assets\cipher_wheel_gear.png', "width", Setup.w/27*2/7, [Setup.w/27*4 + Setup.w/27*2/7*3, Setup.w/27 + Setup.w/27*2/7*3], ["right", "bottom"])

        self.back = Surfaces.Image(r'assets\cipher_wheel.png', "height", Setup.h/3*2, [0, 0], ["center", "center"])
        self.front = Surfaces.Image(r'assets\cipher_wheel.png', "height", Setup.h/3*2/7*4.5, [0, 0], ["center", "center"])
        self.gear = Surfaces.Image(r'assets\cipher_wheel_gear.png', "height", Setup.h/3*2/7, [0, 0], ["center", "center"])

        self.draw_front = self.front.img

        self.button_back = pygame.Rect(Setup.h/27, Setup.h/27, Setup.h/27*3, Setup.h/27*3) # the pause button in game
       
        self.state = 0
        self.current_angle = 0
        self.before_angle = 0
        self.changing = False

        self.comparison_vector = pygame.Vector2(0, -1)
        self.mouse_vector = pygame.Vector2(Inputs.mx-Setup.w/2, Inputs.my-Setup.h/2)

        self.midpoint_x, self.midpoint_y = Setup.w/2, Setup.h/2

    def check(self):
        if self.state == 1:
            if self.icon_back.get_rect().collidepoint(Inputs.mx, Inputs.my) and Inputs.mbdown:
                Setup.scene = 5

            self.icon_back.draw()
            self.icon_front.draw()
            self.icon_gear.draw()

    def get_angle(self):
        angle = self.mouse_vector.angle_to(self.comparison_vector)

        return angle

    def back_button(self):
        pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.button_back)

        if self.button_back.collidepoint(Inputs.mx, Inputs.my):
            if Inputs.click:
                pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_back) # when the the mouse is pressed down while hovering over the button, the button will light up in the opposite of the background color
            else:
                pygame.draw.rect(Setup.screen, Setup.gray, self.button_back) # when the mouse is hovering over the button, it will light up in the midtone (gray)

            if Inputs.mbdown:
                Setup.scene = 1

        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.button_back, 2) # the button is outlined in the opposite of 

    def update(self):
        self.mouse_vector = pygame.Vector2(Inputs.mx-Setup.w/2, Inputs.my-Setup.h/2)

        if self.mouse_vector.length() < self.front.img.get_width()/2 and Inputs.mbdown:
            self.changing = True
            self.draw_front = pygame.transform.rotate(self.front.img, self.current_angle)
            self.start_angle = self.get_angle()
            self.before_angle = self.current_angle

        if self.changing:
            self.draw_front = pygame.transform.rotate(self.front.img, self.current_angle)
            self.current_angle = (self.before_angle + self.get_angle() - self.start_angle)

            if Inputs.mbup:
                self.changing = False

        self.back.draw()
        Setup.screen.blit(self.draw_front, (Setup.w/2-self.draw_front.get_width()/2, Setup.h/2-self.draw_front.get_height()/2))
        self.gear.draw()

        self.back_button()