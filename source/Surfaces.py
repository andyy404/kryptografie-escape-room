import pygame, Setup

monospace = pygame.font.Font(r'assets\consolas.ttf', 200)
gothic = pygame.font.Font(r'assets\gothic.ttf', 200)

class Surface():
    def __init__(self, size_type, size, position, alignment):
        if size_type == "width":
            self.img = pygame.transform.scale(self.img, (size, size/self.img.get_width()*self.img.get_height()))
        
        elif size_type == "height":
            self.img = pygame.transform.scale(self.img, (size/self.img.get_height()*self.img.get_width(), size))
        
        self.position = position
        self.alignment = alignment

        if self.alignment[0] == "left":
            self.position[0] = self.position[0]
        elif self.alignment[0] == "center":
            self.position[0] = Setup.w/2 - self.img.get_width()/2
        elif self.alignment[0] == "right":
            self.position[0] = Setup.w - self.img.get_width() - self.position[0]

        if self.alignment[1] == "top":
            self.position[1] = self.position[1]
        elif self.alignment[1] == "center":
            self.position[1] = Setup.h/2 - self.img.get_height()/2
        elif self.alignment[1] == "bottom":
            self.position[1] = Setup.h - self.img.get_height() - self.position[1]

    def draw(self, blend_mode = 0):
        Setup.screen.blit(self.img, self.position, None, blend_mode)

    def get_rect(self):
        return pygame.Rect(self.position, self.img.get_size())


class UVText(Surface):
    def __init__(self, font, text, size_type, size, position, alignment = ["left", "top"]):
        self.img = font.render(text, False, Setup.color_theme[3], (0, 0, 0, 0))

        super().__init__(size_type, size, position, alignment)


class Text(Surface):
    def __init__(self, font, text, color, size_type, size, position, alignment = ["left", "top"]):
        self.img = font.render(text, False, color)

        super().__init__(size_type, size, position, alignment)

class Image(Surface):
    def __init__(self, path, size_type, size, position, alignment = ["left", "top"]):
        self.img = pygame.image.load(path)

        super().__init__(size_type, size, position, alignment)