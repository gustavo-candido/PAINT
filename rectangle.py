import pygame
from pygame.locals import *
from tool import Tool

class Rectangle(Tool):

    def __init__(self, color):
        self.first_click = False
        self.points = []
        self.color = color


    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        if mouse_y <= 60:   # 60 = Height Tool Menu
            mouse_y = 61


        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.__init__(self.color)
        # First click -> Save the line origin
        if event.type == MOUSEBUTTONDOWN  and self.first_click == False:
            self.first_click = True
            self.points.append((mouse_x, mouse_y))
        # "Floating Line" -> Update just screen
        elif self.first_click and (event.type != MOUSEBUTTONDOWN or event.button != 1):
            if len(self.points) == 2:
                self.points.pop()
            self.points.append((mouse_x,mouse_y))
            self.drawRectangle(screen, self.points[0], self.points[1], self.color)
        # Second click -> Fixed the line on screen and background and prepare to another line
        elif self.first_click and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.points.append((mouse_x,mouse_y))
            self.drawRectangle(screen, self.points[0], self.points[1], self.color)
            self.drawRectangle(background, self.points[0], self.points[1], self.color)
            self.__init__(self.color)


    def drawRectangle(self, layer, point1, point2, color):
        x1, y1 = point1
        x2, y2 = point2

        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)

        for x in range(x1, x2+1):
            layer.set_at((x,y1), color)
        for x in range(x1, x2+1):
            layer.set_at((x,y2), color)
        for y in range(y1, y2+1):
            layer.set_at((x1, y), color)
        for y in range(y1, y2+1):
            layer.set_at((x2, y), color)
