import objects, random, pygame, main
from pygame.locals import *


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
            objects.Shelf(0),
            objects.Door(5, self.code),
            objects.Shelf(1),
            objects.Lamp(4),
            objects.DeskLeft(2),
            objects.DeskRight(3),
            
            ]

        super().__init__(self.objectlist, self.code)

class Room2(Room):
    def __init__(self):
        self.code = random.choice(main.words_list)
        self.key = random.choice(main.words_list)

        self.objectlist = [
            objects.Door(0, self.code),
            objects.Shelf(5),
            objects.Lamp(1),
            objects.DeskRight(4),
            objects.Calendar(2),
            objects.DeskLeft(3)]

        super().__init__(self.objectlist, self.code)

class Room3(Room):
    def __init__(self):
        self.code = random.randint(10000, 99999)

        self.objectlist = [
            objects.Desk(0),
            objects.Shelf(5),
            objects.Desk(1),
            objects.Shelf(4),
            objects.Door(2),
            objects.Lamp(3)]

        super().__init__(self.objectlist, self.code)