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
#upload image for our snake head
img = pygame.image.load('snake.png')

clock = pygame.time.Clock()

block_size = 20
FPS = 10
##we create direction variable for our snake head
##the snake starts moving right at the start
direction = "right"
#font-size and font-family
font = pygame.font.SysFont("Arial", 25)
#let's define snake
##  XnY = list of two elements: X and Y
def snake(block_size, snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

#let's define apple
def apple(randAppleX, randAppleY, appleThickness):
    pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])
#passing text
def text_objects(text, color):
    textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()
#let's make messages
def message_to_screen(msg,color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)

#we will create game loop
def gameLoop():
    #we make direction global so we can reference it
    global  direction
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    # place Apple
    randAppleX = round((random.randrange(0, display_width - block_size)))
    randAppleY = round((random.randrange(0, display_height - block_size)))

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to continue or Q to quit", blue)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
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
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
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
        # x axis crossover
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness:
            #y axis crossover
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size))
                randAppleY = round(random.randrange(0, display_height - block_size))
                snakeLength += 1
        #declare FPS
        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
