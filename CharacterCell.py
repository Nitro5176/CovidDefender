import pygame
import random

class CharacterCell():

    def __init__(self, positionX, positionY, height, length, speed):
        self.positionX = positionX
        self.positionY = positionY
        self.height = height
        self.length = length
        self.speed = speed
        self.character = [pygame.image.load("CharacterShip.png"), pygame.image.load("piishipdown.png"),
                          pygame.image.load("piishipleft.png"), pygame.image.load("piishipright.png")]

    def draw(self, window, num,):
        #1 == up
        #2 == down
        #3 == left
        #4 == right
        if num == 1:
            window.blit(self.character[0], (self.positionX, self.positionY))
        elif num == 2:
            window.blit(self.character[1], (self.positionX, self.positionY))
        elif num == 3:
            window.blit(self.character[2], (self.positionX, self.positionY))
        elif num == 4:
            window.blit(self.character[3], (self.positionX, self.positionY))
        else:
            window.blit(self.character[0], (self.positionX, self.positionY))