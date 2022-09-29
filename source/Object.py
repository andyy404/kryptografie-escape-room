import pygame, Setup, Inputs, Surfaces

class Object():
    def __init__(self, position):
        self.position = position # there's space for 6 objects per room and the spaces are numbered 0 to 5 from left to right

        self.w50 = Setup.w/50
        self.h50 = Setup.h/50

        self.pos5 = self.position*self.w50*5
        self.pos6 = self.position*self.w50*6

    def return_hitbox(self):
        return self.hitbox


class Shelf(Object):
    '''(shelf_type = 0 is full with books; shelf_type = 1 has a UV flashlight which you can pick up; shelf_type = 2 has a key with an engraved string of letters'''
    def __init__(self, position, shelf_type = 0, key = None):
        super().__init__(position)
        self.type = shelf_type
        self.state = True # for type = 1 (if True, the uv lamp is still on the shelf, if False then not)

        self.key = key

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

        self.hitbox = pygame.Rect(self.w50*7 + self.pos6, self.h50*19, self.w50*6, self.h50*24)

    def draw(self):
        pygame.draw.polygon(Setup.screen, Setup.color_theme[0], self.polygon)
        pygame.draw.polygon(Setup.screen, Setup.color_theme[1], self.polygon, 2)
        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, self.lines, 2)

        if self.type == 0:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
                (self.w50*7 + self.pos6, self.h50*31),
                (self.w50*7 + self.pos6, self.h50*28),
                (self.w50*8 + self.pos6, self.h50*28),
                (self.w50*8 + self.pos6, self.h50*31),
                (self.w50*8 + self.pos6, self.h50*27),
                (self.w50*10 + self.pos6, self.h50*27),
                (self.w50*10 + self.pos6, self.h50*31),
                (self.w50*10 + self.pos6, self.h50*26),
                (self.w50*11 + self.pos6, self.h50*26),
                (self.w50*11 + self.pos6, self.h50*31),
                (self.w50*11 + self.pos6, self.h50*28),
                (self.w50*12 + self.pos6, self.h50*28),
                (self.w50*12 + self.pos6, self.h50*31),
                (self.w50*12 + self.pos6, self.h50*26),
                (self.w50*13 + self.pos6, self.h50*26),
                (self.w50*13 + self.pos6, self.h50*31)
            ), 2)

        if self.type == 1 and self.state == True:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
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
                (self.w50*10.5 + self.pos6, self.h50*30.25)
            ), 2)
            
        if self.type == 2:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
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
                (self.w50*9 + self.pos6, self.h50*31)
            ), 2)

    def interaction_screen(self):
        if self.type == 0 or self.state == False:
            Setup.scene = 1
        
        else:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
                (0, Setup.h/9*2),
                (Setup.w/16*5, Setup.h/9*2),
                (Setup.w/16*5, 0),
                (Setup.w/16*5, Setup.h/9*2),
                (Setup.w/16*8, Setup.h/9*2),
                (Setup.w/16*8, 0),
                (Setup.w/16*8, Setup.h/9*2),
                (Setup.w/16*13, Setup.h/9*2),
                (Setup.w/16*13, 0),
                (Setup.w/16*13, Setup.h/9*2),
                (Setup.w, Setup.h/9*2),
                (Setup.w/16*14, Setup.h/9*3),
                (Setup.w/16*2, Setup.h/9*3),
                (Setup.w/16*14, Setup.h/9*3),
                (Setup.w/16*14, Setup.h/9*6),
                (Setup.w, Setup.h/9*7),
                (Setup.w/16*14, Setup.h/9*7),
                (Setup.w/16*14, Setup.h),
                (Setup.w/16*14, Setup.h/9*7),
                (Setup.w/16*2, Setup.h/9*7),
                (Setup.w/16*2, Setup.h),
                (Setup.w/16*2, Setup.h/9*7),
                (0, Setup.h/9*7),
                (Setup.w/16*2, Setup.h/9*6),
                (Setup.w/16*14, Setup.h/9*6),
                (Setup.w/16*2, Setup.h/9*6),
                (Setup.w/16*2, Setup.h/9*3)
            ), 2)

            if self.type == 1:
                pygame.draw.polygon(Setup.screen, Setup.color_theme[0], ( 
                    (Setup.w/16*5.5, Setup.h/9*7),
                    (Setup.w/16*8.5, Setup.h/9*6.25),
                    (Setup.w/16*9.5, Setup.h/9*7),
                    (Setup.w/16*10.5, Setup.h/9*6.75),
                    (Setup.w/16*9.75, Setup.h/9*3.75),
                    (Setup.w/16*8.75, Setup.h/9*4),
                    (Setup.w/16*8.25, Setup.h/9*5.25),
                    (Setup.w/16*5.25, Setup.h/9*6)
                ))

                pygame.draw.polygon(Setup.screen, Setup.color_theme[1], ( 
                    (Setup.w/16*5.5, Setup.h/9*7),
                    (Setup.w/16*8.5, Setup.h/9*6.25),
                    (Setup.w/16*9.5, Setup.h/9*7),
                    (Setup.w/16*10.5, Setup.h/9*6.75),
                    (Setup.w/16*9.75, Setup.h/9*3.75),
                    (Setup.w/16*8.75, Setup.h/9*4),
                    (Setup.w/16*8.25, Setup.h/9*5.25),
                    (Setup.w/16*5.25, Setup.h/9*6)
                ), 2)

                pygame.draw.polygon(Setup.screen, Setup.color_theme[1], ( 
                    (Setup.w/16*8.75, Setup.h/9*6),
                    (Setup.w/16*9.25, Setup.h/9*5.75),
                    (Setup.w/16*9, Setup.h/9*5.25),
                    (Setup.w/16*8.5, Setup.h/9*5.5)
                ), 2)

                if pygame.Rect(Setup.w/16*5.25, Setup.h/9*3.75, Setup.w/16*5.25, Setup.h/9*3.25).collidepoint(Inputs.mx, Inputs.my) and Inputs.mbdown:
                    self.state = False
                    Setup.uv_lamp.state = 1

            if self.type == 2:
                pygame.draw.polygon(Setup.screen, Setup.color_theme[0], (
                    (Setup.w/16*5.5, Setup.h/9*7),
                    (Setup.w/16*4.5, Setup.h/9*6),
                    (Setup.w/16*4.5, Setup.h/9*5),
                    (Setup.w/16*5.5, Setup.h/9*4),
                    (Setup.w/16*6.5, Setup.h/9*4),
                    (Setup.w/16*7.5, Setup.h/9*5),
                    (Setup.w/16*12.5, Setup.h/9*5),
                    (Setup.w/16*12.5, Setup.h/9*6),
                    (Setup.w/16*12, Setup.h/9*7),
                    (Setup.w/16*11.5, Setup.h/9*6.5),
                    (Setup.w/16*11, Setup.h/9*6.5),
                    (Setup.w/16*10.5, Setup.h/9*6),
                    (Setup.w/16*10, Setup.h/9*7),
                    (Setup.w/16*9.5, Setup.h/9*6),
                    (Setup.w/16*9, Setup.h/9*6.5),
                    (Setup.w/16*8.5, Setup.h/9*6),
                    (Setup.w/16*7.5, Setup.h/9*6),
                    (Setup.w/16*6.5, Setup.h/9*7)
                ))

                pygame.draw.polygon(Setup.screen, Setup.color_theme[1], (
                    (Setup.w/16*5.5, Setup.h/9*7),
                    (Setup.w/16*4.5, Setup.h/9*6),
                    (Setup.w/16*4.5, Setup.h/9*5),
                    (Setup.w/16*5.5, Setup.h/9*4),
                    (Setup.w/16*6.5, Setup.h/9*4),
                    (Setup.w/16*7.5, Setup.h/9*5),
                    (Setup.w/16*12.5, Setup.h/9*5),
                    (Setup.w/16*12.5, Setup.h/9*6),
                    (Setup.w/16*12, Setup.h/9*7),
                    (Setup.w/16*11.5, Setup.h/9*6.5),
                    (Setup.w/16*11, Setup.h/9*6.5),
                    (Setup.w/16*10.5, Setup.h/9*6),
                    (Setup.w/16*10, Setup.h/9*7),
                    (Setup.w/16*9.5, Setup.h/9*6),
                    (Setup.w/16*9, Setup.h/9*6.5),
                    (Setup.w/16*8.5, Setup.h/9*6),
                    (Setup.w/16*7.5, Setup.h/9*6),
                    (Setup.w/16*6.5, Setup.h/9*7)
                ), 2)

                pygame.draw.polygon(Setup.screen, Setup.color_theme[1], (
                    (Setup.w/16*5.5, Setup.h/9*5),
                    (Setup.w/16*6.5, Setup.h/9*5),
                    (Setup.w/16*6.5, Setup.h/9*6),
                    (Setup.w/16*5.5, Setup.h/9*6)
                ), 2)

    def uv_drawing(self):
        if self.type == 2:
            text_key = Surfaces.UVText(Surfaces.monospace, self.key, "height", Setup.h/9/2, [Setup.w/16*7.75, Setup.h/9*5.25])
            text_key.draw(pygame.BLEND_SUB)


