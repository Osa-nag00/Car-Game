import pygame
import time
import random

pygame.init()

# window size
display_width = 800
display_height = 600
car_width = 27
car_height = 60

# colors for pygame to use
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
block_color = (53, 115, 255)
# opening the window, setting it's name
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

# importing car image from directory
carImg = pygame.image.load('racecar.png')
Explo = pygame.image.load('Explo.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, block_color, [thingx, thingy, thingw, thingh])


# function to display car after importing it
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')


def game_loop():
    # where the car spawns
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    dodged = 0

    # basically a quit function
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # moving the car
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            # this makes it so you can hold left or right down to keep going instead of repressing over and over
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color):

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed

        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            gameExit = True
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            # score
            dodged += 1
            thing_speed += 1

        # collision with blocks, first coded collision detection
        if y < thing_starty + thing_height and (y + car_height > thing_starty):
            if x + car_width > thing_startx and x < thing_startx + thing_width:
                crash()
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
