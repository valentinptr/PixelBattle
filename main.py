import pygame
from game import *
from objects import *

FPS = 60
fpsClock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Modern Pong")
clock = pygame.time.Clock()
running = True
dt = 0

engine = Engine()
cube_j1 = Cube(160, 200, (74, 149, 43))
cube_j2 = Cube(640, 300, (255, 255, 255))
engine.render_grid()
engine.drop_cubes(cube_j1.x, cube_j1.y, cube_j1.color)
engine.drop_cubes(cube_j2.x, cube_j2.y, cube_j2.color)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    engine.update(dt)
    engine.draw_background(screen)
    engine.draw_grid(screen)
    engine.draw_cubes(screen)

    pygame.display.flip()
    dt = clock.tick(FPS) / 1000

pygame.quit()
