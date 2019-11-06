import pygame
from pygame.locals import *
from tool import Tool

class Circle(Tool):

    def __init__(self, color):
        self.first_click = False
        self.points = []
        self.color = color
        print(f"Im a circle and my color is {color}")


    def circlePoints(self, layer, x, y, x1, y1, color):
        if  y+y1 > 60:
            layer.set_at(( x+x1,  y+y1),color)
        if -y+y1 > 60:
            layer.set_at(( x+x1, -y+y1),color)
        if  y+y1 > 60:
            layer.set_at((-x+x1,  y+y1),color)
        if -y+y1 > 60:
            layer.set_at((-x+x1, -y+y1),color)
        if  x+y1 > 60:
            layer.set_at(( y+x1,  x+y1),color)
        if -x+y1 > 60:
            layer.set_at(( y+x1, -x+y1),color)
        if  x+y1 > 60:
            layer.set_at((-y+x1,  x+y1),color)
        if -x+y1 > 60:
            layer.set_at((-y+x1, -x+y1),color)


    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        if mouse_y <= 60:   # 60 = Height Tool Menu
            mouse_y = 61


        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.first_click = False
            self.points = []

        # First click -> Save the line origin
        if event.type == MOUSEBUTTONDOWN  and self.first_click == False:
            self.first_click = True
            self.points.append((mouse_x, mouse_y))
        # "Floating Line" -> Update just screen
        elif self.first_click and (event.type != MOUSEBUTTONDOWN or event.button != 1):
            if len(self.points) == 2:
                self.points.pop()
            self.points.append((mouse_x,mouse_y))
            self.drawCircle(screen, self.points[0], self.points[1], self.color)
        # Second click -> Fixed the line on screen and background and prepare to another line
        elif self.first_click and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.points.append((mouse_x,mouse_y))
            self.drawCircle(screen, self.points[0], self.points[1], self.color)
            self.drawCircle(background, self.points[0], self.points[1], self.color)
            self.first_click = False
            self.points = []

    def drawCircle(self, layer, point1, point2, color):
        x1, y1 = point1
        x2, y2 = point2

        radius = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        radius = int(radius)

        x = 0
        y = radius
        d = 1 - radius

        self.circlePoints(layer, x, y, x1, y1, color)

        while y > x:
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x-y) + 5
                y -= 1
            x+=1
            self.circlePoints(layer, x, y, x1, y1, color)
