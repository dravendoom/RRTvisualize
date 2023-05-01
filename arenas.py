import pygame
import math
import random

black = (0, 0, 0)

def Arena1():
    start_point = (150, 150)
    end_point = (random.randint(700, 900), random.randint(100, 900))
    obstacles = [
        pygame.Rect(0, 0, 50, 1000),
        pygame.Rect(0, 0, 1000, 50),
        pygame.Rect(950, 0, 50, 1000),
        pygame.Rect(0, 950, 1000, 50),
        pygame.Rect(300, 0, 50, 750),
        pygame.Rect(300, 850, 50, 100),
        pygame.Rect(600, 0, 50, 100),
        pygame.Rect(600, 200, 50, 750),
    ]
    return obstacles, start_point, end_point

def Arena2():
    start_point = (100, 100)
    end_point = (500, 500)
    obstacles = [
        pygame.Rect(0, 0, 50, 1000),
        pygame.Rect(0, 0, 1000, 50),
        pygame.Rect(950, 0, 50, 1000),
        pygame.Rect(0, 950, 1000, 50),
        pygame.Rect(0, 200, 800, 50),
        pygame.Rect(750, 200, 50, 600),
        pygame.Rect(200, 750, 600, 50)
    ]
    return obstacles, start_point, end_point

def Arena3():
    start_point = (75, 75)
    end_point = (900, 900)
    obstacles = [
        pygame.Rect(0, 0, 50, 1000),
        pygame.Rect(0, 0, 1000, 50),
        pygame.Rect(950, 0, 50, 1000),
        pygame.Rect(0, 950, 1000, 50),
        pygame.Rect(100, 100, 125, 125),
        pygame.Rect(100, 300, 125, 125),
        pygame.Rect(100, 500, 125, 125),
        pygame.Rect(100, 700, 125, 125),
        pygame.Rect(300, 100, 125, 125),
        pygame.Rect(500, 100, 125, 125),
        pygame.Rect(700, 100, 125, 125),
        pygame.Rect(300, 300, 125, 125),
        pygame.Rect(500, 300, 125, 125),
        pygame.Rect(700, 300, 125, 125),
        pygame.Rect(300, 500, 125, 125),
        pygame.Rect(500, 500, 125, 125),
        pygame.Rect(700, 500, 125, 125),
        pygame.Rect(300, 700, 125, 125),
        pygame.Rect(500, 700, 125, 125),
        pygame.Rect(700, 700, 125, 125),
        pygame.Rect(825, 100, 50, 700),
        pygame.Rect(100, 825, 700, 50)

    ]
    return obstacles, start_point, end_point