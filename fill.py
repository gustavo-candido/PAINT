import pygame
from pygame.locals import *
from tool import Tool
from collections import deque
from random import randrange, shuffle

class Fill(Tool):

    def __init__(self, color):
        self.color = color


    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        # First click -> Save the line origin
        if event.type == MOUSEBUTTONDOWN:
            if mouse_y > 60:
                print("Filling...")
                self.drawFill(background, (mouse_x, mouse_y), self.color)
                self.drawFill(screen, (mouse_x, mouse_y), self.color)

    def is_valid(self, point):
        x, y = point
        return 0 <= x < 900 and 61 <= y < 500

    def drawFill(self, layer, point1, color):

        previous_color = layer.get_at(point1)

        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]


        fila = deque()
        fila.append(point1)
        vis = {}
        vis[point1] = True
        while len(fila) > 0:
            current_point = fila.popleft()
            layer.set_at(current_point, color)
            x, y = current_point

            for i in range(4):
                #
                # coin = randrange(0,3)
                # if not coin:
                #     continue

                new_point = (x+dx[i], y+dy[i])
                if not vis.get(new_point, False) and self.is_valid(new_point):
                    if layer.get_at(new_point) == previous_color:
                        fila.append(new_point)
                        vis[new_point] = True