class Desk(Object):
    '''(desk_type = 0 is empty; desk_type = 1 has some papers with a hidden message; desk_type = 2 has a caesar cipher wheel; desk_type = 3 has a tabula recta; desk_type = 4 has a whole computer'''
    def __init__(self, position, desk_type = 0, code = None):
        super().__init__(position)
        self.type = desk_type
        self.state = True # for type = 2 (if True, the cipher wheel is still on the desk, if False then not)

        self.code = code

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
        
        self.hitbox = pygame.Rect(self.w50*7 + self.pos6, self.h50*31, self.w50*6, self.h50*12)

        if self.type == 2:
            self.cipher_wheel_back = Surfaces.Image(r'assets\cipher_wheel.png', "width", Setup.w/16*3, [Setup.w/32*15, Setup.h/18*8], ["right", "top"])
            self.cipher_wheel_front = Surfaces.Image(r'assets\cipher_wheel.png', "width", Setup.w/16*3/7*4.5, [Setup.w/32*15 + Setup.w/16*3/7*1.25, Setup.h/18*8 + Setup.w/16*3/7*1.25], ["right", "top"])
            self.cipher_wheel_gear = Surfaces.Image(r'assets\cipher_wheel_gear.png', "width", Setup.w/16*3/7, [Setup.w/32*15 + Setup.w/16*3/7*3, Setup.h/18*8 + Setup.w/16*3/7*3], ["right", "top"])

        if self.type == 3:
            self.tabula_recta = Surfaces.Image(r'assets\tabula_recta.png', "height", Setup.h/3*2, [0, Setup.h/9*2], ["center", "top"])

        if self.type == 4:
            self.input = ''

            self.keyboard = Surfaces.Image(r'assets\keyboard.png', "width", Setup.w/32*10 +4, [Setup.w/32*11, Setup.h/9*5], ["left", "top"])

            self.hitbox_qwertzuiop = pygame.Rect(Setup.w/32*11, Setup.h/9*5, self.keyboard.img.get_width(), self.keyboard.img.get_height()/3)
            self.hitbox_asdfghjkl = pygame.Rect(Setup.w/32*11, Setup.h/9*5 + self.keyboard.img.get_height()/3, self.keyboard.img.get_width(), self.keyboard.img.get_height()/3)
            self.hitbox_yxcvbnm = pygame.Rect(Setup.w/32*11, Setup.h/9*5 + self.keyboard.img.get_height()/3*2, self.keyboard.img.get_width(), self.keyboard.img.get_height()/3)

            self.hitbox_qa =  pygame.Rect(Setup.w/32*11, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_wsy = pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_edx = pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*2, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_rfc = pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*3, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_tgv = pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*4, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_zhb = pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*5, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_ujn = pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*6, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_ikm = pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*7, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_ol =  pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*8, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_p =   pygame.Rect(Setup.w/32*11 + self.keyboard.img.get_width()/10*9, Setup.h/9*5, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())

    def draw(self):
        pygame.draw.polygon(Setup.screen, Setup.color_theme[0], self.polygon)
        pygame.draw.polygon(Setup.screen, Setup.color_theme[1], self.polygon, 2)
        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, self.lines, 2)

        if self.type == 1:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
                (self.w50*9.75 + self.pos6, self.h50*31),
                (self.w50*10.75 + self.pos6, self.h50*30.75),
                (self.w50*10 + self.pos6, self.h50*30),
                (self.w50*9 + self.pos6, self.h50*30.25),
                (self.w50*9.75 + self.pos6, self.h50*31),
                (self.w50*10.75 + self.pos6, self.h50*30.75),
                (self.w50*9.5 + self.pos6, self.h50*30.75),
                (self.w50*10.5 + self.pos6, self.h50*30.5), #
                (self.w50*9.25 + self.pos6, self.h50*30.5),
                (self.w50*10.25 + self.pos6, self.h50*30.25),
                (self.w50*9 + self.pos6, self.h50*30.25)
            ), 2)

        if self.type == 2 and self.state == True:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
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
                (self.w50*9.5 + self.pos6, self.h50*30.75)
            ), 2)

        if self.type == 3:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
                (self.w50*10.25 + self.pos6, self.h50*31),
                (self.w50*11 + self.pos6, self.h50*30.25),
                (self.w50*10 + self.pos6, self.h50*30),
                (self.w50*9.75 + self.pos6, self.h50*30.25),
                (self.w50*10.75 + self.pos6, self.h50*30.5),
                (self.w50*9.75 + self.pos6, self.h50*30.25),
                (self.w50*9.5 + self.pos6, self.h50*30.5),
                (self.w50*10.5 + self.pos6, self.h50*30.75),
                (self.w50*9.5 + self.pos6, self.h50*30.5),
                (self.w50*9.25 + self.pos6, self.h50*30.75)
            ), 2)

        if self.type == 4:
            pygame.draw.lines(Setup.screen, Setup.color_theme[1], True, (
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
                (self.w50*12 + self.pos5, self.h50*29.75),
                (self.w50*13 + self.pos5, self.h50*29.75),
                (self.w50*11.5 + self.pos5, self.h50*29.75),
                (self.w50*11.5 + self.pos5, self.h50*30)
            ), 2)

    def interaction_screen(self):
        if self.type == 0 or self.state == False:
            Setup.scene = 1

            if self.type == 4:
                try:
                    Setup.room = Setup.rooms_list[Setup.rooms_list.index(Setup.room) + 1]
                except:
                    Setup.scene = 2
                    Setup.color_theme = Setup.dark_theme

        else:

            if self.type == 1:
                pygame.draw.rect(Setup.screen, Setup.color_theme[1], (Setup.w/2, Setup.h/9*2, Setup.w/32*9, Setup.h/3*2), 2)
                pygame.draw.polygon(Setup.screen, Setup.color_theme[0], ((Setup.w/32*7, Setup.h/9*2), (Setup.w/2, Setup.h/9), (Setup.w/32*19, Setup.h/9*7), (Setup.w/16*5, Setup.h/9*8)))
                pygame.draw.polygon(Setup.screen, Setup.color_theme[1], ((Setup.w/32*7, Setup.h/9*2), (Setup.w/2, Setup.h/9), (Setup.w/32*19, Setup.h/9*7), (Setup.w/16*5, Setup.h/9*8)), 2)

            if self.type == 2:
                self.cipher_wheel_back.draw()
                self.cipher_wheel_front.draw()
                self.cipher_wheel_gear.draw()

                if Inputs.mbdown and self.cipher_wheel_back.get_rect().collidepoint(Inputs.mx, Inputs.my):
                    self.state = False
                    Setup.cipher_wheel.state = 1
            
            if self.type == 3:
                self.tabula_recta.draw()

            if self.type == 4:
                pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, (
                    (Setup.w/32*11, Setup.h),
                    (Setup.w/32*11, Setup.h/18*17),
                    (Setup.w/32*21, Setup.h/18*17),
                    (Setup.w/32*21, Setup.h),
                    (Setup.w/32*21, Setup.h/18*17),
                    (Setup.w/32*18, Setup.h/18*17),
                    (Setup.w/32*17, Setup.h/18*15),
                    (Setup.w/32*27, Setup.h/18*15),
                    (Setup.w/32*27, Setup.h/18*2),
                    (Setup.w/32*5, Setup.h/18*2),
                    (Setup.w/32*5, Setup.h/18*15),
                    (Setup.w/32*6, Setup.h/18*15),
                    (Setup.w/32*6, Setup.h/18*3),
                    (Setup.w/32*26, Setup.h/18*3),
                    (Setup.w/32*26, Setup.h/18*14),
                    (Setup.w/32*6, Setup.h/18*14),
                    (Setup.w/32*6, Setup.h/18*17),
                    (Setup.w/32*10, Setup.h/18*17),
                    (Setup.w/32*10, Setup.h/18*14),
                    (Setup.w/32*10, Setup.h/18*15),
                    (Setup.w/32*17, Setup.h/18*15),
                    (Setup.w/32*15, Setup.h/18*15),
                    (Setup.w/32*14, Setup.h/18*17)
                ), 2)

                self.keyboard.draw()
                if Inputs.mbdown:
                    if self.hitbox_qwertzuiop.collidepoint(Inputs.mx, Inputs.my):
                        if self.hitbox_qa.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'Q'
                        if self.hitbox_wsy.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'W'
                        if self.hitbox_edx.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'E'
                        if self.hitbox_rfc.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'R'
                        if self.hitbox_tgv.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'T'
                        if self.hitbox_zhb.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'Z'
                        if self.hitbox_ujn.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'U'
                        if self.hitbox_ikm.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'I'
                        if self.hitbox_ol.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'O'
                        if self.hitbox_p.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'P'

                    if self.hitbox_asdfghjkl.collidepoint(Inputs.mx, Inputs.my):
                        if self.hitbox_qa.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'A'
                        if self.hitbox_wsy.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'S'
                        if self.hitbox_edx.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'D'
                        if self.hitbox_rfc.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'F'
                        if self.hitbox_tgv.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'G'
                        if self.hitbox_zhb.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'H'
                        if self.hitbox_ujn.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'J'
                        if self.hitbox_ikm.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'K'
                        if self.hitbox_ol.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'L'

                    if self.hitbox_yxcvbnm.collidepoint(Inputs.mx, Inputs.my):
                        if self.hitbox_wsy.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'Y'
                        if self.hitbox_edx.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'X'
                        if self.hitbox_rfc.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'C'
                        if self.hitbox_tgv.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'V'
                        if self.hitbox_zhb.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'B'
                        if self.hitbox_ujn.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'N'
                        if self.hitbox_ikm.collidepoint(Inputs.mx, Inputs.my):
                            self.input += 'M'
                        if self.hitbox_p.collidepoint(Inputs.mx, Inputs.my):
                            self.input = self.input[:len(self.input) - 1]

                    if self.input == self.code:
                        self.state = False

                

                display = Surfaces.Text(Surfaces.monospace, self.input, Setup.color_theme[1], "height", self.keyboard.img.get_height()/3, [Setup.w/32*11, Setup.h/9*5 - self.keyboard.img.get_height()/3], ["left", "top"])
                display.draw()

    def uv_drawing(self):
        if self.type == 1:
            text_key = Surfaces.UVText(Surfaces.monospace, self.code, "height", Setup.h/9, [Setup.w/8*5, Setup.h/9*3])
            text_key.draw(pygame.BLEND_SUB)


