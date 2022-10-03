import pygame
import random

#Missions:

#TODO --> Set up the pygame. Start to set up classes for each object and study this library's basics and advanced attributes and subjects.

#Initialize the PyGame library 
pygame.init()

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

#Screen creation including sizes
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Supermarket Game')

# Characteristics

x = 50
y = 425
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

#Program running loop
run_program = True

while run_program:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_program = False
            print('Window closed by the user')

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_LEFT] and x > vel:
        x -= vel

    if KEYS[pygame.K_RIGHT] and x < 500 -  width - vel:
        x += vel
        
    if not (isJump):
        if KEYS[pygame.K_UP] and y > vel:
            y -= vel

        if KEYS[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if KEYS[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), (x, y, width, height))
    pygame.display.update()

pygame.quit()