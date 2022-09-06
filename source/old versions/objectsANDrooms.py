# this file contains the 


import pygame, random, main, varANDfunc
from pygame.locals import *
pygame.init()


#! OBJECTS --------------------------------------------------------------------------------------------------------------------
class Shelf():
    '''a shelf for decoration. (deco_type = 0 is full with books; deco_type = 1 has a UV flashlight which you can pick up'''
    def __init__(self, position, deco_type = 0):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.type = deco_type # normal shelf with books (0), shelf with uv lamp from room 1 (1), shelf with key from room 3 (2)
    
    def interaction(self):
        if self.type > 0:
            pass

    def return_drawing():
        pass

class Desk():
    '''just a standard desk'''
    def __init__(self, position, shelf_type = 0):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.type = shelf_type # 2 digit number (first digit says which desk part it is (left (0), middle (1), left (2)); second digit says what's on the desk(hhh (1), zzz (2), ))

    def interaction():
        pass

    def return_drawing():
        pass

class Door():
    '''where you enter the code to open the door'''
    def __init__(self, position, door_type, code):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.type = door_type 
        self.code = code
    
    def interaction():
        pass

    def return_drawing():
        pass

class Lamp():
    '''a normal lamp that can be switched on (state = True) and off (state = False)'''
    def __init__(self, position):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right
        self.state = True # True = on; False = off
        
    def interaction(self):
        self.state = not self.state
        if varANDfunc.color_theme == varANDfunc.light_theme:
            varANDfunc.color_theme = varANDfunc.dark_theme
        else:
            varANDfunc.color_theme = varANDfunc.light_theme

    def return_drawing():
        pass

class Calendar():
    '''a calendar that hangs on the wall and may or may not contain an encrypted message'''
    def __init__(self, position):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right

    def interaction():
        pass

    def return_drawing():
        pass

#! ROOMS ----------------------------------------------------------------------------------------------------------------------
class Room():
    def __init__(self, drawing_list, code):
        self.drawing_list = drawing_list
        self.code = code

    def return_list(self):
        return self.draw_list

    def turn_right(self):
        global looking_at_wall
        looking_at_wall = (looking_at_wall + 1) % 4

    def turn_left(self):
        global looking_at_wall
        looking_at_wall = (looking_at_wall - 1) % 4 

    def draw(self):
        pygame.draw.polygon(varANDfunc.screen, varANDfunc.color_theme[0], self.drawing_list[0])

    def draw_uv_stuff(self): # needs to be seperate from render() because this needs to be drawn after the uv light and the objects need to be drawn before
        pass #draws everything uv reactive in red with the special flag sub

class Room1(Room):
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.objectlist = [ #? #FIXME add all the right parameters to these objects
            Shelf(0),
            Door(5, self.code),
            Shelf(1),
            Lamp(4),
            Desk(2),
            Desk(3)]

        for obj in self.object_list:
            self.drawing_list.append(obj.return_drawing())

        super().__init__(self.drawing_list, self.code)

class Room2(Room):
    def __init__(self):
        self.code = random.choice(main.words_list)
        self.key = random.choice(main.words_list)

        self.objectlist = [ #? #FIXME add all the right parameters to these objects
            Door(0, self.code),
            Shelf(5),
            Lamp(1),
            Desk(4),
            Calendar(2),
            Desk(3)]

        for obj in self.object_list:
            self.drawing_list.append(obj.return_drawing())

        super().__init__(self.drawing_list, self.code)

class Room3(Room):
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.objectlist = [ #? #FIXME add all the right parameters to these objects
            Desk(0),
            Shelf(5),
            Desk(1),
            Shelf(4),
            Door(2),
            Lamp(3)]

        for obj in self.object_list:
            self.drawing_list.append(obj.return_drawing())

        super().__init__(self.drawing_list, self.code)