import pygame, random, game_objects, game_screen

#Initialize the PyGame library and text
pygame.init()

pygame.font.init()
leveltext = pygame.font.SysFont("bahnschrift", 60)
scoretext = pygame.font.SysFont("bahnschrift", 40)
livestext = pygame.font.SysFont("bahnschrift", 45)

#Setting up the game
pygame.display.set_caption('Supermarket Game')
background = pygame.image.load('Game_SuperMarket_Banner.png')

music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

# Game Constants - 
# Cart Constants
CART_START_LOCATION = game_screen.WINDOW_WIDTH // 2
CART_HEIGHT = 205
CART_WIDTH = 50
CART_VELOCITY = 20

# Colors Constants
BLACK = (0, 0, 0)
RED = (139, 0, 0)

#Animations pictures for the main-cart object
walkright_pic = pygame.image.load('ShoppingCartRight.png')
walkleft_pic = pygame.image.load('ShoppingCartLeft.png')

user_score = 0
current_level = 1
user_lives = 3
level_requirement = 10

cart_height = 421

current_food_vel = 1

user_alive = True
clock = pygame.time.Clock()
maincart = game_objects.cart(CART_START_LOCATION, game_screen.WINDOW_HEIGHT - walkleft_pic.get_height() - 20, CART_WIDTH, CART_HEIGHT, CART_VELOCITY)

left, right = False, False

def check_if_user_lost():
     
    if user_lives == 0:
        print(f"GAME OVER!\nYour score is {user_score}")
        return False
    
    return True

def generate_food():
    '''
    A function which generates one of the food object classes and returns an instance of it to the main core function of the program.
    '''
    food_tup = (game_objects.bread, game_objects.drinks, game_objects.eggs, game_objects.meat, game_objects.veg, game_objects.milk, game_objects.goldencandy)

    current_food = random.choice(food_tup)

    current_food_instance = current_food(random.choice(range(10, game_screen.WINDOW_WIDTH - 50, 10)), 0, False, current_food_vel)
    return current_food_instance

def checkMovement():
    """
    The function checks if user pressed right/left keys and updates
    """

    global left, right

    KEYS = pygame.key.get_pressed()

    if KEYS[pygame.K_LEFT] and maincart.x > 0: #Left Movement
            maincart.x -= maincart.vel
            left = True
            right = False

    elif KEYS[pygame.K_RIGHT] and maincart.x < game_screen.WINDOW_WIDTH - maincart.width: #Right Movement
        maincart.x += maincart.vel
        left = False
        right = True

def moveCart():
    """
    The function performs representation of cart's image by movement direction
    """

    if left:
        game_screen.screen.blit(walkleft_pic, (maincart.x, maincart.y))

    elif right:
        game_screen.screen.blit(walkright_pic, (maincart.x, maincart.y))
    
    else:
        game_screen.screen.blit(walkright_pic, (maincart.x, maincart.y))

def drawGameTexts():
    """
    The function represents to game screen the texts of level, score and lives
    """

    game_screen.screen.blit(background, (0, 0)) # Draws the background

    leveltextTBD = leveltext.render(f'Level: {current_level}', 1, BLACK)
    scoretextTBD = scoretext.render(f'Score: {user_score}', 1, BLACK)
    lives_textTBD = livestext.render(f'Lives: {user_lives}', 1, RED)
    
    game_screen.screen.blit(leveltextTBD, (2, 0)) #Drawing both texts of Level and Score
    game_screen.screen.blit(scoretextTBD, (2, 68))
    game_screen.screen.blit(lives_textTBD, (game_screen.WINDOW_WIDTH - 150, 0))

def redrawGameWindow(current_food_instance):
    '''
    A function which redraws the game window in each frame, draws the level, scores and lives texts. Additionaly it draws the maincart and the random falling food objects including speed control of the maincart and food-objects.
    '''
    global current_level, user_score, user_lives, level_requirement, current_food_vel
    
    drawGameTexts()

    if current_food_instance.respawn == False:
        current_food_instance.draw()
    
    if current_food_instance.y <= game_screen.WINDOW_HEIGHT:
        current_food_instance.y += 3 * current_food_instance.vel

    else:
        current_food_instance.respawn = True
        current_food_instance = generate_food()

    if current_food_instance.y >= maincart.y + 25 and current_food_instance.y < game_screen.WINDOW_HEIGHT - 100:  # Checks Y
        if current_food_instance.x in range(maincart.x - CART_WIDTH, maincart.x + CART_WIDTH):  # Checks X
            user_score += current_food_instance.pts

            if user_score >= level_requirement:
                current_level += 1
                level_requirement *= 1.5
                current_food_vel *= 1.1

            current_food_instance = generate_food()

    elif current_food_instance.y >= 510:
        user_lives -= 1
        current_food_instance.respawn = True
        current_food_instance = generate_food()

    moveCart()

    pygame.display.update() #Updates background and displays the background I downloaded.
    return current_food_instance

def main():
    '''
    The main function of the program, includes the program flow and running including FPS and drawing functions.
    '''

    global user_alive, clock, maincart, right, left

    current_food_instance = generate_food()
    #Main prorgam loop

    while user_alive:
        clock.tick(40) #40 Frames Per Second (FPS)
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f'WINDOW CLOSED BY THE USER\nYour score is {user_score}')
                return 1

        user_alive = check_if_user_lost()

        checkMovement()

        current_food_instance = redrawGameWindow(current_food_instance)

        pygame.display.update()

    return 0

if __name__ == '__main__':
    main()