import pygame
#initializing the module
pygame.init()

#let's declare colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255, 128,0)
yellow = (255,255,0)
green = (0,255,0)
lightBlue = (0,255,255)
blue = (0,0,255)
purple = (127,0,255)

#let's get the surface
gameDisplay = pygame.display.set_mode((800,600))
#let's add title==Caption
pygame.display.set_caption('Our game')

gameExit = False
#let's start at upper left corner
lead_x = 0
lead_y = 0
lead_x_change = 0
#we will create game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10

    lead_x += lead_x_change
    #we choose white as our background color
    gameDisplay.fill(white)
    #add some other graphics
    pygame.draw.rect(gameDisplay, purple, [lead_x, lead_y,50,50])
    pygame.display.update()
#quite the game == uninitializing
pygame.quit()

quit()
