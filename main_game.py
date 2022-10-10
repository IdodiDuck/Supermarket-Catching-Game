import pygame
import random

#Missions:

#TODO --> Set up the pygame. Start to set up classes for each object and study this library's basics and advanced attributes and subjects.

#Initialize the PyGame library 

pygame.init()

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 630

#Screen creation including sizes
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Supermarket Game')

# Characteristics

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.isJump = False
        self.jumpCount = 10

background = pygame.image.load('Game_SuperMarket_Banner.png')

#Function which is Displaying the background

def redrawGameWindow():
    screen.blit(background, (0, 0)) #Draws the background
    pygame.display.update() #Updates background and displays the background I downloaded.

run_program = True
clock = pygame.time.Clock()
obj = player(50, 50, 50, 50)

while run_program:
    clock.tick(40)
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_program = False
            print('Window closed by the user')

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_LEFT] and obj.x > obj.vel:
        obj.x -= obj.vel

    if KEYS[pygame.K_RIGHT] and obj.x < 750 - obj.width - obj.vel:
        obj.x += obj.vel
        
    if not (obj.isJump):
        if KEYS[pygame.K_UP] and obj.y > obj.vel:
            obj.y -= obj.vel

        if KEYS[pygame.K_DOWN] and obj.y < 150 - obj.height - obj.vel:
            obj.y += obj.vel

        if KEYS[pygame.K_SPACE]:
            obj.isJump = True
    else:
        if obj.jumpCount >= -10:
            neg = 1
            if obj.jumpCount < 0:
                neg = -1
            obj.y -= (obj.jumpCount ** 2) * 0.5 * neg
            obj.jumpCount -= 1

        else:
            obj.isJump = False
            obj.jumpCount = 10

    redrawGameWindow()    
    pygame.draw.rect(screen, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (obj.x, obj.y, obj.width, obj.height))
    pygame.display.update()

pygame.quit()
