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
pygame.display.set_caption('Snake Game')
#make a logo icon
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)
#upload image of our snake head
img = pygame.image.load('snake.png')
#upload image of our apple
appleimg = pygame.image.load('apple.png')
clock = pygame.time.Clock()
appleThickness = 30
block_size = 20
FPS = 10
##we create direction variable for our snake head
##the snake starts moving right at the start
direction = "right"
#font-size and font-family
smallFont = pygame.font.SysFont("comicsansms", 25)
mediumFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 85)

#let's make a pause function
def pause():
    paused = True
    message_to_screen("The game is paused",
                      green,
                      -100,
                      font_size="medium")
    message_to_screen("Press C to continue or Q to quit",
                      blue,
                      25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #if you want to have a new window, uncomment the line below
        #gameDisplay.fill(white)

#let's make a score
def score(score):
    text = smallFont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [20,10])
#create function for random apple
def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - appleThickness))
    randAppleY = round(random.randrange(0, display_height - appleThickness))
    return randAppleX,randAppleY

#let's make intro screen
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Welcome to the SNAKE game",
                          green,
                          -120,
                          font_size="medium")
        message_to_screen("The objective of the game is to eat red apples",
                          blue,
                          -50,
                          font_size="small")
        message_to_screen("The more you eat, the longer you get",
                          blue,
                          20,
                          font_size="small")
        message_to_screen("Press C to play, P to pause or Q to quit",
                          blue,
                          90,
                          font_size="small")
        pygame.display.update()
        clock.tick(15)

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
#passing text
def text_objects(text, color, font_size):
    if font_size == "small":
        textSurf = smallFont.render(text, True, color)
    elif font_size == "medium":
        textSurf = mediumFont.render(text, True, color)
    elif font_size == "large":
        textSurf = largeFont.render(text, True, color)
    return textSurf, textSurf.get_rect()
#let's make messages
def message_to_screen(msg,color, y_displace = 0, font_size = "small"):
    textSurf, textRect = text_objects(msg, color, font_size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

#we will create game loop
def gameLoop():
    #we make direction global so we can reference it
    global  direction
    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    # place Apple

    randAppleX, randAppleY = randAppleGen()

    while not gameExit:
        if gameOver == True:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              font_size="large")
            message_to_screen("Press C to play again or Q to quit",
                              blue,
                              y_displace=50,
                              font_size="small")
            pygame.display.update()
        while gameOver == True:
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

                elif event.key == pygame.K_p:
                    pause()
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

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        #call score() function
        score(snakeLength-1)


        pygame.display.update()
        # x axis crossover
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + appleThickness > randAppleX and lead_x + appleThickness < randAppleX + appleThickness:
            #y axis crossover
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + appleThickness > randAppleY and lead_y + appleThickness < randAppleY + appleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
        #declare FPS
        clock.tick(FPS)
    pygame.quit()
    quit()
game_intro()
gameLoop()
