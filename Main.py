import pygame

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

#temporary variables:
height = 50
length = 50
speed = 5
positionX = 300
positionY = 300

def main():
    #makes the variable running global.
    global running, height, length, speed, positionX, positionY

    while running:
        #frames:
        clock.tick(30)

        #to exit the game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #when a key is pressed
        keyPressed = pygame.key.get_pressed()

        if keyPressed[pygame.K_UP]:
            positionY -= speed
        if keyPressed[pygame.K_DOWN]:
            positionY += speed
        if keyPressed[pygame.K_RIGHT]:
            positionX += speed
        if keyPressed[pygame.K_LEFT]:
            positionX -= speed

        #makes the wallpaper black
        window.fill((0,0,0))
        pygame.draw.rect(window, (0,255,0), (positionX, positionY, length, height))
        #needs to refresh otherwise it would show a black screen
        pygame.display.update()
#calling the main method
main()
pygame.quit()
