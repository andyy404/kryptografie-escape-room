import pygame
pygame.init()

class Desk():
    '''just a standard desk. (deco_type = 0 is empty; deco_type = 1 has the hidden number code from room 1)'''
    def __init__(self, x, y, deco_type = 0):
        self.x = x
        self.y = y
        self.type = deco_type

    def interaction():
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
    '''a shelf for decoration. (deco_type = 0 is full with books; deco_type = 1 has a UV torch which you can pick up'''
    def __init__(self, x, y, deco_type = 0):
        self.x = x
        self.y = y
        self.type = deco_type
    
    def interaction():
        pass

class Door():
    '''the door to leave the room. can be open (state = 1) or closed (state = 0)'''
    def __init__(self, x, y, code, opened = False):
        self.x = x
        self.y = y
        self.code = code
        self.open = opened

        return 
    
    def interaction():
        pass

class Keypad():
    '''where you enter the code to open the door'''
    def __init__(self, x, y, code):
        self.x = x
        self.y = y
        self.code = code
    
    def interaction():
        pass