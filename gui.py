import pygame 
from pygame.locals import *

class Gui:
    def __init__(self):
        pygame.init()

        self.WIDTH = 900
        self.HEIGHT = 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.layer = pygame.surface.Surface((self.WIDTH, self.HEIGHT))
        self.layer.fill((255,255,255))
        self.screen.fill((255,255,255))
        pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit() 
                    exit()  




def main():
    gui = Gui()


if __name__ == "__main__":
    main()
