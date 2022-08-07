import objects, random, pygame
from pygame.locals import *

mapping = []

class Room():
    def __init__(self, objectlist, code):
        self.objectlist = objectlist
        self.code = code

        # CALCULATE THE DIFFERENT VIEWS
        # view 0
        for obj in objectlist:
            if obj[1] <= 1:
                pass                

        # view 1
        for obj in objectlist:
            if obj[0] >= 3:
                pass

        # view 2
        for obj in objectlist:
            if obj[1] >= 3:
                pass

        # view 3
        for obj in objectlist:
            if obj[0] <= 1:
                pass

        self.draw_list = [[], [], [], []]

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
            objects.Lamp(4, 1),
            objects.Desk(0, 0),
            objects.Desk(0, 1, 1),
            objects.Door(2, 0, self.code),
            objects.Shelf(2, 4),
            objects.Keypad(3, 0, self.code),
            objects.Shelf(3, 4),
            objects.Shelf(4, 4, 1)]

        super().__init__(self.objectlist, self.code)