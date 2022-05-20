import pygame, random
pygame.init()

class Object:
    '''all objects standing in the rooms'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check():
        pass  

class Desk(Object):
    '''just a standard desk. (deco_type = 0 is empty; deco_type = 1 has the hidden number code from room 1)'''

    def __init__(self, x, y, deco_type = 0):
        super().__init__(x, y)
        self.type = deco_type

class Lamp(Object):
    '''a normal lamp that can be switched on (state = 1) and off (state = 0)'''

    def __init__(self, x, y, state):
        super().__init__(x, y)
        self.state = state

class Shelf(Object):
    '''a shelf for decoration'''

    def __init__(self, x, y, deco_type = 0):
        super().__init__(x, y)
        self.type = deco_type

class Door(Object):
    '''the door to leave the room. can be open (state = 1) or closed (state = 0)'''

    def __init__(self, x, y, code, open = False):
        super().__init__(x, y)
        self.code = code

class Keypad(Object):
    '''where you enter the code to open the door'''

    def __init__(self, x, y, code):
        super().__init__(x, y)
        self.code = code