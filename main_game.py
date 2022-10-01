import pygame

#Missions:

#TODO --> Set up the pygame. Start to set up classes for each object and study this library's basics and advanced attributes and subjects.

#Initialize the PyGame library 
pygame.init()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 600

#Screen creation including sizes
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Supermarket Game')

#Program running loop
run_program = True
while run_program:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_program = False
            print('Window closed by the user')