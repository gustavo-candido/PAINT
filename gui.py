import pygame
from pygame.locals import *
import os
from tool import Tool
from line import Line
from polyline import Polyline
from rectangle import Rectangle
from square import Square
from circle import Circle

class Gui:
    def __init__(self):
        pygame.init()

        # Set Width
        self.WIDTH = 900
        # Set Height
        self.HEIGHT = 500
        # Set pictures folder path
        self.base_path = os.path.dirname(os.path.abspath(__file__)) + '/pictures/'
        # Create screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        # "Background image" from screen, check draw function from Line class to better understanding
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

                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.Inside(rectangle_rect):
                    self.current_tool = Rectangle()
                    print("Rectangle tool selected")
                    continue

                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.Inside(square_rect):
                    self.current_tool = Square()
                    print("Square tool selected")
                    continue

                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.Inside(circle_rect):
                    self.current_tool = Circle()
                    print("Circle tool selected")
                    continue




                self.current_tool.draw(self.screen, self.layer, event, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.keyboard)
                pygame.display.flip()


    def Inside(self, rect):
        return rect.left <= pygame.mouse.get_pos()[0] <= rect.right and rect.top <= pygame.mouse.get_pos()[1] <= rect.bottom

def main():
    gui = Gui()


if __name__ == "__main__":
    main()
