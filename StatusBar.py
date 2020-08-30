import pygame


class StatusBar():

    def __init__(self, positionX, positionY, height, length, window):
        self.positionY = positionY
        self.positionX = positionX
        self.height = height
        self.length = length
        self.healths = [pygame.image.load("greenbar.png"), pygame.image.load("yellowbar.png"), pygame.image.load("redbar.png"), pygame.image.load("deadbar.png")]

    def health(self, window, num):
        if num == 0:
            window.blit(self.healths[0], (self.positionX, self.positionY))
        elif num == 1:
            window.blit(self.healths[1], (self.positionX, self.positionY))
        elif num == 2:
            window.blit(self.healths[2], (self.positionX, self.positionY))
        elif num == 3:
            window.blit(self.healths[3], (self.positionX, self.positionY))
        else:
            window.blit(self.healths[0], (self.positionX, self.positionY))
