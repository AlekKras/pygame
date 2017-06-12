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

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()
#we will create game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -5
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 5
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -5
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 5
                lead_x_change = 0


    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, purple, [lead_x, lead_y,20,20])


    pygame.display.update()

    #declare FPS
    clock.tick(30)

pygame.quit()

quit()
