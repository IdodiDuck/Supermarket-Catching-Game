import pygame, game_screen

class cart(object):
    '''
    Main Cart, the object that the user controls. The cart should catch the falling food items before they reach the floor
    Cart inherits from the class object
    '''

    def __init__(self, x, y, width, height, vel): #Attributes of the cart
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

class bread(object):
    '''
    The bread food object class, one of the options of the random food falling objects. Bread worths 5 points in the score
    '''
    pic = pygame.image.load('Bread_Obj.png')

    def __init__(self, x, y, respawn, vel):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5
        self.vel = vel
    
    def draw(self):
        '''
        A function which draws the instance of the bread food object to the screen every frame in coordinates (self.x, self.y)
        '''
        (game_screen.screen).blit(bread.pic, (self.x, self.y))
        
class drinks(object):
    '''
    The drinks food object class, one of the options of the random food falling objects. Drinks worths 10 points in the score
    '''
    pic = pygame.image.load('Drinks_Obj.png')

    def __init__(self, x, y, respawn, vel):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 10
        self.vel = vel

    def draw(self):
        '''
        A function which draws the instance of the drinks food object to the screen every frame in coordinates (self.x, self.y)
        '''
        game_screen.screen.blit(drinks.pic, (self.x, self.y))

class eggs(object):
    '''
    The eggs cartoon food object class, one of the options of the random food falling objects. Eggs worths 5 points in the score
    '''

    pic = pygame.image.load('Eggs_Obj.png')
    def __init__(self, x, y, respawn, vel):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5
        self.vel = vel

    def draw(self):
        '''
        A function which draws the instance of the eggs food object to the screen every frame in coordinates (self.x, self.y)
        '''
        
        game_screen.screen.blit(eggs.pic, (self.x, self.y))

class milk(object):
    '''
    The milk food object class, one of the options of the random food falling objects. Milk worths 5 points in the score
    '''
    pic = pygame.image.load('Milk_Obj.png')
    def __init__(self, x, y, respawn, vel):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5
        self.vel = vel

    def draw(self):
        '''
        A function which draws the instance of the milk food object to the screen every frame in coordinates (self.x, self.y)
        '''
        game_screen.screen.blit(milk.pic, (self.x, self.y))

class veg(object):
    '''
    The vegetables food object class, one of the options of the random food falling objects. Vegetables worths 5 points in the score
    '''
    pic = pygame.image.load('Vegetables_Obj.png')
    def __init__(self, x, y, respawn, vel):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 5
        self.vel = vel

    def draw(self):
        '''
        A function which draws the instance of the vegetables food object to the screen every frame in coordinates (self.x, self.y)
        '''
        game_screen.screen.blit(veg.pic, (self.x, self.y))

class meat(object):
    '''
    The meat food object class, one of the options of the random food falling objects. Meat worths 10 points in the score
    '''
    pic = pygame.image.load('Meat_Obj.png')
    def __init__(self, x, y, respawn, vel):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 10
        self.vel = vel

    def draw(self):
        '''
        A function which draws the instance of the meat food object to the screen every frame in coordinates (self.x, self.y)
        '''
        game_screen.screen.blit(meat.pic, (self.x, self.y))

class goldencandy(object):
    '''
    The Golden Candy food object class, one of the options of the random food falling objects but the most valueable one. Golden Candy worths 100 points in the score
    '''
    pic = pygame.image.load('GoldenCandy_Obj.png')
    def __init__(self, x, y, respawn, vel):
        self.x = x
        self.y = y
        self.respawn = respawn
        self.pts = 100
        self.vel = vel 
        
    def draw(self):
        '''
        A function which draws the instance of the golden candy food object to the screen every frame in coordinates (self.x, self.y)
        '''
        game_screen.screen.blit(goldencandy.pic, (self.x, self.y))