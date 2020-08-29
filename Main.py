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

def main():
    #makes the variable running global.
    global running

    while running:
        #frames:
        clock.tick(30)

        #to exit the game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #makes the wallpaper black
        window.fill((0,0,0))

#calling the main method
main()
pygame.quit()
