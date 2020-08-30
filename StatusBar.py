import pygame


class StatusBar():

    def __init__(self, positinoX, positionY, height, length):
        self.height = height
        self.length = length
        self.height = height
        self.length = length
        self.health = [pygame.image.load("greenbar.png"), pygame.image.load("yellowbar.png"),
                       pygame.image.load("redbar.png"), pygame.image.load("deadbar.png")]

    def health(self, window, num):

        if num == 0:
            window.blit(self.health[0], (self.positionX, self.positionY))
        elif num == 1:
            window.blit(self.health[1], (self.positionX, self.positionY))
        elif num == 2:
            window.blit(self.health[2], (self.positionX, self.positionY))
        elif num == 3:
            window.blit(self.health[3], (self.positionX, self.positionY))
        else:
            window.blit(self.health[0], (self.positionX, self.positionY))