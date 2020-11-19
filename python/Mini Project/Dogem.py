import pygame
import random

#defining colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0,)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#black screen
size = (1000,720)

screen = pygame.display.set_mode(size)

#title of the window
pygame.display.set_caption("MINI Project")

#exit game falg set to false
done = False

#screen refresh rate
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):  #blueprint for an object with methods and attribute #and object is an instance of a class
    def __init__(self,colour,width,height):
        super().__init__()
        
        #set player dimentions
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        
        #set position of player
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
    #end procedure

    def player_speed(self,x,y):
        self.rect.x += x
        self.rect.y += y
        #end if
        
    def player_limits(self):
        if player.rect.x > 960:
            player.rect.x = 960
        elif player.rect.x < 40:
            player.rect.x = 40
        elif player.rect.y > 690:
            player.rect.y = 690
        elif player.rect.y < 40:
            player.rect.y = 40
        #end if
    #end procedure        
#end class
        
class Wall(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,x,y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #end procedure
#end class

map = [
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

all_sprite_group = pygame.sprite.Group()

my_player = Player(YELLOW,40,40)
all_sprite_group.add(my_player)
            
wall_group = pygame.sprite.Group()

x = 0
y = 0

for row in map:
    for column in row:
        if column == 1:
            my_wall = Wall(WHITE,40,40,x,y)
            all_sprite_group.add(my_wall)
            wall_group.add(my_wall)
        x = x + 40
        #end if
    #next column
    x = 0
    y = y + 40
#next row
    
pygame.init()
#game loop
while not done:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:#if left key is pressed
        my_player.player_speed(-10,0)
        
    elif key[pygame.K_RIGHT]:
        my_player.player_speed(10,0)
        
    elif key[pygame.K_UP]:
        my_player.player_speed(0,-10)
        
    elif key[pygame.K_DOWN]:
        my_player.player_speed(0,10)  

    #update all sprites    
    all_sprite_group.update()
    #screen background is black
    screen.fill(BLACK)
    #draw function
    all_sprite_group.draw(screen)
    #flip display to show new position of objects
    
    
    pygame.display.flip()
    clock.tick(60)
    
#end game loop
pygame.quit()
