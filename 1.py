import pygame
#initializing the module
pygame.init()
#let's get the surface
gameDisplay = pygame.display.set_mode((800,600))
#update the surface
# pygame.display.flip() ~~ pygame.display.update()
# So you can use either way, but we will stick with the last one
pygame.display.update()
#quite the game == uninitializing
pygame.quit()
quit()

