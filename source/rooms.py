import objects, random, pygame
from pygame.locals import *

class Room():
    def __init__(self, objectlist, code):
        self.objectlist = objectlist
        self.code = code

        # CALCULATE THE DIFFERENT VIEWS


        return [[], [], [], []]

    def turn_right(self):
        global looking_at_wall
        looking_at_wall = (looking_at_wall + 1) % 4

    def turn_left(self):
        global looking_at_wall
        looking_at_wall = (looking_at_wall - 1) % 4 


class Room1(Room):
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.objectlist = [
            objects.Lamp(4, 1),
            objects.Desk(0, 0),
            objects.Desk(0, 1, 1),
            objects.Door(2, 0, self.code),
            objects.Shelf(2, 4),
            objects.Keypad(3, 0, self.code),
            objects.Shelf(3, 4),
            objects.Shelf(4, 4, 1)]

        super().__init__(self.objectlist, self.code)