import pygame 
from pygame.locals import *


class Tool:
    def __init__(self):
        ...

    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        ...

###########################################################################################################################################################################################################
class Line(Tool):

    def __init__(self):
        self.first_click = False
        self.points = []

    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        if mouse_y <= 60:   # 60 = Height Tool Menu
            mouse_y = 61


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
# Stop drawing when ESC is pressed

class Polyline(Line):

    def __init__(self):
        self.first_click = False
        self.points = []

    def draw(self, screen, background, event, mouse_x, mouse_y, keyboard):
        if mouse_y <= 60:   # 60 = Height Tool Menu
            mouse_y = 61


        # Reset to another polyline
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.__init__() 
        # First click -> Save the line origin
        elif event.type == MOUSEBUTTONDOWN  and self.first_click == False:
            self.first_click = True
            self.points.append((mouse_x, mouse_y))
        # "Floating Line" -> Update just screen
        elif self.first_click and (event.type != MOUSEBUTTONDOWN or event.button != 1): 
            if len(self.points) == 2:
                self.points.pop()
            self.points.append((mouse_x,mouse_y))
            self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], (0,0,0))
        # Second click -> Fixed the line on screen and background and prepare next line
        elif self.first_click and event.type == MOUSEBUTTONDOWN and event.button == 1: 
            self.points.append((mouse_x,mouse_y))
            self.drawLine(screen, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], (0,0,0))
            self.drawLine(background, self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], (0,0,0))
            self.points = [self.points[1]]
###########################################################################################################################################################################################################
class Gui:
    def __init__(self):
        pygame.init()

        # Set Width
        self.WIDTH = 900
        # Set Height
        self.HEIGHT = 500
        # Set pictures folder path
        self.base_path = 'Paint/pictures/'
        # Create screen 
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # "Background image" from screen check draw function from Line class to better understand 
        self.layer = pygame.surface.Surface((self.WIDTH, self.HEIGHT))
        # Remember pressed keys 
        self.keyboard = [0]*255
        # Set current tool to nothing
        self.current_tool = Tool()


        # Set background initial color and tool icons
        self.layer.fill((255,255,255))
        line_icon = pygame.image.load(self.base_path+'line.png')
        line_icon = pygame.transform.scale(line_icon, (50,50))
        line_rect = line_icon.get_rect()
        line_rect.move_ip(0, 0)
        self.layer.blit(line_icon, line_rect)

        curve_icon = pygame.image.load(self.base_path+'curve.png')
        curve_icon = pygame.transform.scale(curve_icon, (50,50))
        curve_rect = curve_icon.get_rect()
        curve_rect.move_ip(50, 0)
        self.layer.blit(curve_icon, curve_rect)

        circle_icon = pygame.image.load(self.base_path+'circle.png')
        circle_icon = pygame.transform.scale(circle_icon, (50,50))
        circle_rect = circle_icon.get_rect()
        circle_rect.move_ip(100, 0)
        self.layer.blit(circle_icon, circle_rect)

        square_icon = pygame.image.load(self.base_path+'square.png')
        square_icon = pygame.transform.scale(square_icon, (50,50))
        square_rect = square_icon.get_rect()
        square_rect.move_ip(150, 0)
        self.layer.blit(square_icon, square_rect)

        polyline_icon = pygame.image.load(self.base_path+'polyline.png')
        polyline_icon = pygame.transform.scale(polyline_icon, (50,50))
        polyline_rect = polyline_icon.get_rect()
        polyline_rect.move_ip(200, 0)
        self.layer.blit(polyline_icon, polyline_rect)

        rectangle_icon = pygame.image.load(self.base_path+'rectangle.png')
        rectangle_icon = pygame.transform.scale(rectangle_icon, (50,50))
        rectangle_rect = rectangle_icon.get_rect()
        rectangle_rect.move_ip(250, 0)
        self.layer.blit(rectangle_icon, rectangle_rect)

        bucket_icon = pygame.image.load(self.base_path+'bucket.png')
        bucket_icon = pygame.transform.scale(bucket_icon, (50,50))
        bucket_rect = bucket_icon.get_rect()
        bucket_rect.move_ip(300, 0)
        self.layer.blit(bucket_icon, bucket_rect)

        self.screen.blit(self.layer, (0,0))

        pygame.display.flip()


        #
        self.layer.blit(self.screen, (0,0))
        while True:
            for event in pygame.event.get():

                self.screen.blit(self.layer, (0,0))
                if event.type == QUIT:
                    pygame.quit() 
                    exit()  

                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.Inside(line_rect):
                    self.current_tool = Line()
                    print("Line tool selected")
                    continue

                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.Inside(polyline_rect):
                    self.current_tool = Polyline()
                    print("Polyline tool selected")
                    continue


                self.current_tool.draw(self.screen, self.layer, event, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.keyboard)
                pygame.display.flip()


    def Inside(self, rect):
        return rect.left <= pygame.mouse.get_pos()[0] <= rect.right and rect.top <= pygame.mouse.get_pos()[1] <= rect.bottom

def main():
    gui = Gui()


if __name__ == "__main__":
    main()