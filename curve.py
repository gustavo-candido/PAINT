import pygame
from pygame.locals import *
from tool import Tool
from line import Line
import numpy

class Curve(Line):

    def __init__(self, color):
        self.first_click = False
        self.first_line = False
        self.points = []
        self.color = color
        self.screen_aux = pygame.surface.Surface((900,500))

    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        if mouse_y <= 60:   # 60 = Height Tool Menu
            mouse_y = 61

        if self.first_line == False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.__init__(self.color)

            elif event.type == MOUSEBUTTONDOWN  and self.first_click == False:
                self.first_click = True
                self.points.append((mouse_x, mouse_y))

            elif self.first_click and (event.type != MOUSEBUTTONDOWN or event.button != 1):
                if len(self.points) == 2:
                    self.points.pop()
                self.points.append((mouse_x,mouse_y))
                self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.color)

            elif self.first_click and event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.screen_aux.blit(background, (0,0))
                self.drawLine(background, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.color)
                self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], self.color)

                self.first_line = True
                self.first_click = False

        else: 
            if event.type == MOUSEBUTTONDOWN  and self.first_click == False  and event.button == 1:
                self.first_click = True
                background.blit(self.screen_aux, (0,0))

                self.points.append((mouse_x,mouse_y))
                self.Process_Curve(background, self.points[0], self.points[2], self.points[1], self.points[1])
                self.Process_Curve(screen, self.points[0], self.points[2], self.points[1], self.points[1])

            elif event.type == MOUSEBUTTONDOWN  and self.first_click == True and event.button == 1:
                self.points.append((mouse_x,mouse_y))
                background.blit(self.screen_aux, (0,0))

                self.Process_Curve(background, self.points[0], self.points[2], self.points[3], self.points[1])
                self.Process_Curve(screen, self.points[0], self.points[2], self.points[3], self.points[1])
                self.__init__(self.color)
                



    def Process_Curve(self, layer, p0, p1, p2, p3):
        sX, sY = p0

        for t in numpy.arange(0,1,0.01):
            b0 = (1-t)**3
            b1 = 3 * t * (1-t)**2
            b2 = 3 * t**2 * (1-t)
            b3 = t**3

            eX = int((b0 * p0[0]) + (b1 * p1[0]) + (b2 * p2[0]) + (b3 * p3[0]))
            eY = int((b0 * p0[1]) + (b1 * p1[1]) + (b2 * p2[1]) + (b3 * p3[1]))
            self.drawLine(layer, sX, sY, eX, eY, self.color)
            sX,sY = (eX, eY)

        self.drawLine(layer, sX, sY, p3[0], p3[1], self.color)

