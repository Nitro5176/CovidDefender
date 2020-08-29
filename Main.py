import pygame
from CovidCell import CovidCell
from CharacterCell import CharacterCell
from RedCell import RedCell

pygame.init()
#size of the window
window = pygame.display.set_mode((600, 600))
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

#temporary variables:
height = 50
length = 50
speed = 5
positionX = 300
positionY = 300

def main():
    # makes the variable running global.
    global running, height, length, speed, positionX, positionY

    red = RedCell((204,0,0), 3, 30, 30)
    covid = CovidCell((255, 0, 255), 3, 30, 30)
    hero = CharacterCell(positionX, positionY, height, length, speed)

    while running:
        # frames:
        clock.tick(30)

        # to exit the game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # when a key is pressed
        keyPressed = pygame.key.get_pressed()
        if keyPressed[pygame.K_UP] and positionY > originY:
            hero.positionY -= speed
        if keyPressed[pygame.K_DOWN] and positionY < screenY - height:
            hero.positionY += speed
        if keyPressed[pygame.K_RIGHT] and positionX < screenX - length:
            hero.positionX += speed
        if keyPressed[pygame.K_LEFT] and positionX > originX:
            hero.positionX -= speed

        covid.move()
        red.move()

        # makes the wallpaper black
        window.fill((0,0,0))

        # One CovidCell

        hero.draw(window)
        pygame.draw.rect(window, covid.color, (covid.positionX, covid.positionY, covid.length, covid.height))
        pygame.draw.rect(window, red.color, (red.positionX, red.positionY, red.length, red.height))

        #needs to refresh otherwise it would show a black screen
        pygame.display.update()
#calling the main method
main()
pygame.quit()
