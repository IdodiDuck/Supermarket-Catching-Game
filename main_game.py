import pygame, random

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
    def __init__(self, x, y, respawn):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5
    
    def draw(self):
        screen.blit(bread.pic, (self.x, self.y))
        
class drinks(object):
    pic = pygame.image.load('Drinks_Obj.png')
    def __init__(self, x, y, respawn):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 10

    def draw(self):
        screen.blit(drinks.pic, (self.x, self.y))

class eggs(object):
    pic = pygame.image.load('Eggs_Obj.png')
    def __init__(self, x, y, respawn):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5

    def draw(self):
        screen.blit(eggs.pic, (self.x, self.y))

class milk(object):
    pic = pygame.image.load('Milk_Obj.png')
    def __init__(self, x, y, respawn):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5

    def draw(self):
        screen.blit(milk.pic, (self.x, self.y))

class veg(object):
    pic = pygame.image.load('Vegetables_Obj.png')
    def __init__(self, x, y, respawn):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5

    def draw(self):
        screen.blit(veg.pic, (self.x, self.y))

class meat(object):
    pic = pygame.image.load('Meat_Obj.png')
    def __init__(self, x, y, respawn):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 10

    def draw(self):
        screen.blit(meat.pic, (self.x, self.y))

class goldencandy(object):
    pic = pygame.image.load('GoldenCandy_Obj.png')
    def __init__(self, x, y, respawn):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 100
    
    def draw(self):
        screen.blit(goldencandy.pic, (self.x, self.y))
        
food_tup = (bread, drinks, eggs, meat, veg, milk, goldencandy)

current_food = random.choice(food_tup)
current_food_instance = current_food(random.randint(1, WINDOW_WIDTH), current_food.pic.get_height(), False)

#Function which is drawing the images in the game and updates the display in every frame
def redrawGameWindow():
    global level, score

    screen.blit(background, (0, 0)) #Draws the background
    leveltextTBD = leveltext.render(f'Level: {level}', 1, (0, 0, 0))
    scoretextTBD = scoretext.render(f'Score: {score}', 1, (0, 0, 0))

    screen.blit(leveltextTBD, (2, 0)) #Drawing both texts of Level and Score
    screen.blit(scoretextTBD, (2, 68))

    if current_food_instance.respawn == False:
        current_food_instance.draw()

    if current_food_instance.y == maincart.y:
        current_food_instance.y = maincart.y
        current_food_instance.respawn = True

    else:
        current_food_instance.y += 4
        
    if left:
        screen.blit(walkleft_pic, (maincart.x, maincart.y))

    elif right:
        screen.blit(walkright_pic, (maincart.x, maincart.y))
    
    else:
        screen.blit(walkright_pic, (maincart.x, maincart.y))

    pygame.display.update() #Updates background and displays the background I downloaded.

run_program = True
clock = pygame.time.Clock()
maincart = cart(50, WINDOW_HEIGHT - walkleft_pic.get_height() - 130, 60, 60)

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