import numpy as np
import pygame
import sklearn.preprocessing
import pygame_ai as pai
import time
from concepts import Context


class App:
    windowWidth = 800
    windowHeight = 600
    waiter = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.waiter = Waiter()
        self.dishes = Dishes()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('TEST')
        self._running = True
        self._image_surf = pygame.image.load("cafe.png").convert()
        #self._apple_surf = pygame.image.load("apple.png").convert()

    def on_render(self):
        self._display_surf.blit(self._image_surf, [0, 0])
        #self.dishes.draw(self._display_surf, self._apple_surf)
        #self.aiwaiter.draw(self._display_surf, self._image_surf)
        pygame.display.flip()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            #self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0);
        pygame.quit()


class Dishes:
    x=0
    y=0

    def __int__(self,x,y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Clients:
    x = 0
    y = 0

    def __int__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Kitchen:
    pass


class Order:
    pass


class Waiter(pai.gameobject.GameObject):
    pass


class Field(object):

    def __int__(self):
        pass

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x2 <= x1 <= x2 + bsize and y2 <= y1 <= y2 + bsize:
            return True
        return False



if __name__ == "__main__" :
    pygame.init()
    theApp = App()
    theApp.on_execute()
    pygame.quit()