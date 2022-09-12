import pygame, Setup

class Timer():
    def __init__(self, starting_time):
        self.running = False
        self.time = starting_time

        self.coord_upper = int(Setup.h/27*1.5)
        self.coord_middle = int(Setup.h/27*2.5)
        self.coord_lower = int(Setup.h/27*3.5)

        self.coord_left = int(Setup.w/2 - Setup.h/27*3)
        self.coord_right = int(Setup.w/2 - Setup.h/27*2)

        self.draw_functions = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]

        self.rect = pygame.Rect(Setup.w/2-Setup.h/27*3.5, Setup.h/27, Setup.h/27*7, Setup.h/27*3) # the rectangle around the in game timer
        self.point_upper = pygame.Rect(Setup.w/2-2, Setup.h/27*2-2, 4, 4)
        self.point_lower = pygame.Rect(Setup.w/2-2, Setup.h/27*3-2, 4, 4)  

    def zero(self, modifier):

        pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_lower),
            (self.coord_left + modifier, self.coord_lower)), 4)

    def one(self, modifier):

        pygame.draw.line(Setup.screen, Setup.color_theme[1], (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_lower), 4)

    def two(self, modifier):

        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, ((self.coord_left + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_left + modifier, self.coord_middle),
            (self.coord_left + modifier, self.coord_lower),
            (self.coord_right + modifier, self.coord_lower)), 4)

    def three(self, modifier):

        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, (
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_left + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_lower),
            (self.coord_left + modifier, self.coord_lower)), 4)

    def four(self, modifier):

        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, (
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_left + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_lower)), 4)

    def five(self, modifier):

        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, (
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_left + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_lower),
            (self.coord_left + modifier, self.coord_lower)), 4)

    def six(self, modifier):

        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, (
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_left + modifier, self.coord_lower),
            (self.coord_right + modifier, self.coord_lower),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_left + modifier, self.coord_middle)), 4)

    def seven(self, modifier):

        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, (
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_lower)), 4)

    def eight(self, modifier, color = Setup.color_theme[1], thickness = 4):

        pygame.draw.lines(Setup.screen, color, True, (
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_left + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_right + modifier, self.coord_lower),
            (self.coord_left + modifier, self.coord_lower)), thickness)

    def nine(self, modifier):
        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, (
            (self.coord_right + modifier, self.coord_middle),
            (self.coord_left + modifier, self.coord_middle),
            (self.coord_left + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_upper),
            (self.coord_right + modifier, self.coord_lower),
            (self.coord_left + modifier, self.coord_lower)), 4)
    
    def draw(self):
        pygame.draw.rect(Setup.screen, Setup.color_theme[0], self.rect)
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.rect, 2)

        for i, time in enumerate(self.times_list):
            if i <= 1:
                modifier = int(i * Setup.h/27*1.5)
            else:
                modifier = int(i * Setup.h/27*1.5 + Setup.h/27*0.5)

            self.eight(modifier, Setup.color_theme[2], 4)
            self.draw_functions[time](modifier)

        if (((self.time - self.time % 30) / 30) % 60) % 2 == 0:
            pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.point_upper)
            pygame.draw.rect(Setup.screen, Setup.color_theme[1], self.point_lower)

    def update(self):
        seconds = ((self.time - self.time % 60) / 60) % 60
        single_seconds = seconds % 10
        ten_seconds = (seconds - seconds % 10) / 10

        minutes = (((self.time - self.time % 60) / 60) - seconds) / 60
        single_minutes = minutes % 10
        ten_minutes = (minutes - minutes % 10) / 10

        self.times_list = [int(ten_minutes), int(single_minutes), int(ten_seconds), int(single_seconds)]

        self.draw()

        if self.running:
            self.time -= 1
