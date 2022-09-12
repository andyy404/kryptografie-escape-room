import pygame, Setup

class Room():
    def __init__(self, object_list):

        self.drawing_list = []

        for obj in object_list:
            self.drawing_list.append(obj.return_drawing())

    def draw_lines(self):
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], (Setup.w/50*10, Setup.h/50*10, Setup.w/50*10*3, Setup.h/50*10*3), 2)

        pygame.draw.line(Setup.screen, Setup.color_theme[1], (0, 0), (Setup.w/50*10, Setup.h/50*10), 2)
        pygame.draw.line(Setup.screen, Setup.color_theme[1], (Setup.w, 0), (Setup.w/50*10*4,  Setup.h/50*10), 2)
        pygame.draw.line(Setup.screen, Setup.color_theme[1], (0, Setup.h), (Setup.w/50*10, Setup.h/50*10*4), 2)
        pygame.draw.line(Setup.screen, Setup.color_theme[1], (Setup.w, Setup.h), (Setup.w/50*10*4, Setup.h/50*10*4), 2)

    def draw_objects(self):
        for object_drawing in self.drawing_list:
                pygame.draw.polygon(Setup.screen, Setup.color_theme[0], object_drawing[0])
                pygame.draw.polygon(Setup.screen, Setup.color_theme[1], object_drawing[0], 2)
                pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, object_drawing[1], 2)