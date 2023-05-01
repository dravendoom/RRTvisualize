import pygame
import random
import math
import time
from node import Node

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (55, 155, 222)
purple = (128, 0, 128)

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class RRT:
    def __init__(self, start, goal, obstacles):
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.obstacles = obstacles
        self.nodes = [self.start]
        self.edges = []

    def generate_rrt(self, k, delta_t, max_paths):
        paths = []
        found_paths = 0
        shortest_path = None
        shortest_distance = math.inf

        while found_paths < max_paths:
            path = None
            for i in range(k):
                rand_node = self.random_state()
                nearest_node = self.nearest_neighbor(rand_node)
                u = self.select_input(rand_node, nearest_node)
                new_node = self.new_state(nearest_node, u, delta_t)
                if not self.collision(new_node, nearest_node):
                    self.nodes.append(new_node)
                    new_node.parent = nearest_node
                    self.edges.append((nearest_node, new_node, u))
                    pygame.draw.line(screen, blue, (nearest_node.x, nearest_node.y), (new_node.x, new_node.y), 2)
                    pygame.display.update()
                    if self.goal_reached(new_node):
                        path = self.get_path(new_node)
                        break
            if path is not None:
                paths.append(path)
                found_paths += 1
                self.exclude_nodes(path)

                # Draw the path in red
                for i in range(len(path) - 1):
                    pygame.draw.line(screen, red, (path[i].x, path[i].y), (path[i + 1].x, path[i + 1].y), 3)
                    pygame.display.update()

                # Calculate the path distance
                path_distance = sum(euclidean_distance(path[i].x, path[i].y, path[i+1].x, path[i+1].y) for i in range(len(path) - 1))
                if path_distance < shortest_distance:
                    shortest_distance = path_distance
                    shortest_path = path

        # Draw the shortest path in purple
        if shortest_path:
            for i in range(len(shortest_path) - 1):
                pygame.draw.line(screen, purple, (shortest_path[i].x, shortest_path[i].y),
                                 (shortest_path[i + 1].x, shortest_path[i + 1].y), 4)
                pygame.display.update()

        return paths

    def random_state(self):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        return Node(x, y)

    def nearest_neighbor(self, node):
        min_distance = math.inf
        nearest_node = None
        for n in self.nodes:
            distance = euclidean_distance(n.x, n.y, node.x, node.y)
            if distance < min_distance:
                min_distance = distance
                nearest_node = n
        return nearest_node

    def select_input(self, rand_node, nearest_node):
        return math.atan2(rand_node.y - nearest_node.y, rand_node.x - nearest_node.x)

    def new_state(self, nearest_node, u, delta_t):
        x = nearest_node.x + delta_t * math.cos(u)
        y = nearest_node.y + delta_t * math.sin(u)
        return Node(x, y)

    def line_intersection(self, p1, p2, q1, q2):
        def clockwiseLineSegment(A, B, C):
            return (C.y - A.y) * (B.x - A.x) > (B.y - A.y) * (C.x - A.x)
        if (p1 == q1) or (p1 == q2) or (p2 == q1) or (p2 == q2):
            return False
        return (clockwiseLineSegment(p1, q1, q2) != clockwiseLineSegment(p2, q1, q2)) and (clockwiseLineSegment(p1, p2, q1) != clockwiseLineSegment(p1, p2, q2))

    def collision(self, node, parent_node):
        for obstacle in self.obstacles:
            p1 = parent_node
            p2 = node
            rect_points = [
                (obstacle.left, obstacle.top),
                (obstacle.left, obstacle.bottom),
                (obstacle.right, obstacle.bottom),
                (obstacle.right, obstacle.top),
            ]
            for i in range(len(rect_points)):
                q1 = Node(rect_points[i][0], rect_points[i][1])
                q2 = Node(rect_points[(i + 1) % len(rect_points)][0], rect_points[(i + 1) % len(rect_points)][1])

                if self.line_intersection(p1, p2, q1, q2):
                    return True
        return False

    def goal_reached(self, node):
        goal_radius = 50
        goalFlag = euclidean_distance(self.goal.x, self.goal.y, node.x, node.y) < goal_radius
        return goalFlag

    def get_path(self, node):
        path = []
        while node.parent is not None:
            path.append(node)
            node = node.parent
        path.append(self.start)
        path.reverse()
        return path

    def exclude_nodes(self, nodes_to_exclude):
        self.nodes = [node for node in self.nodes if node not in nodes_to_exclude]