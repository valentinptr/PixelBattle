import random

import objects

BACKGROUND_COLOR = 'black'
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MIN_SPEED = 100
MAX_SPEED = MIN_SPEED


def direction():
    """
    This function is used to determine a random speed
    :return:  with random sign
    """
    speed = random.randint(MIN_SPEED, MAX_SPEED)
    sign = random.randint(0, 100000000)
    if (sign % 2) == 0:
        speed = -speed
    return speed


BALL_SPEED_X_1 = direction()  # we assign an X speed
BALL_SPEED_Y_1 = BALL_SPEED_X_1  # we assign an Y speed

BALL_SPEED_X_2 = direction()  # we assign an X speed
BALL_SPEED_Y_2 = BALL_SPEED_X_2  # we assign an Y speed


class Engine:
    def __init__(self):
        self.cubes = []
        self.grids = []

    def update(self, dt):
        global BALL_SPEED_X_1, BALL_SPEED_Y_1, BALL_SPEED_X_2, BALL_SPEED_Y_2

        # initialization of the X and Y speed of the ball
        self.cubes[0].x += int(BALL_SPEED_X_1 * dt)
        self.cubes[0].y += int(BALL_SPEED_Y_1 * dt)

        self.cubes[1].x += int(BALL_SPEED_X_2 * dt)
        self.cubes[1].y += int(BALL_SPEED_Y_2 * dt)

        if self.cubes[0].x < 0:
            self.cubes[0].x = 1
            BALL_SPEED_X_1 = -BALL_SPEED_X_1  # the X speed is then reversed

        if self.cubes[1].x < 0:
            self.cubes[1].x = 1
            BALL_SPEED_X_2 = -BALL_SPEED_X_2  # the X speed is then reversed

        # used to check if the ball as collided with the right wall
        if self.cubes[0].x > (WINDOW_WIDTH - objects.SIZE_CUBE - 1):
            self.cubes[0].x = WINDOW_WIDTH - objects.SIZE_CUBE
            BALL_SPEED_X_1 = -BALL_SPEED_X_1  # the X speed is then reversed

        if self.cubes[1].x > (WINDOW_WIDTH - objects.SIZE_CUBE - 1):
            self.cubes[1].x = WINDOW_WIDTH - objects.SIZE_CUBE
            BALL_SPEED_X_2 = -BALL_SPEED_X_2  # the X speed is then reversed

        # used to check if the ball as entered the upper goal
        if self.cubes[0].y < 1:
            BALL_SPEED_Y_1 = -BALL_SPEED_Y_1

        if self.cubes[1].y < 1:
            BALL_SPEED_Y_2 = -BALL_SPEED_Y_2

        if self.cubes[0].y > WINDOW_HEIGHT - objects.SIZE_CUBE - 1:
            self.cubes[0].y = WINDOW_HEIGHT - objects.SIZE_CUBE
            BALL_SPEED_Y_1 = -BALL_SPEED_Y_1

        if self.cubes[1].y > WINDOW_HEIGHT - objects.SIZE_CUBE - 1:
            self.cubes[1].y = WINDOW_HEIGHT - objects.SIZE_CUBE
            BALL_SPEED_Y_2 = -BALL_SPEED_Y_2

        for grid in self.grids:
            if (self.cubes[0].x == grid.x) and (self.cubes[0].y == grid.y) and grid.color == (100, 100, 100):
                grid.color = (67, 124, 86)
                BALL_SPEED_X_1 = -BALL_SPEED_X_1

            if (self.cubes[1].x == grid.x) and (self.cubes[1].y == grid.y) and grid.color == (67, 124, 86):
                grid.color = (100, 100, 100)
                BALL_SPEED_X_2 = -BALL_SPEED_X_2


    @staticmethod
    def draw_background(screen):
        screen.fill(BACKGROUND_COLOR)

    def draw_cubes(self, screen):
        for cube in self.cubes:
            cube.draw(screen)

    def drop_cubes(self, x, y, color):
        new_cube = objects.Cube(x, y, color)
        self.cubes.append(new_cube)
        return new_cube

    def draw_grid(self, screen):
        for grid in self.grids:
            grid.draw(screen)

    def drop_grid(self, x, y, color):
        new_grid = objects.Grid(x, y, color)
        self.grids.append(new_grid)
        return new_grid

    def render_grid(self):
        for x in range(0, int(WINDOW_WIDTH / 2), objects.SIZE_CUBE):
            for y in range(0, WINDOW_HEIGHT, objects.SIZE_CUBE):
                self.drop_grid(x, y, (67, 124, 86))

        for x in range(int(WINDOW_WIDTH / 2), WINDOW_WIDTH, objects.SIZE_CUBE):
            for y in range(0, WINDOW_HEIGHT, objects.SIZE_CUBE):
                self.drop_grid(x, y, (100, 100, 100))
