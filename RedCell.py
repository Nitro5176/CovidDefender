import random
import time


class RedCell:

    def __init__(self, color, speed, length, height):
        self.color = color
        self.speed = speed
        self.length = length
        self.height = height
        self.move()

    # Change these later ( default here )
    positionX = 400
    positionY = 450

    def move(self):
        # 1 - Left
        # 2 - Up
        # 3 - Right
        # 4 - Down
        direction = random.randint(1, 4)


        for i in range(5):
            if direction == 1 and self.positionX > 0+3:
                self.positionX -= self.speed
            if direction == 2 and self.positionY > 0+3:
                self.positionY -= self.speed
            if direction == 3 and self.positionX < 570 -3:
                self.positionX += self.speed
            if direction == 4 and self.positionY < 570 -3:
                self.positionY += self.speed

