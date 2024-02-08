from pygame import gfxdraw

SIZE_CUBE = 20


class Cube:
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        gfxdraw.box(screen, (self.x, self.y, SIZE_CUBE, SIZE_CUBE), self.color)


class Grid:
    def __init__(self, x, y, color):
        self.color = color  # white color
        self.x = x
        self.y = y

    def draw(self, screen):
        gfxdraw.box(screen, (self.x, self.y, SIZE_CUBE, SIZE_CUBE), self.color)
