import pygame
#we will import time for timer
import time
#for placing apples we would need random
import random
#initializing the module
pygame.init()

#let's declare colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (255, 128,0)
yellow = (255,255,0)
green = (0,155,0)
lightBlue = (0,255,255)
blue = (0,0,255)
purple = (127,0,255)

display_width = 800
display_height = 600

#let's get the surface
gameDisplay = pygame.display.set_mode((display_width, display_height))
#let's add title==Caption
pygame.display.set_caption('Our game')

clock = pygame.time.Clock()

block_size = 20
FPS = 10
#font-size
font = pygame.font.SysFont(None, 25)
#let's define snake
# XnY = list of two elements: X and Y
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

#let's define apple
def apple(randAppleX, randAppleY, appleThickness):
    pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])
#let's make messages
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text,[display_width/4, display_height/2])

#we will create game loop
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    # place Apple
    randAppleX = round((random.randrange(0, display_width - block_size)) / block_size) * block_size
    randAppleY = round((random.randrange(0, display_height - block_size)) / block_size) * block_size

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to continue or Q to quit", blue)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

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
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        #create Snake rule: can't go over itself
        for eachBlock in snakeList[:-1]:
            if eachBlock == snakeHead:
                #basically, when the head touches the rest of body, the game should end
                gameOver = True

        snake(block_size, snakeList)

        appleThickness = 30

        apple(randAppleX, randAppleY, appleThickness)

        pygame.display.update()

        if lead_x >= randAppleX and lead_x <= randAppleX + appleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + appleThickness:
                randAppleX = round((random.randrange(0, display_width - block_size)) / block_size) * block_size
                randAppleY = round((random.randrange(0, display_height - block_size)) / block_size) * block_size
                snakeLength +=1




        #declare FPS
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
