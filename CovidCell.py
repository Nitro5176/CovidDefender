import random
import pygame
import time

class CovidCell:
    isVisible = True

    def __init__(self, color, speed, length, height, positionX, positionY):
        self.color = color
        self.speed = speed
        self.length = length
        self.height = height
        self.positionX = positionX
        self.positionY = positionY
        self.move()
        self.covidCell = pygame.image.load("Covid.png")

    # Change these later ( default here )
    #positionX = random.randint(0, 600)
    #ositionY = random.randint(0, 600)

    def move(self):
        # 1 - Left
        # 2 - Up
        # 3 - Right
        # 4 - Down
        direction = random.randint(1, 4)


        for i in range(5):
            if direction == 1 and self.positionX > 0 + 3:
                self.positionX -= self.speed
            if direction == 2 and self.positionY > 0 + 3:
                self.positionY -= self.speed
            if direction == 3 and self.positionX < 570 - 3:
                self.positionX += self.speed
            if direction == 4 and self.positionY < 570 - 3:
                self.positionY += self.speed

    def draw(self, window):
        window.blit(self.covidCell, (self.positionX, self.positionY))

    def set_visibility(self, is_visible):
        self.isVisible = is_visible

    def did_hit(self, leftSide, topSide, rightSide, bottomSide):
        # Virus coll with user
        if rightSide >= self.positionX and rightSide <= (self.positionX + self.length):  # inside from left to right
            if topSide >= self.positionY and topSide <= (self.positionY + self.height):
                print("from right-top")

                # if (healthBar < 3) and covid.isVisible:
                #     healthBar += 1
                # covid.set_visibility(False)
                return True

            if bottomSide >= self.positionY and bottomSide <= (self.positionY + self.height):
                print("from right-bottom")

                # if (healthBar < 3) and covid.isVisible:
                #     healthBar += 1
                # covid.set_visibility(False)
                return True

        if leftSide >= self.positionX and leftSide <= (self.positionX + self.length):  # inside from right to left
            if topSide >= self.positionY and topSide <= (self.positionY + self.height):
                print("from left-top")
                # if (healthBar < 3) and covid.isVisible:
                #     healthBar += 1
                # covid.set_visibility(False)
                return True

            if bottomSide >= self.positionY and bottomSide <= (self.positionY + self.height):
                print("from left-bottom")

                # if (healthBar < 3) and covid.isVisible:
                #     healthBar += 1
                # covid.set_visibility(False)
                return True