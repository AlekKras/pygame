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

display_width = 800
display_height = 600

#let's get the surface
gameDisplay = pygame.display.set_mode((display_width, display_height))
#let's add title==Caption
pygame.display.set_caption('Our game')

gameExit = False

lead_x = display_width/2
lead_y = display_height/2
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

block_size = 20
FPS = 10
#we will create game loop
while not gameExit:
    #create event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -block_size
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = block_size
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -block_size
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = block_size
                lead_x_change = 0
    #create boundaries
    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
        gameExit = True

    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, purple, [lead_x, lead_y,block_size,block_size])


    pygame.display.update()

    #declare FPS
    clock.tick(FPS)

pygame.quit()

quit()
