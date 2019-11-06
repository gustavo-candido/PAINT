import pygame
from pygame.locals import *
from tool import Tool

class Line(Tool):

    def __init__(self):
        self.first_click = False
        self.points = []

    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        if mouse_y <= 60:   # 60 = Height Tool Menu
            mouse_y = 61


        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.__init__()
        # First click -> Save the line origin
        if event.type == MOUSEBUTTONDOWN  and self.first_click == False:
            self.first_click = True
            self.points.append((mouse_x, mouse_y))
        # "Floating Line" -> Update just screen
        elif self.first_click and (event.type != MOUSEBUTTONDOWN or event.button != 1):
            if len(self.points) == 2:
                self.points.pop()
            self.points.append((mouse_x,mouse_y))
            self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], (0,0,0))
        # Second click -> Fixed the line on screen and background and prepare to another line
        elif self.first_click and event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.points.append((mouse_x,mouse_y))
            self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], (0,0,0))
            self.drawLine(background, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], (0,0,0))
            self.__init__()


    # All below its just primitives to draw a line
    def drawLineX(self, layer, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        dxAbs = abs(dx)
        dyAbs = abs(dy)
        diX = 2 * dyAbs - dxAbs
        diY = 2 * dxAbs - dyAbs

        if dx >= 0: x,y,limit = x1, y1, x2   # Left -> Right
        else: x,y,limit = x2, y2, x1         # Right -> Left

        if (dx < 0 and dy < 0) or (dx > 0 and dy > 0): increment = 1
        else: increment = -1

        layer.set_at((x,y), color)

        while x < limit:
            x = x + 1

            if diX < 0: diX = diX + 2 * dyAbs

            else:
                y = y + increment
                diX = diX + 2 * (dyAbs - dxAbs)

            layer.set_at((x,y), color)


    def drawLineY(self, layer, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        dxAbs = abs(dx)
        dyAbs = abs(dy)
        diX = 2 * dyAbs - dxAbs
        diY = 2 * dxAbs - dyAbs

        if dy >= 0: x, y, limit = x1, y1, y2   # Down -> Top
        else: x, y, limit = x2, y2, y1         # Top -> Down

        if (dx < 0 and dy < 0) or (dx > 0 and dy > 0): increment = 1
        else: increment = -1

        layer.set_at((x,y), color)

        while y < limit:
            y = y + 1

            if diY <= 0: diY = diY + 2 * dxAbs

            else:
                x = x + increment
                diY = diY + 2 * (dxAbs - dyAbs)

            layer.set_at((x,y), color)

    def drawLine(self, layer, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        dxAbs = abs(dx)
        dyAbs = abs(dy)
        diX = 2 * dyAbs - dxAbs
        diY = 2 * dxAbs - dyAbs

        if dyAbs <= dxAbs: self.drawLineX(layer, x1, y1, x2, y2, color)
        else: self.drawLineY(layer, x1, y1, x2, y2, color)



###########################################################################################################################################################################################################
