#importing pygame
import pygame
import random

#defining colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

#black screen
size = (640,480)
screen = pygame.display.set_mode(size)
#title of the window
pygame.display.set_caption("invader")
#exit game falg set to false
done = False
#screen refress rate
clock = pygame.time.Clock()

class Invader(pygame.sprite.Sprite):
    #define the constructor
    def __init__(self, colour ,width, height, speed):
        super().__init__()
        
        #create a sprite and dill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.speed = speed
        
        #set position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,620)
        self.rect.y = random.randrange(-50,240)
        
    #end procedure    
    #class update function    
    def update(self):
        self.rect.y = self.rect.y + self.speed
        #endless snow
        if self.rect.y > 480:
            self.rect.y = 0
            self.rect.x = random.randrange(0,620)
        #end if 
    #end procedure
            
class Player(pygame.sprite.Sprite):  #blueprint for an object with methods and attribute #and object is an instance of a class
    def __init__(self,colour,width,height):
        super().__init__()
        
        #set player dimentions
        self.lives = 3
        self.speed = 0
        self.bullet_count = 50
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        
        #set position of player
        self.rect = self.image.get_rect()
        self.rect.x = 290
        self.rect.y = 455
        
    def update(self):
        self.rect.x = self.rect.x + self.speed
        #endless scroll
        if self.rect.x > 640:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 640
            
    def player_set_speed(self,speed):
        self.speed = speed
        
        #end if 
    #end procedure

class Bullet(pygame.sprite.Sprite):
    def __init__(self,colour,speed,x,y):
        super().__init__()
        #define varibles
        self.speed = -10
        self.image = pygame.Surface([10,10])
        self.image.fill(colour)
        #draw bullet
        self.rect = self.image.get_rect()
        self.rect.x = x +15
        self.rect.y = y + 10
    
    def update(self):
        self.rect.y = self.rect.y + self.speed
        
    

#end class            
    
def show_score(x,y):
    font= pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Lives: " + str(my_player.lives),True,WHITE)
    screen.blit(text, (x,y))
#end functions    
 
#initialise pygame
pygame.init()

#create a list of all invaders   
invaders_group = pygame.sprite.Group()
#creating a list of all sprites
all_sprite_group = pygame.sprite.Group()
#a list of all bullets
bullet_group = pygame.sprite.Group()

#creating the player
my_player = Player(YELLOW,30,20)
all_sprite_group.add(my_player)

#creating the snowflakes
number_of_invaders = 20
if number_of_invaders < 1:
    number_of_invaders = 15
else:
    for x in range(number_of_invaders):
        my_invader = Invader(WHITE, 15 ,15, (3 +random.randrange(0,6)))
        invaders_group.add(my_invader)
        all_sprite_group.add(my_invader)
#next x
    
#game loop
while not done:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:#if left key is pressed
                my_player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                my_player.player_set_speed(3)
            elif event.key == pygame.K_SPACE:
                my_bullet = Bullet(RED, 10, my_player.rect.x,my_player.rect.y)
                #creating the bullets 
                bullet_group.add(my_bullet)
                all_sprite_group.add(my_bullet)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                my_player.player_set_speed(0)
            
            
    
    #game logic goes here
    
    #when an invader hits the player
    player_hit_group = pygame.sprite.spritecollide(my_player, invaders_group, True)
    
    #deduction of lives
    for foo in player_hit_group:
        my_player.lives = my_player.lives - 1
        
    for x in bullet_group:
        bullet_hit_group = pygame.sprite.spritecollide(x, invaders_group, True)
        for foo in bullet_hit_group:
            my_player.bullet_count = my_player.bullet_count - 1
            number_of_invaders = number_of_invaders - 1


    #score limiter
    if my_player.lives < 1:
        screen.fill(WHITE)
        font= pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("Game Over",True,BLACK)
        screen.blit(text, (screen.get_width()//2 - text.get_width()//2,screen.get_height()//2 - text.get_height()//2))
    else:
        #update all sprites    
        all_sprite_group.update()
        #screen background is black
        screen.fill(BLACK)
        #draw function
        all_sprite_group.draw(screen)
         
    #display score
    show_score(10,10)
    
    #flip display to show new position of objects
    pygame.display.flip()
    clock.tick(60)
    
#end game loop
pygame.quit()

#frame counter and divide by 60 for clock base time score