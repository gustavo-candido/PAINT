import pygame
from pygame.locals import *
from line import Line

# Stop drawing when ESC is pressed
class Polyline(Line):

    def __init__(self, color):
        self.first_click = False
        self.points = []
        self.color = color

    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        if mouse_y <= 60:   # 60 = Height Tool Menu
            mouse_y = 61


        # Reset to another polyline
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.__init__(self.color)
        # First click -> Save the line origin
        elif event.type == MOUSEBUTTONDOWN  and self.first_click == False:
            self.first_click = True
            self.points.append((mouse_x, mouse_y))
        # "Floating Line" -> Update just screen
        elif self.first_click and (event.type != MOUSEBUTTONDOWN or event.button != 1):
            if len(self.points) == 2:
                self.points.pop()
            self.points.append((mouse_x,mouse_y))
            self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.color)
        # Second click -> Fixed the line on screen and background and prepare next line
        elif self.first_click and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.points.append((mouse_x,mouse_y))
            self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.color)
            self.drawLine(background, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.color)
            self.points = [self.points[1]]