class Door(Object):
    '''(door_type = 0 has a keypad with numbers; door_type = 1 has a keyboard)'''
    def __init__(self, position, door_type, code):
        super().__init__(position)
        self.type = door_type
        self.state = True # for type = 1 (if True, the door is closed, if False then open)
        self.code = code
        self.input = ''

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

        self.hitbox = pygame.Rect(self.w50*10 + self.pos5, self.h50*20, self.w50*5, self.h50*20)

        if self.type == 0:
            self.keypad = Surfaces.Image(r'assets\keypad.png', "width", Setup.w/16*3 +4, [Setup.w/16*6.5, Setup.h/9*4], ["left", "top"])

            self.hitbox_123 = pygame.Rect(Setup.w/16*6.5, Setup.h/9*4, self.keypad.img.get_width(), self.keypad.img.get_height()/4)
            self.hitbox_456 = pygame.Rect(Setup.w/16*6.5, Setup.h/9*4 + self.keypad.img.get_height()/4, self.keypad.img.get_width(), self.keypad.img.get_height()/4)
            self.hitbox_789 = pygame.Rect(Setup.w/16*6.5, Setup.h/9*4 + self.keypad.img.get_height()/4*2, self.keypad.img.get_width(), self.keypad.img.get_height()/4)

            self.hitbox_147 = pygame.Rect(Setup.w/16*6.5, Setup.h/9*4, self.keypad.img.get_width()/3, self.keypad.img.get_height())
            self.hitbox_258 = pygame.Rect(Setup.w/16*6.5 + self.keypad.img.get_width()/3, Setup.h/9*4, self.keypad.img.get_width()/3, self.keypad.img.get_height())
            self.hitbox_369 = pygame.Rect(Setup.w/16*6.5 + self.keypad.img.get_width()/3*2, Setup.h/9*4, self.keypad.img.get_width()/3, self.keypad.img.get_height())

            self.hitbox_0 = pygame.Rect(Setup.w/16*6.5 + self.keypad.img.get_width()/3, Setup.h/9*4 + self.keypad.img.get_height()/4*3, self.keypad.img.get_width()/3, self.keypad.img.get_height()/4)

        if self.type == 1:
            self.keyboard = Surfaces.Image(r'assets\keyboard.png', "width", Setup.w/16*10 +4, [Setup.w/16*3, Setup.h/9*4], ["left", "top"])

            self.hitbox_qwertzuiop = pygame.Rect(Setup.w/16*3, Setup.h/9*4, self.keyboard.img.get_width(), self.keyboard.img.get_height()/3)
            self.hitbox_asdfghjkl = pygame.Rect(Setup.w/16*3, Setup.h/9*4 + self.keyboard.img.get_height()/3, self.keyboard.img.get_width(), self.keyboard.img.get_height()/3)
            self.hitbox_yxcvbnm = pygame.Rect(Setup.w/16*3, Setup.h/9*4 + self.keyboard.img.get_height()/3*2, self.keyboard.img.get_width(), self.keyboard.img.get_height()/3)

            self.hitbox_qa =  pygame.Rect(Setup.w/16*3, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_wsy = pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_edx = pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*2, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_rfc = pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*3, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_tgv = pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*4, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_zhb = pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*5, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_ujn = pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*6, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_ikm = pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*7, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_ol =  pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*8, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())
            self.hitbox_p =   pygame.Rect(Setup.w/16*3 + self.keyboard.img.get_width()/10*9, Setup.h/9*4, self.keyboard.img.get_width()/10, self.keyboard.img.get_height())

    def draw(self):
        pygame.draw.polygon(Setup.screen, Setup.color_theme[0], self.polygon)
        pygame.draw.polygon(Setup.screen, Setup.color_theme[1], self.polygon, 2)
        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, self.lines, 2)

    def interaction_screen(self):
        if self.state == False:
            Setup.scene = 1
            try:
                    Setup.room = Setup.rooms_list[Setup.rooms_list.index(Setup.room) + 1]
            except:
                Setup.scene = 2
                Setup.color_theme = Setup.dark_theme

        if self.type == 0:
            self.keypad.draw()

            if Inputs.mbdown:
                if len(self.input) == 4:
                    self.input = ''

                else:
                    if self.hitbox_123.collidepoint(Inputs.mx, Inputs.my):
                        if self.hitbox_147.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '1'
                        if self.hitbox_258.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '2'
                        if self.hitbox_369.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '3'
                    if self.hitbox_456.collidepoint(Inputs.mx, Inputs.my):
                        if self.hitbox_147.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '4'
                        if self.hitbox_258.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '5'
                        if self.hitbox_369.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '6'
                    if self.hitbox_789.collidepoint(Inputs.mx, Inputs.my):
                        if self.hitbox_147.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '7'
                        if self.hitbox_258.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '8'
                        if self.hitbox_369.collidepoint(Inputs.mx, Inputs.my):
                            self.input += '9'
                    if self.hitbox_0.collidepoint(Inputs.mx, Inputs.my):
                        self.input += '0'
                
                    if self.input == self.code:
                        self.state = False

            display = Surfaces.Text(Surfaces.monospace, self.input, Setup.color_theme[1], "height", self.keypad.img.get_height()/4, [Setup.w/16*6.5, Setup.h/9*4 - self.keypad.img.get_height()/4], ["left", "top"])
            display.draw()

        if self.type == 1:
            self.keyboard.draw()
            if Inputs.mbdown:
                if self.hitbox_qwertzuiop.collidepoint(Inputs.mx, Inputs.my):
                    if self.hitbox_qa.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'Q'
                    if self.hitbox_wsy.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'W'
                    if self.hitbox_edx.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'E'
                    if self.hitbox_rfc.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'R'
                    if self.hitbox_tgv.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'T'
                    if self.hitbox_zhb.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'Z'
                    if self.hitbox_ujn.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'U'
                    if self.hitbox_ikm.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'I'
                    if self.hitbox_ol.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'O'
                    if self.hitbox_p.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'P'

                if self.hitbox_asdfghjkl.collidepoint(Inputs.mx, Inputs.my):
                    if self.hitbox_qa.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'A'
                    if self.hitbox_wsy.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'S'
                    if self.hitbox_edx.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'D'
                    if self.hitbox_rfc.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'F'
                    if self.hitbox_tgv.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'G'
                    if self.hitbox_zhb.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'H'
                    if self.hitbox_ujn.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'J'
                    if self.hitbox_ikm.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'K'
                    if self.hitbox_ol.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'L'

                if self.hitbox_yxcvbnm.collidepoint(Inputs.mx, Inputs.my):
                    if self.hitbox_wsy.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'Y'
                    if self.hitbox_edx.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'X'
                    if self.hitbox_rfc.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'C'
                    if self.hitbox_tgv.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'V'
                    if self.hitbox_zhb.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'B'
                    if self.hitbox_ujn.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'N'
                    if self.hitbox_ikm.collidepoint(Inputs.mx, Inputs.my):
                        self.input += 'M'
                    if self.hitbox_p.collidepoint(Inputs.mx, Inputs.my):
                        self.input = self.input[:len(self.input) - 1]

                if self.input == self.code:
                    self.state = False

            display = Surfaces.Text(Surfaces.monospace, self.input, Setup.color_theme[1], "height", self.keyboard.img.get_height()/3, [Setup.w/16*3, Setup.h/9*4 - self.keyboard.img.get_height()/3], ["left", "top"])
            display.draw()


