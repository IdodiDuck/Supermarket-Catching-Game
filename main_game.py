import pygame

#Missions:

#TODO --> Set up the pygame. Start to set up classes for each object and study this library's basics and advanced attributes and subjects.

#Initialize the PyGame library 

pygame.init()

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 630

#Screen creation including sizes
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption('Supermarket Game')

walkright_pic = pygame.image.load('ShoppingCartRight.png')
walkleft_pic = pygame.image.load('ShoppingCartLeft.png') #D:\Ido.Files\Documents\GitHub\PyGame-Project\Shopping Cart Animations
 
# Characteristics

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
    global walkCount

    screen.blit(background, (0, 0)) #Draws the background
    pygame.display.update() #Updates background and displays the background I downloaded.

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkleft_pic, (maincart.x, maincart.y))
        walkCount += 1

    elif right:
        screen.blit(walkright_pic, (maincart.x, maincart.y))
    
    else:
        screen.blit(walkright_pic, (maincart.x, maincart.y))


run_program = True
clock = pygame.time.Clock()
maincart = cart(50, WINDOW_HEIGHT - walkleft_pic.get_height() -130, 50, 50)

walkCount = 0 
left, right = False, False

#Main prorgam loop
while run_program:
    clock.tick(40)
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_program = False
            print('Window closed by the user')

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_LEFT] and maincart.x > maincart.vel:
        maincart.x -= maincart.vel
        left = True
        right = False

    elif KEYS[pygame.K_RIGHT] and maincart.x < 570 - maincart.width - maincart.vel:
        maincart.x += maincart.vel
        left = False
        right = True

    # else:
    #     right = False
    #     left = False
    #     walkCount = 0
        
    redrawGameWindow()  

    pygame.display.update()
    
pygame.quit()