import pygame, random

#Missions:

#TODO --> Set up the pygame. Start to set up classes for each object and study this library's basics and advanced attributes and subjects.

#Initialize the PyGame library and text
pygame.init()

pygame.font.init()
leveltext = pygame.font.SysFont("bahnschrift", 60)
scoretext = pygame.font.SysFont('bahnschrift', 40)

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 630

#Screen creation including sizes
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Supermarket Game')

score = 0
level = 1

#Animations pictures for the main-cart object
walkright_pic = pygame.image.load('ShoppingCartRight.png')
walkleft_pic = pygame.image.load('ShoppingCartLeft.png')

# Classes and Attributes of all the objects
class cart(object):
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
    global walkCount, level, score
    
    screen.blit(background, (0, 0)) #Draws the background
    leveltextTBD = leveltext.render(f'Level: {level}', 1, (0, 0, 0))
    scoretextTBD = scoretext.render(f'Score: {score}', 1, (0, 0, 0))

    screen.blit(leveltextTBD, (2, 0))
    screen.blit(scoretextTBD, (2, 68))
    pygame.display.update() #Updates background and displays the background I downloaded.

    if left:
        screen.blit(walkleft_pic, (maincart.x, maincart.y))
        walkCount += 1

    elif right:
        screen.blit(walkright_pic, (maincart.x, maincart.y))
    
    else:
        screen.blit(walkright_pic, (maincart.x, maincart.y))


run_program = True
clock = pygame.time.Clock()
maincart = cart(50, WINDOW_HEIGHT - walkleft_pic.get_height() - 130, 50, 50)

walkCount = 0 
left, right = False, False

#Main prorgam loop
while run_program:
    clock.tick(40) #40 Frames Per Second (FPS)
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_program = False
            print('Window closed by the user')

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_LEFT] and maincart.x > maincart.vel -  maincart.width + 39: #Left Movement
        maincart.x -= maincart.vel
        left = True
        right = False

    elif KEYS[pygame.K_RIGHT] and maincart.x < 600 - maincart.width - maincart.vel: #Right Movement
        maincart.x += maincart.vel
        left = False
        right = True
   
    redrawGameWindow()

    pygame.display.update()