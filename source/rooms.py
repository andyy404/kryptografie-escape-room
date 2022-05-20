from re import I
import objects, random, pygame
from pygame.locals import *

class Room1():
    def __init__(self):
        self.code = random.randint(1000, 99999).zfill(5)

        self.objectlist = [
            objects.Lamp(4, 1),
            objects.Desk(0, 0),
            objects.Desk(0, 1, 1),
            objects.Door(2, 0, self.code),
            objects.Shelf(2, 4),
            objects.Keypad(3, 0, self.code),
            objects.Shelf(3, 4),
            objects.Shelf(4, 4, 1)]

    def check(self):
        for ev in pygame.event.get():
            if ev == MOUSEBUTTONDOWN:
                pass

    def render(self):
        pass

    def run(self):
        pass