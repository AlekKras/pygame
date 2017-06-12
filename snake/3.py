import pygame
#initializing the module
pygame.init()

#let's get the surface
gameDisplay = pygame.display.set_mode((800,600))

#let's add title==Caption
pygame.display.set_caption('Our game')

#update the surface
pygame.display.update()

gameExit = False
#we will create game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

#quite the game == uninitializing
pygame.quit()

quit()
