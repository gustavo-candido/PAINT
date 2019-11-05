import pygame 
from pygame.locals import *
import os
class Gui:
    def __init__(self):
        pygame.init()

        self.WIDTH = 900
        self.HEIGHT = 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.layer = pygame.surface.Surface((self.WIDTH, self.HEIGHT))
        self.layer.fill((255,255,255))
        self.screen.fill((255,255,0))
       
        self.set_tools()
        self.screen.blit(self.layer, (0,0))


        pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit() 
                    exit()  


    def set_tools(self):
        line_icon = pygame.image.load(os.path.abspath('Paint/PAINT/pictures/line.png'))
        line_icon = pygame.transform.scale(line_icon, (50,50))
        line_rect = line_icon.get_rect()
        line_rect.move_ip(0, 0)
        self.layer.blit(line_icon, line_rect)





def main():
    gui = Gui()


if __name__ == "__main__":
    main()
