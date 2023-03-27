import pygame
import random
import math
import time

screen_width = 1000
screen_height = 1000
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (55, 155, 222)

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

class RRT:
    def __init__(self, start, goal, obstacles):
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.obstacles = obstacles
        self.nodes = [self.start]
        self.edges = []

    def generate_rrt(self, k, delta_t):
        for i in range(k):
            rand_node = self.random_state()
            nearest_node = self.nearest_neighbor(rand_node)
            u = self.select_input(rand_node, nearest_node)
            new_node = self.new_state(nearest_node, u, delta_t)
            if not self.collision(new_node):
                self.nodes.append(new_node)
                new_node.parent = nearest_node
                self.edges.append((nearest_node, new_node, u))
                if self.goal_reached(new_node):
                    return self.get_path(new_node)
        return None

    def random_state(self):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        return Node(x, y)

    def nearest_neighbor(self, node):
        min_dist = math.inf
        nearest_node = None
        for n in self.nodes:
            dist = math.sqrt((n.x - node.x)**2 + (n.y - node.y)**2)
            if dist < min_dist:
                min_dist = dist
                nearest_node = n
        return nearest_node

    def select_input(self, rand_node, nearest_node):
        return math.atan2(rand_node.y - nearest_node.y, rand_node.x - nearest_node.x)

    def new_state(self, nearest_node, u, delta_t):
        x = nearest_node.x + delta_t * math.cos(u)
        y = nearest_node.y + delta_t * math.sin(u)
        return Node(x, y)

    def collision(self, node):
        for obstacle in self.obstacles:
            if obstacle.collidepoint(node.x, node.y):
                return True
        return False

    def goal_reached(self, node):
        goal_radius = 20
        euclidian_distance = math.sqrt((self.goal.x - node.x)**2 + (self.goal.y - node.y)**2) < goal_radius
        return euclidian_distance

    def get_path(self, node):
        path = []
        while node.parent is not None:
            path.append(node)
            node = node.parent
        path.append(self.start)
        path.reverse()
        return path

# Initialize Pygame
pygame.init()

# Set up the screen

pygame.display.set_caption("RRT Path Planning")

# Define the obstacles
#amount_of_obstacles = input("ENTER THE AMOUNT OF OBSTACLES YOU WISH FOR: ")
#amount_of_obstacles = int(amount_of_obstacles)
#width_variance = input("(min: 10) ENTER THE MAX RANGE OF WIDTH OF AN OBSTACLE: ")
#width_variance = int(width_variance)
#height_variance = input("(min: 10) ENTER THE MAX RANGE OF HEIGHT OF AN OBSTACLE: ")
#height_variance = int(height_variance)

obstacles = []
i = 0

while i < 25:
    # Create a new rectangle and append it to the obstacles list
    new_obstacle = pygame.Rect(random.randint(1,1000), random.randint(1,1000), random.randint(100,100), random.randint(100, 100))
    obstacles.append(new_obstacle)

    i = i + 1

# Define the RRT

start_point = (50, 50)
end_point = (550, 350)

rrt = RRT(start_point, end_point, obstacles)

# Generate the RRT
paths = []
found_paths = 0
while found_paths < 1:
    path = rrt.generate_rrt(10000, 5)
    if path is not None:
        paths.append(path)
        found_paths += 1

# Draw the obstacles and the RRT

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
pygame.draw.circle(screen, green, start_point, 2)
pygame.draw.circle(screen, green, end_point, 20)
for obstacle in obstacles:
    pygame.draw.rect(screen, black, obstacle)
for edge in rrt.edges:
    pygame.draw.line(screen, blue, (edge[0].x, edge[0].y), (edge[1].x, edge[1].y))
    time.sleep(.01)
    pygame.display.update()




# Draw the path if it exists
if paths:
    for path in paths:
        for i in range(len(path) - 1):
            pygame.draw.line(screen, red, (path[i].x, path[i].y), (path[i+1].x, path[i+1].y))
            time.sleep(.01)
            pygame.display.update()

# Event loop to keep the window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
