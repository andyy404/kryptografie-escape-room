import Setup

class Object():
    def __init__(self, position):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right

        self.w50 = Setup.w/50
        self.h50 = Setup.h/50

        self.pos5 = self.position*self.w50*5
        self.pos6 = self.position*self.w50*6

    def return_drawing(self):     
        return [self.polygon, self.lines]


class Shelf(Object):
    '''(shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position, shelf_type = 0):
        super().__init__(position)
        self.type = shelf_type
        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        if self.position <= 2:
            self.polygon = [
                    (self.w50*7 + self.pos6, self.h50*19),
                    (self.w50*13 + self.pos6, self.h50*19),
                    (self.w50*15 + self.pos5, self.h50*20),
                    (self.w50*15 + self.pos5, self.h50*40),
                    (self.w50*13 + self.pos6, self.h50*43),
                    (self.w50*7 + self.pos6, self.h50*43)
                ]

        else:
            self.polygon = [
                (self.w50*10 + self.pos5, self.h50*20),
                (self.w50*7 + self.pos6, self.h50*19),
                (self.w50*13 + self.pos6, self.h50*19),
                (self.w50*13 + self.pos6, self.h50*43),
                (self.w50*7 + self.pos6, self.h50*43),
                (self.w50*10 + self.pos5, self.h50*40)
            ]


        if self.type == 1:
            self.added_points = [
                (self.w50*7.5 + self.pos6, self.h50*31),
                (self.w50*7.25 + self.pos6, self.h50*30),
                (self.w50*10.25 + self.pos6, self.h50*29.25),
                (self.w50*10.75 + self.pos6, self.h50*28),
                (self.w50*11.75 + self.pos6, self.h50*27.75),
                (self.w50*12.5 + self.pos6, self.h50*30.75),
                (self.w50*11.5 + self.pos6, self.h50*31),
                (self.w50*10.5 + self.pos6, self.h50*30.25),
                (self.w50*10.75 + self.pos6, self.h50*30),
                (self.w50*11.25 + self.pos6, self.h50*29.75),
                (self.w50*11 + self.pos6, self.h50*29.25),
                (self.w50*10.5 + self.pos6, self.h50*29.5),
                (self.w50*10.75 + self.pos6, self.h50*30),
                (self.w50*10.5 + self.pos6, self.h50*30.25),
                (self.w50*7.5 + self.pos6, self.h50*31)
            ]
            
        if self.type == 2:
            self.added_points = [
                (self.w50*8.5 + self.pos6, self.h50*31),
                (self.w50*8.25 + self.pos6, self.h50*30.75),
                (self.w50*8.5 + self.pos6, self.h50*30.5),
                (self.w50*9 + self.pos6, self.h50*30.5),
                (self.w50*9 + self.pos6, self.h50*30),
                (self.w50*8.5 + self.pos6, self.h50*30),
                (self.w50*8.5 + self.pos6, self.h50*30.5),
                (self.w50*8.25 + self.pos6, self.h50*30.75),
                (self.w50*8 + self.pos6, self.h50*30.5),
                (self.w50*8 + self.pos6, self.h50*30),
                (self.w50*8.5 + self.pos6, self.h50*29.5),
                (self.w50*9 + self.pos6, self.h50*29.5),
                (self.w50*9.5 + self.pos6, self.h50*30),
                (self.w50*12 + self.pos6, self.h50*30),
                (self.w50*12 + self.pos6, self.h50*30.5),
                (self.w50*11.75 + self.pos6, self.h50*31),
                (self.w50*11.5 + self.pos6, self.h50*30.75),
                (self.w50*11.25 + self.pos6, self.h50*30.75),
                (self.w50*11 + self.pos6, self.h50*30.5),
                (self.w50*10.75 + self.pos6, self.h50*31),
                (self.w50*10.5 + self.pos6, self.h50*30.5),
                (self.w50*10.25 + self.pos6, self.h50*30.75),
                (self.w50*10 + self.pos6, self.h50*30.5),
                (self.w50*9.5 + self.pos6, self.h50*30.5),
                (self.w50*9 + self.pos6, self.h50*31),
                (self.w50*8.5 + self.pos6, self.h50*31)
            ]


        self.lines = [
            (self.w50*13 + self.pos6, self.h50*43),
            (self.w50*7 + self.pos6, self.h50*43),
            (self.w50*8 + self.pos6, self.h50*43),
            (self.w50*8 + self.pos6, self.h50*39),
            (self.w50*9 + self.pos6, self.h50*39),
            (self.w50*9 + self.pos6, self.h50*43),
            (self.w50*9 + self.pos6, self.h50*40),
            (self.w50*10 + self.pos6, self.h50*40),
            (self.w50*10 + self.pos6, self.h50*43),
            (self.w50*10 + self.pos6, self.h50*38),
            (self.w50*12 + self.pos6, self.h50*38),
            (self.w50*12 + self.pos6, self.h50*43),
            (self.w50*12 + self.pos6, self.h50*39),
            (self.w50*13 + self.pos6, self.h50*39),
            (self.w50*13 + self.pos6, self.h50*43), # 14

            (self.w50*13 + self.pos6, self.h50*37),
            (self.w50*7 + self.pos6, self.h50*37),
            (self.w50*7 + self.pos6, self.h50*32),
            (self.w50*9 + self.pos6, self.h50*32),
            (self.w50*9 + self.pos6, self.h50*37),
            (self.w50*9 + self.pos6, self.h50*33),
            (self.w50*10 + self.pos6, self.h50*33),
            (self.w50*10 + self.pos6, self.h50*37),
            (self.w50*10 + self.pos6, self.h50*34),
            (self.w50*11 + self.pos6, self.h50*34),
            (self.w50*11 + self.pos6, self.h50*37),
            (self.w50*11 + self.pos6, self.h50*32),
            (self.w50*12 + self.pos6, self.h50*32),
            (self.w50*12 + self.pos6, self.h50*37),
            (self.w50*12 + self.pos6, self.h50*33),
            (self.w50*13 + self.pos6, self.h50*33),
            (self.w50*13 + self.pos6, self.h50*37),

            (self.w50*13 + self.pos6, self.h50*31),
            (self.w50*7 + self.pos6, self.h50*31),
            (self.w50*7 + self.pos6, self.h50*28),  # 34
            (self.w50*8 + self.pos6, self.h50*28),  #
            (self.w50*8 + self.pos6, self.h50*31),  # 36
            (self.w50*8 + self.pos6, self.h50*27),  #
            (self.w50*10 + self.pos6, self.h50*27), #
            (self.w50*10 + self.pos6, self.h50*31), # 39
            (self.w50*10 + self.pos6, self.h50*26), #
            (self.w50*11 + self.pos6, self.h50*26), #
            (self.w50*11 + self.pos6, self.h50*31), # 42
            (self.w50*11 + self.pos6, self.h50*28), #
            (self.w50*12 + self.pos6, self.h50*28), #
            (self.w50*12 + self.pos6, self.h50*31), # 45
            (self.w50*12 + self.pos6, self.h50*26), #
            (self.w50*13 + self.pos6, self.h50*26), # 47
            (self.w50*13 + self.pos6, self.h50*31),

            (self.w50*13 + self.pos6, self.h50*25),
            (self.w50*7 + self.pos6, self.h50*25),
            (self.w50*7 + self.pos6, self.h50*20),
            (self.w50*9 + self.pos6, self.h50*20),
            (self.w50*9 + self.pos6, self.h50*25),
            (self.w50*9 + self.pos6, self.h50*22),
            (self.w50*10 + self.pos6, self.h50*22),
            (self.w50*10 + self.pos6, self.h50*25),
            (self.w50*10 + self.pos6, self.h50*20),
            (self.w50*12 + self.pos6, self.h50*20),
            (self.w50*12 + self.pos6, self.h50*25),
            (self.w50*12 + self.pos6, self.h50*21),
            (self.w50*13 + self.pos6, self.h50*21),
            (self.w50*13 + self.pos6, self.h50*25),

            (self.w50*13 + self.pos6, self.h50*19),
            (self.w50*7 + self.pos6, self.h50*19),
            (self.w50*7 + self.pos6, self.h50*43)
        ]

        if self.type > 0:
            for i in range(34, 48):
                self.lines.pop(34)
            for point in self.added_points:
                self.lines.insert(34, point)


class Desk(Object):
    '''(desk_type = 0 is empty; desk_type = 1 has some papers with a hidden message; desk_type = 2 has a caesar cipher wheel; desk_type = 3 has a tabula recta; desk_type = 4 has a whole computer'''
    def __init__(self, position, desk_type = 0):
        super().__init__(position)
        self.type = desk_type
        self.state = True # for type = 2 (if True, the cipher wheel is still on the desk, if False then not)

        if self.position <= 2:
            self.polygon = [
                (self.w50*7 + self.pos6, self.h50*31),
                (self.w50*10 + self.pos5, self.h50*30),
                (self.w50*15 + self.pos5, self.h50*30),
                (self.w50*15 + self.pos5, self.h50*40),
                (self.w50*13 + self.pos6, self.h50*43),
                (self.w50*12 + self.pos6, self.h50*43),
                (self.w50*12 + self.pos6, self.h50*32),
                (self.w50*11 + self.pos5, self.h50*32),
                (self.w50*11 + self.pos5, self.h50*40),
                (self.w50*8 + self.pos6, self.h50*43),
                (self.w50*7 + self.pos6, self.h50*43)
            ]

        else:
            self.polygon = [
                (self.w50*10 + self.pos5, self.h50*30),
                (self.w50*15 + self.pos5, self.h50*30),
                (self.w50*13 + self.pos6, self.h50*31),
                (self.w50*13 + self.pos6, self.h50*43),
                (self.w50*12 + self.pos6, self.h50*43),
                (self.w50*14 + self.pos5, self.h50*40),
                (self.w50*14 + self.pos5, self.h50*32),
                (self.w50*8 + self.pos6, self.h50*32),
                (self.w50*8 + self.pos6, self.h50*43),
                (self.w50*7 + self.pos6, self.h50*43),
                (self.w50*10 + self.pos5, self.h50*40)
            ]


        if self.type == 1:
            self.added_points = [
                (self.w50*9.75 + self.pos6, self.h50*31),
                (self.w50*10.75 + self.pos6, self.h50*30.75),
                (self.w50*10 + self.pos6, self.h50*30),
                (self.w50*9 + self.pos6, self.h50*30.25),
                (self.w50*9.75 + self.pos6, self.h50*31),
                (self.w50*10.75 + self.pos6, self.h50*30.75),
                (self.w50*9.5 + self.pos6, self.h50*30.75),
                (self.w50*10.5 + self.pos6, self.h50*30.5), #
                (self.w50*8.25 + self.pos6, self.h50*30.5),
                (self.w50*10.25 + self.pos6, self.h50*30.25),
                (self.w50*9 + self.pos6, self.h50*30.25),
                (self.w50*9.75 + self.pos6, self.h50*31)
            ]

        if self.type == 2:
            self.added_points = [
                (self.w50*10 + self.pos6, self.h50*31),
                (self.w50*10 + self.pos6, self.h50*30.75),
                (self.w50*10.25 + self.pos6, self.h50*30.5),
                (self.w50*10 + self.pos6, self.h50*30.25),
                (self.w50*9.75 + self.pos6, self.h50*30.5),
                (self.w50*10 + self.pos6, self.h50*30.75),
                (self.w50*10 + self.pos6, self.h50*31),
                (self.w50*10.5 + self.pos6, self.h50*30.75),
                (self.w50*10.5 + self.pos6, self.h50*30.25),
                (self.w50*10 + self.pos6, self.h50*30),
                (self.w50*9.5 + self.pos6, self.h50*30.25),
                (self.w50*9.5 + self.pos6, self.h50*30.75),
                (self.w50*10 + self.pos6, self.h50*31)
            ]

        if self.type == 3:
            self.added_points = [
                (self.w50*10.25 + self.pos6, self.h50*31),
                (self.w50*11 + self.pos6, self.h50*30.25),
                (self.w50*10 + self.pos6, self.h50*30),
                (self.w50*9.75 + self.pos6, self.h50*30.25),
                (self.w50*10.75 + self.pos6, self.h50*30.5),
                (self.w50*9.75 + self.pos6, self.h50*30.25),
                (self.w50*9.5 + self.pos6, self.h50*30.5),
                (self.w50*10.5 + self.pos6, self.h50*30.75),
                (self.w50*9.5 + self.pos6, self.h50*30.5),
                (self.w50*9.25 + self.pos6, self.h50*30.75),
                (self.w50*10.25 + self.pos6, self.h50*31)
            ]

        if self.type == 4:
            self.added_points = [
                (self.w50*10 + self.pos5, self.h50*30),
                (self.w50*13.5 + self.pos5, self.h50*30),
                (self.w50*13.5 + self.pos5, self.h50*29.75),
                (self.w50*13 + self.pos5, self.h50*29.75),
                (self.w50*12.75 + self.pos5, self.h50*28.75),
                (self.w50*14.75 + self.pos5, self.h50*28.75),
                (self.w50*14.75 + self.pos5, self.h50*25.25),
                (self.w50*10.25 + self.pos5, self.h50*25.25),
                (self.w50*10.25 + self.pos5, self.h50*28.75),
                (self.w50*10.5 + self.pos5, self.h50*28.75),
                (self.w50*10.5 + self.pos5, self.h50*25.5),
                (self.w50*14.5 + self.pos5, self.h50*25.5),
                (self.w50*14.5 + self.pos5, self.h50*28.75),
                (self.w50*14.25 + self.pos5, self.h50*28.5),
                (self.w50*14.25 + self.pos5, self.h50*28.75),
                (self.w50*14.5 + self.pos5, self.h50*28.5),
                (self.w50*10.5 + self.pos5, self.h50*28.5),
                (self.w50*10.5 + self.pos5, self.h50*29.5),
                (self.w50*11.5 + self.pos5, self.h50*29.5),
                (self.w50*11.5 + self.pos5, self.h50*28.5),
                (self.w50*11.5 + self.pos5, self.h50*28.75),
                (self.w50*12.75 + self.pos5, self.h50*28.75),
                (self.w50*12.25 + self.pos5, self.h50*28.75),
                (self.w50*12.5 + self.pos5, self.h50*29.75),
                (self.w50*13 + self.pos5, self.h50*29.75),
                (self.w50*11.5 + self.pos5, self.h50*29.75),
                (self.w50*11.5 + self.pos5, self.h50*30),
                (self.w50*10 + self.pos5, self.h50*30),
                (self.w50*7 + self.pos6, self.h50*31)
            ]
        

        self.lines = [
            (self.w50*10 + self.pos5, self.h50*30),
            (self.w50*7 + self.pos6, self.h50*31),
            (self.w50*7 + self.pos6, self.h50*43),
            (self.w50*7 + self.pos6, self.h50*31),
            (self.w50*13 + self.pos6, self.h50*31),
            (self.w50*15 + self.pos5, self.h50*30),
            (self.w50*13 + self.pos6, self.h50*31),
            (self.w50*13 + self.pos6, self.h50*43),
            (self.w50*12 + self.pos6, self.h50*43),
            (self.w50*12 + self.pos6, self.h50*32),
            (self.w50*8 + self.pos6, self.h50*32),
            (self.w50*8 + self.pos6, self.h50*43)
        ]
        
        if self.type > 0:
            for point in self.added_points:
                self.lines.insert(4, point)


class Door(Object):
    '''(door_type = 0 has a keypad with numbers; door_type = 1 has a keyboard)'''
    def __init__(self, position, door_type):
        super().__init__(position)
        self.type = door_type
        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        self.polygon = [
            (self.w50*10 + self.pos5, self.h50*20),
            (self.w50*15 + self.pos5, self.h50*20),
            (self.w50*15 + self.pos5, self.h50*40),
            (self.w50*10 + self.pos5, self.h50*40)
        ]

        self.lines = [
            (self.w50*11 + self.pos5, self.h50*29),
            (self.w50*12 + self.pos5, self.h50*29),
            (self.w50*12 + self.pos5, self.h50*31),
            (self.w50*11 + self.pos5, self.h50*31),
            (self.w50*11 + self.pos5, self.h50*29)
        ]


class Lamp(Object):
    '''a shelf for decoration. (shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position):
        super().__init__(position)
        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)


        self.polygon = [
            (self.w50*11 + self.pos5, self.h50*40),
            (self.w50*12 + self.pos5, self.h50*38),
            (self.w50*12.5 + self.pos5, self.h50*31),
            (self.w50*12 + self.pos5, self.h50*24),
            (self.w50*11 + self.pos5, self.h50*24),
            (self.w50*12 + self.pos5, self.h50*20),
            (self.w50*13 + self.pos5, self.h50*20),
            (self.w50*14 + self.pos5, self.h50*24),
            (self.w50*13 + self.pos5, self.h50*24),
            (self.w50*12.5 + self.pos5, self.h50*31),
            (self.w50*13 + self.pos5, self.h50*38),
            (self.w50*14 + self.pos5, self.h50*40)
        ]

        self.lines = [
            (self.w50*12 + self.pos5, self.h50*38),
            (self.w50*13 + self.pos5, self.h50*38),
            (self.w50*12 + self.pos5, self.h50*24),
            (self.w50*13 + self.pos5, self.h50*24)
        ]


class Calendar(Object):
    '''a shelf for decoration. (shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position):
        super().__init__(position)

        self.polygon = [
            (self.w50*11 + self.pos5, self.h50*26),
            (self.w50*14 + self.pos5, self.h50*26),
            (self.w50*14 + self.pos5, self.h50*29),
            (self.w50*11 + self.pos5, self.h50*29)
        ]

        self.lines = [
            (self.w50*12 + self.pos5, self.h50*26),
            (self.w50*12 + self.pos5, self.h50*29),
            (self.w50*13 + self.pos5, self.h50*29),
            (self.w50*13 + self.pos5, self.h50*26)
        ]
