import pygame, Setup, Inputs

class Room():
    def __init__(self, object_list):
        self.object_list = object_list
        
        self.interaction_screen_list = []
        self.active_interaction_screen = None

        self.uv_drawing_list = []
        self.active_uv_drawing = None

        for obj in reversed(object_list):
            self.interaction_screen_list.append(obj.interaction_screen)

            try:
                obj.uv_drawing()
            except:
                self.uv_drawing_list.append(None)
            else:
                self.uv_drawing_list.append(obj.uv_drawing)

    def draw_lines(self):
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], (Setup.w/50*10, Setup.h/50*10, Setup.w/50*10*3, Setup.h/50*10*3), 2)

        pygame.draw.line(Setup.screen, Setup.color_theme[1], (0, 0), (Setup.w/50*10, Setup.h/50*10), 2)
        pygame.draw.line(Setup.screen, Setup.color_theme[1], (Setup.w, 0), (Setup.w/50*10*4,  Setup.h/50*10), 2)
        pygame.draw.line(Setup.screen, Setup.color_theme[1], (0, Setup.h), (Setup.w/50*10, Setup.h/50*10*4), 2)
        pygame.draw.line(Setup.screen, Setup.color_theme[1], (Setup.w, Setup.h), (Setup.w/50*10*4, Setup.h/50*10*4), 2)

    def draw_objects(self):
        for obj in self.object_list:
            obj.draw()

    def draw_uv_things(self):
        if self.active_uv_drawing != None:
            self.active_uv_drawing()

    def check_hitboxes(self):
        for i, obj in enumerate(reversed(self.object_list)):
            if obj.return_hitbox().collidepoint(Inputs.mx, Inputs.my) and Inputs.mbdown and Setup.timer.time < Setup.default_timer_time:
                
                self.active_interaction_screen = self.interaction_screen_list[i]
                self.active_uv_drawing = self.uv_drawing_list[i]

                Setup.scene = 6