class Lamp(Object):
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

        self.hitbox = pygame.Rect(self.w50*11 + self.pos5, self.h50*20, self.w50*3, self.h50*21)
    
    def draw(self):
        pygame.draw.polygon(Setup.screen, Setup.color_theme[0], self.polygon)
        pygame.draw.polygon(Setup.screen, Setup.color_theme[1], self.polygon, 2)
        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, self.lines, 2)

    def interaction_screen(self):
        if Setup.color_theme == Setup.dark_theme:
            Setup.color_theme = Setup.light_theme
        elif Setup.color_theme == Setup.light_theme:
            Setup.color_theme = Setup.dark_theme

        Setup.scene = 1


class Calendar(Object):
    def __init__(self, position, code = None, key = None):
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

        self.hitbox = pygame.Rect(self.w50*11 + self.pos5, self.h50*26, self.w50*3, self.h50*3)

    def draw(self):
        pygame.draw.polygon(Setup.screen, Setup.color_theme[0], self.polygon)
        pygame.draw.polygon(Setup.screen, Setup.color_theme[1], self.polygon, 2)
        pygame.draw.lines(Setup.screen, Setup.color_theme[1], False, self.lines, 2)

    def interaction_screen(self):
        pygame.draw.rect(Setup.screen, Setup.color_theme[1], (Setup.w/16*4.5, Setup.h/9*2, Setup.w/16*7, Setup.h/9*5), 2)