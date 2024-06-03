import pygame
import random
import math
import time
from node import Node
from rrt import RRT
import arenas

screen_width = 1000
screen_height = 1000
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (55, 155, 222)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.init()
pygame.display.set_caption("RRT Path Planning")

for arena_function in [arenas.Arena1, arenas.Arena2, arenas.Arena3]:
    arena_info = arena_function()
    obstacles = arena_info[0]
    start_point = arena_info[1]
    end_point = arena_info[2]

    rrt = RRT(start_point, end_point, obstacles)
    screen.fill(white)
    for obstacle in obstacles:
        pygame.draw.rect(screen, black, obstacle)
        pygame.display.update()
    pygame.draw.circle(screen, green, start_point, 2)
    pygame.draw.circle(screen, green, end_point, 50)

    paths = rrt.generate_rrt(10000, 12, 10)

    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting_for_key = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
