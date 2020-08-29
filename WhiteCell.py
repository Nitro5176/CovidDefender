import random
import time

class WhiteCell:
    radius = 50
    color = (255, 255, 255)
    speed = 8

    #random starting positions`
    starty = random.randint(0, 600)
    startx = random.randint(0, 600)

    def move(self):
        # 1 - Left
        # 2 - Up
        # 3 - Right
        # 4 - Down
        direction = random.randint(1, 4)

        t_end = time.time() + 60

    while time.time() <  t_end:
        if direction == 1:
            self.startx -= self.speed
        if direction == 2:
            self.starty -= self.speed
        if direction == 3:
            self.startx += self.speed
        if direction == 4:
            self.starty += self.speed

        #frames:
        clock.tick(30)



