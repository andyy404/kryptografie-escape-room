import pygame, random, main, varANDfunc
from pygame.locals import *
pygame.init()


#! OBJECTS --------------------------------------------------------------------------------------------------------------------
class Desk():
    '''just a standard desk'''
    def __init__(self, position, deco_type = 0):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.type = deco_type # 2 digit number (first digit says which desk part it is left (0), middle (1), left (2); second digit says what's on the desk)
        super().__init__(self.position)

    def return_drawing():
        pass

class Lamp():
    '''a normal lamp that can be switched on (state = True) and off (state = False)'''
    def __init__(self, x, y, state = False):
        self.x = x
        self.y = y
        self.state = state
        
    def interaction(self):
        self.state = not self.state

class Shelf():
    '''a shelf for decoration. (deco_type = 0 is full with books; deco_type = 1 has a UV flashlight which you can pick up'''
    def __init__(self, x, y, deco_type = 0):
        self.x = x
        self.y = y
        self.type = deco_type
    
    def interaction():
        pass

class Door():
    '''where you enter the code to open the door'''
    def __init__(self, x, y, code):
        self.x = x
        self.y = y
        self.code = code
    
    def interaction():
        pass

class Calendar():
    def __init__(self, position, deco_type = 0):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.type = deco_type # 2 digit number (first digit says which desk part it is left (0), middle (1), left (2); second digit says what's on the desk)
        super().__init__(self.position)

    def return_drawing():
        pass

#! ROOMS ----------------------------------------------------------------------------------------------------------------------
class Room():
    def __init__(self, objectlist, code):
        self.objectlist = objectlist
        self.code = code

    def return_list(self):
        return self.draw_list

    def turn_right(self):
        global looking_at_wall
        looking_at_wall = (looking_at_wall + 1) % 4

    def turn_left(self):
        global looking_at_wall
        looking_at_wall = (looking_at_wall - 1) % 4 

    def render(self):
        pass
        

    def render_uv_stuff(self): # needs to be seperate from render() because this needs to be drawn after the uv light and the objects need to be drawn before
        pass #draws everything uv reactive in red with the special flag sub

class Room1(Room):
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.objectlist = [
            Shelf(0),
            Door(5, self.code),
            Shelf(1),
            Lamp(4),
            Desk(2),
            Desk(3)]

        for obj in self.object_list:
            self.drawing_list.append(obj.return_drawing())

        super().__init__(self.objectlist, self.code)

    def render(self):
        pygame.draw.polygon(varANDfunc.screen, varANDfunc.color_theme)

class Room2(Room):
    def __init__(self):
        self.code = random.choice(main.words_list)
        self.key = random.choice(main.words_list)

        self.objectlist = [
            Door(0, self.code),
            Shelf(5),
            Lamp(1),
            Desk(4),
            Calendar(2),
            Desk(3)]

        super().__init__(self.objectlist, self.code)

class Room3(Room):
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.objectlist = [
            Desk(0),
            Shelf(5),
            Desk(1),
            Shelf(4),
            Door(2),
            Lamp(3)]

        super().__init__(self.objectlist, self.code)