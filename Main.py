import time
import pygame

from CovidCell import CovidCell
from WhiteCell import WhiteCell
from CharacterCell import CharacterCell
from RedCell import RedCell
from StatusBar import StatusBar
import random

pygame.init()
#size of the window
window = pygame.display.set_mode((600, 600))
#backgrounds
background1 = pygame.image.load("topbackground.png")
background2 = pygame.image.load("middlebackground.png")
background3 = pygame.image.load("bottombackground.png")
#display name
pygame.display.set_caption("Covid Defender")
#clock (for frames per second)
clock = pygame.time.Clock()

print("Welcome to CovidDefender!")
print("   ooooooooooooooo")
print(" o       o         o")
print("o        o          o")
print(" o       o         o")
print("   ooooooooooooooo")
print("")
print("     \  |  /")
print("   \ o  o  o /")
print("  \ o       o /")
print("   o  x   x  o")
print("- o           o -")
print("   o  vvvvv  o")
print("  / o       o \ ")
print("   / o  o  o \ ")
print("    /   |   \ ")

#Game Over Text
gameOver = pygame.font.Font('freesansbold.ttf', 32)
gameOver_surface = gameOver.render('Game Over', True, (255, 255, 255), (0, 0, 0))
gameOver_rect = gameOver_surface.get_rect()
gameOver_rect.center = (300,300)

#Global variables:
running = True
screenX = 600
screenY = 600
originX = 0
originY = 0
heroPosition = 0
#0->3 green, yellow, red, dead
healthBar = 0
#positioning
height = 50
length = 50
speed = 5
positionX = 300
positionY = 300
#background countdown and switch
counting = 0





def main():
    # makes the variable running global.
    global running, height, length, speed, positionX, positionY, heroPosition, healthBar, counting


    redObjects = createListObject(RedCell, 5, 1)
    covidObjects = createListObject(CovidCell, 5, 3)
    whiteObjects = createListObject(WhiteCell, 5, 2)
    hero = CharacterCell(positionX, positionY, height, length, speed)
    statusBar = StatusBar(10, 10, 25, 100, window)

    while running:
        # reset
        window.fill((0, 0, 0))

        #creates 3 background animations
        if(counting > 0 and counting < 50):
            # background
            window.blit(background3, (0, 0))
        elif (counting > 50 and counting < 100):
            window.blit(background2, (0, 0))
        elif(counting >= 100 and counting < 150):
            window.blit(background1, (0, 0))
        elif(counting >= 150):
            counting = 0
        # frames:
        clock.tick(30)

        # to exit the game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # when a key is pressed
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_UP] and hero.positionY > originY:
            heroPosition = 1
            hero.positionY -= speed
        if keyPressed[pygame.K_DOWN] and hero.positionY < screenY - hero.height:
            heroPosition = 2
            hero.positionY += speed
        if keyPressed[pygame.K_RIGHT] and hero.positionX < screenX - hero.length:
            heroPosition = 4
            hero.positionX += speed
        if keyPressed[pygame.K_LEFT] and hero.positionX > originX:
            heroPosition = 3
            hero.positionX -= speed

        for i in range(5):
            whiteObjects[i].move(hero.positionX, hero.positionY)
        for i in range(5):
            covidObjects[i].move(hero.positionX, hero.positionY)
        for i in range(5):
            redObjects[i].move()

        rightSide = hero.positionX + hero.length
        leftSide = hero.positionX
        topSide = hero.positionY
        bottomSide = hero.positionY + hero.height

        # FOR THE multiple RED CELLS check if it hits
        for i in range(5):
            if redObjects[i].did_hit(leftSide, topSide, rightSide, bottomSide):
                if (healthBar > 0 and healthBar <= 3) and redObjects[i].isVisible:
                    healthBar -= 1
                redObjects[i].set_visibility(False)


        # Virus coll with user
        for i in range(5):
            if covidObjects[i].did_hit(leftSide, topSide, rightSide, bottomSide):
                if (healthBar < 3) and covidObjects[i].isVisible:
                    healthBar += 1
                covidObjects[i].set_visibility(False)

        # White Cell coll with user
        for i in range(5):
            if whiteObjects[i].did_hit(leftSide, topSide, rightSide, bottomSide):
                if (healthBar < 3) and whiteObjects[i].isVisible:
                    healthBar += 1
                whiteObjects[i].set_visibility(False)


        # makes the wallpaper black
        #window.fill((0,0,0))

        # One CovidCell
        statusBar.health(window, healthBar)
        hero.draw(window, heroPosition)


        for i in range(len(covidObjects)):
            if covidObjects[i].isVisible:
                covidObjects[i].draw(window)
        for i in range(len(whiteObjects)):
            if whiteObjects[i].isVisible:
                whiteObjects[i].draw(window)
        for i in range(len(redObjects)):
            if redObjects[i].isVisible:
                redObjects[i].draw(window)
                
        counting += 1

        if healthBar == 3:
            window.blit(gameOver_surface, gameOver_rect)
            running = False
        # needs to refresh otherwise it would show a black screen
        pygame.display.update()


def createListObject(object, num, type):
    Objects = list()
    for i in range(num):
        steps = random.randint(1,4)
        positionX = random.randint(0, 600)
        positionY = random.randint(0, 600)

        #red blood cells
        if(type == 1):
            Objects.append(object((204,0,0), steps, 30, 30, positionX, positionY))
        #white blood cells
        elif (type == 2):
            Objects.append(object((204, 0, 0), steps, 30, 30, positionX, positionY))
        #covid cells
        elif(type == 3):
            Objects.append(object((204, 0, 0), steps, 30, 30, positionX, positionY))

    return Objects

# calling the main method
main()
time.sleep(3)
pygame.quit()