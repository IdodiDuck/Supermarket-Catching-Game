import pygame, random, time

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
background = pygame.image.load('Game_SuperMarket_Banner.png')

score = 0
level = 1

#Animations pictures for the main-cart object
walkright_pic = pygame.image.load('ShoppingCartRight.png')
walkleft_pic = pygame.image.load('ShoppingCartLeft.png')

# Classes and Attributes of all the objects
class cart(object):
    '''
    Main Cart, the object that the user controls. The cart should catch the falling food items before they reach the floor
    Cart inherits from the class object
    '''
    def __init__(self, x, y, width, height): #Attributes of the cart
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20

class bread(object):
    pic = pygame.image.load('Bread_Obj.png')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pts = 5
        
class drinks(object):
    pic = pygame.image.load('Drinks_Obj.png')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pts = 10

class eggs(object):
    pic = pygame.image.load('Eggs_Obj.png')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pts = 5

class milk(object):
    pic = pygame.image.load('Milk_Obj.png')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pts = 5

class veg(object):
    pic = pygame.image.load('Vegetables_Obj.png')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pts = 5

class meat(object):
    pic = pygame.image.load('Meat_Obj.png')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pts = 10

class goldencandy(object):
    pic = pygame.image.load('GoldenCandy_Obj.png')
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pts = 100

food_tup = (bread, drinks, eggs, meat, veg, milk)

#Function which is drawing the images in the game and updates the display in every frame
def redrawGameWindow():
    current_food = random.choice(food_tup)
    current_food = current_food(random.randint(0, WINDOW_WIDTH - 5), current_food.pic.get_height())
    global walkCount, level, score

    screen.blit(background, (0, 0)) #Draws the background
    leveltextTBD = leveltext.render(f'Level: {level}', 1, (0, 0, 0))
    scoretextTBD = scoretext.render(f'Score: {score}', 1, (0, 0, 0))

    screen.blit(leveltextTBD, (2, 0)) #Drawing both texts of Level and Score
    screen.blit(scoretextTBD, (2, 68))

    screen.blit(current_food.pic, (current_food.x, current_food.y))
    time.sleep(5)
    current_food.y += 10

    if current_food.y > WINDOW_HEIGHT:
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