import random
import time

class CovidCell:

    def __init__(self, color, speed, length, height):
        self.color = color
        self.speed = speed
        self.length = length
        self.height = height
        self.move()

    # Change these later ( default here )
    positionX = 100
    positionY = 100

    def move(self):
        # 1 - Left
        # 2 - Up
        # 3 - Right
        # 4 - Down
        direction = random.randint(1, 4)


        for i in range(5):
            if direction == 1:
                self.positionX -= self.speed
            if direction == 2:
                self.positionY -= self.speed
            if direction == 3:
                self.positionX += self.speed
            if direction == 4:
                self.positionY += self.speed

