import pygame
import random

class CharacterCell():

    def __init__(self, positionX, positionY, height, length, speed):
        self.positionX = positionX
        self.positionY = positionY
        self.height = height
        self.length = length
        self.speed = speed
        self.character = pygame.image.load("CharacterShip.png")

    def draw(self, window):
        window.blit(self.character, (self.positionX, self.positionY))


