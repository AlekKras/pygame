import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Tanks')

# icon = pygame.image.load("apple.png")
# pygame.display.set_icon(icon)

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 80, 80)
hover_red = (255,0,0)

green = (34, 177, 76)
hover_green = (0,255,0)

yellow = (240,220,40)
hover_yellow = (255,255,0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

#let's define Tank's width and height
tankWidth = 40
tankHeight = 20

gunWidth = 5
wheelWidth = 3


def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, button_x, button_y, button_width, button_height, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((button_x+(button_width/2)),(button_y+(button_height/2)))
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, color, hover_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() # we will get tuple (0,0,0) for each button clicked on the mouse
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, hover_color, (x,y, width, height))
        if click[0] == 1 and action!= None:
            if action == "Exit":
                pygame.quit()
                quit()
            if action == "Controls":
                game_controls()
            if action == "Play":
                gameLoop()

    else:
        pygame.draw.rect(gameDisplay, color, (x,y,width,height))
    text_to_button(text, black, x,y, width, height)

def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)
#that's probable one of the hardest functions to write
def tank (x,y, gunPos):
    x = int(x)
    y = int(y)
    #position of tank's gun
    possibleGun = [(x - 27, y - 5),
                   (x - 26, y - 8),
                   (x - 25, y -11),
                   (x - 23, y - 15),
                   (x - 20, y - 17),
                   (x - 18, y - 19),
                   (x - 15, y - 21),
                   (x - 13, y - 23),
                   (x - 11, y - 25),
                   (x - 8, y -26)
                   ]
    #tank body
    pygame.draw.circle(gameDisplay, black, (x,y), int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))
    #tank's gun
    pygame.draw.line(gameDisplay, black, (x,y), possibleGun[gunPos], gunWidth)
    #tank's wheels
    startZ = 20
    for z in range(6):
        pygame.draw.circle(gameDisplay, black, (x - startZ, y + 20), wheelWidth)
        startZ -= 8

def obstacle():
    x_location = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)

def game_controls():
    g_controls = True

    while g_controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        message_to_screen("Controls", green, -175, size="large")
        message_to_screen("Fire: Spacebar", black, -30)
        message_to_screen("More Turret: Up and Down arrows", black, 10)
        message_to_screen("Move Tank: Left and Right arrows", black, 50)
        message_to_screen("Pause: P", black, 90)
        # add text to buttons
        button("Play", 250, 500, 125, 50, green, hover_green, action="Play")
        button("Exit", 450, 500, 125, 50, red, hover_red, action="Exit")

        pygame.display.update()

        clock.tick(15)


def pause():
    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", black, 25)
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

        clock.tick(5)




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
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks!", green, -100, size="large")
        message_to_screen("The objective is to shoot and destroy", black, -30)
        message_to_screen("the enemy tank before they destroy you.", black, 10)
        message_to_screen("The more enemies you destroy, the harder they get.", black, 50)

        #add text to buttons
        button("Play", 150,500,125,50, green, hover_green, action="Play")
        button("Controls", 350, 500, 125, 50,yellow, hover_yellow, action="Controls")
        button("Exit", 550, 500, 125, 50, red, hover_red, action="Exit")

        pygame.display.update()

        clock.tick(15)

def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    # let's create Tank
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    # Tank's moves
    tankMove = 0

    currentGunPosition = 0
    changeGun = 0

    while not gameExit:

        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove -= 5

                elif event.key == pygame.K_RIGHT:
                    tankMove += 5

                elif event.key == pygame.K_UP:
                    changeGun += 1

                elif event.key == pygame.K_DOWN:
                    changeGun -= 1

                elif event.key == pygame.K_p:
                    pause()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeGun = 0



        gameDisplay.fill(white)

        mainTankX += tankMove


        #let's call tank()
        currentGunPosition += changeGun

        if currentGunPosition > 9:
            currentGunPosition = 9
        elif currentGunPosition <0:
            currentGunPosition = 0

        tank(mainTankX, mainTankY, currentGunPosition)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
