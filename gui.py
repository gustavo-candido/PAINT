import pygame
from pygame.locals import *
import os
from tool import Tool
from line import Line
from polyline import Polyline
from rectangle import Rectangle
from square import Square
from circle import Circle
from curve import Curve

from math import ceil


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


        self.color_values = [
            '#173F5F',
            '#20639B',
            '#3CAEA3',
            '#F6D55C',
            '#ED553B',
            '#e72020',
            '#4de32a',
            '#28cae1',
            '#f477dc',
            '#fbf230',
            '#08469E',
            '#C2352D',
            '#F4F3F4',
            '#824C41',
            '#D89E6D',
            '#007065',
            '#FFFFFF',
            '#000000',
        ]

        self.color = []
        self.color_rects = []
        for i in range(ceil(len(self.color_values)/2)):
            self.color.append( pygame.Color(self.color_values[i]) )
            self.color_rects.append( pygame.Rect(400 + (i*25), 0, 25, 25) )
            pygame.draw.rect(self.layer, self.color[i], self.color_rects[i])

        for i in range( ceil(len(self.color_values)/2), len(self.color_values)):
            self.color.append( pygame.Color(self.color_values[i]) )
            self.color_rects.append( pygame.Rect(400 + ( (i - (ceil(len(self.color_values)/2)) )  *25), 25, 25, 25) )
            pygame.draw.rect(self.layer, self.color[i], self.color_rects[i])

        self.screen.blit(self.layer, (0,0))

        pygame.display.flip()


        self.layer.blit(self.screen, (0,0))
        self.current_color = pygame.Color('#000000') #black
        while True:
            for event in pygame.event.get():
                self.screen.blit(self.layer, (0,0))

                if event.type == QUIT:
                    pygame.quit()
                    exit()

                color_changed_flag = False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    for i in range(len(self.color_rects)):
                        if self.Inside(self.color_rects[i]):
                            print(f"Color {self.color_values[i]} selected")
                            self.current_color = self.color[i]
                            self.current_tool.att_color(self.color[i])
                            color_changed_flag = True
                            break
                    if color_changed_flag:
                        continue

                    else:
                        if self.Inside(line_rect):
                            self.current_tool = Line(self.current_color)
                            print("Line tool selected")
                            continue

                        elif self.Inside(polyline_rect):
                            self.current_tool = Polyline(self.current_color)
                            print("Polyline tool selected")
                            continue

                        elif self.Inside(rectangle_rect):
                            self.current_tool = Rectangle(self.current_color)
                            print("Rectangle tool selected")
                            continue

                        elif self.Inside(square_rect):
                            self.current_tool = Square(self.current_color)
                            print("Square tool selected")
                            continue

                        elif self.Inside(circle_rect):
                            self.current_tool = Circle(self.current_color)
                            print("Circle tool selected")
                            continue

                        elif self.Inside(curve_rect):
                            self.current_tool = Curve(self.current_color)
                            print("Curve tool selected")
                            continue

                self.current_tool.draw(self.screen, self.layer, event, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], self.keyboard)
                pygame.display.flip()
            # pygame.display.flip()


    def Inside(self, rect):
        return rect.left <= pygame.mouse.get_pos()[0] <= rect.right and rect.top <= pygame.mouse.get_pos()[1] <= rect.bottom

def main():
    gui = Gui()


if __name__ == "__main__":
    main()
