import pygame
from CovidCell import CovidCell
from WhiteCell import WhiteCell
from CharacterCell import CharacterCell
from RedCell import RedCell
from StatusBar import StatusBar

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

    red = RedCell((204,0,0), 3, 30, 30)
    covid = CovidCell((255, 0, 255), 3, 30, 30)
    white = WhiteCell((255, 255, 255), 3, 30, 30)
    hero = CharacterCell(positionX, positionY, height, length, speed)
    statusBar = StatusBar(10, 10, 25, 100, window)

    while running:
        # reset
        window.fill((0, 0, 0))

        #creates 3 background animations
        if(counting > 0 and counting < 50):
            # background
            window.blit(background1, (0, 0))
        elif (counting > 50 and counting < 100):
            window.blit(background2, (0, 0))
        elif(counting >= 100 and counting < 150):
            window.blit(background3, (0, 0))
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

        covid.move()
        red.move()
        white.move()

        rightSide = hero.positionX + hero.length
        leftSide = hero.positionX
        topSide = hero.positionY
        bottomSide = hero.positionY + hero.height

        # Check if User hits the red Cell
        if rightSide >= red.positionX and rightSide <= (red.positionX + red.length): # inside from left to right
          if topSide >= red.positionY and topSide <= ( red.positionY + red.height):
              print("from right-top")
              if (healthBar > 0 and healthBar <= 3):
                  healthBar -= 1

          if bottomSide >= red.positionY and bottomSide <= ( red.positionY + red.height):
              print("from right-bottom")
              if (healthBar > 0 and healthBar <= 3):
                  healthBar -= 1

        if leftSide >= red.positionX and leftSide <= (red.positionX + red.length): # inside from right to left
          if topSide >= red.positionY and topSide <= ( red.positionY + red.height):
              print("from left-top")
              if (healthBar > 0 and healthBar <= 3):
                  healthBar -= 1

          if bottomSide >= red.positionY and bottomSide <= ( red.positionY + red.height):
              print("from left-bottom")
              if (healthBar > 0 and healthBar <= 3):
                  healthBar -= 1

        # Virus coll with user
        if rightSide >= covid.positionX and rightSide <= (covid.positionX + covid.length): # inside from left to right
          if topSide >= covid.positionY and topSide <= ( covid.positionY + covid.height):
              print("from right-top")

              if(healthBar < 3 ):
                healthBar += 1


          if bottomSide >= covid.positionY and bottomSide <= ( covid.positionY + covid.height):
              print("from right-bottom")

              if(healthBar < 3 ):
                healthBar += 1

        if leftSide >= covid.positionX and leftSide <= (covid.positionX + covid.length): # inside from right to left
          if topSide >= covid.positionY and topSide <= ( covid.positionY + covid.height):
              print("from left-top")
              if(healthBar < 3 ):
                healthBar += 1

          if bottomSide >= covid.positionY and bottomSide <= ( covid.positionY + covid.height):
              print("from left-bottom")

              if(healthBar < 3 ):
                healthBar += 1

        # White Cell coll with user
        if rightSide >= white.positionX and rightSide <= (white.positionX + white.length): # inside from left to right
          if topSide >= white.positionY and topSide <= ( white.positionY + white.height):
              print("from right-top")

              if(healthBar < 3 ):
                healthBar += 1


          if bottomSide >= white.positionY and bottomSide <= ( white.positionY + white.height):
              print("from right-bottom")

              if(healthBar < 3 ):
                healthBar += 1

        if leftSide >= white.positionX and leftSide <= (white.positionX + white.length): # inside from right to left
          if topSide >= white.positionY and topSide <= ( white.positionY + white.height):
              print("from left-top")
              if(healthBar < 3 ):
                healthBar += 1

          if bottomSide >= white.positionY and bottomSide <= ( white.positionY + white.height):
              print("from left-bottom")

              if(healthBar < 3 ):
                healthBar += 1

        # makes the wallpaper black
        #window.fill((0,0,0))

        # One CovidCell
        statusBar.health(window, healthBar)
        hero.draw(window, heroPosition)
        covid.draw(window)
        red.draw(window)
        white.draw(window)
        counting += 1
        # needs to refresh otherwise it would show a black screen
        pygame.display.update()


# calling the main method
main()
pygame.quit()
