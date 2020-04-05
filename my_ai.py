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
        self.waiter = Waiter()
        self.dishes = Dishes()

    def on_init(self):
        pygame.init()
        #display creating
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        #window name
        pygame.display.set_caption('TEST')
        self._running = True
        self._image_surf = pygame.image.load("cafe.png").convert()
        #self._apple_surf = pygame.image.load("apple.png").convert()

    def on_render(self):
        #background
        self._display_surf.blit(self._image_surf, [0, 0])
        pygame.display.flip()

    #running a program
    def to_run(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                #self._running = False
                pygame.quit()

            self.on_render()

            time.sleep(50.0 / 1000.0);



class Dishes:
    #to do
    x=0
    y=0

    def __int__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Clients:
    #to do
    x = 0
    y = 0

    def __int__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Kitchen:
    #to do or delete
    pass


class Order:
    #to do
    pass


class Waiter(pai.gameobject.GameObject):
    #to do
    pass


class Field(object):
    #To do
    def __int__(self):
        pass





if __name__ == "__main__" :
    pygame.init()
    theApp = App()
    theApp.to_run()
    pygame.quit()