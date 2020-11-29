import pygame
import random

#defining colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0,)
BLUE = (0,0,225)
YELLOW = (255,255,0)

block_size = 40
#black screen
size = (20 * block_size,16 * block_size)

screen = pygame.display.set_mode(size)

#title of the window
pygame.display.set_caption("MINI Project")

#exit game falg set to false
done = False

#screen refresh rate
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):  #blueprint for an object with methods and attribute #and object is an instance of a class
    def __init__(self,colour,width,height,speed):
        super().__init__()
        
        #set player dimentions
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        
        #set position of player
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()//2 - self.image.get_width()
        self.rect.y = screen.get_height()//2 - self.image.get_height()
        
        self.old_x =  self.rect.x
        self.old_y = self.rect.y
        
    def update(self):
        
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        
        if self.rect.x > screen.get_width() - self.image.get_width():  
            self.rect.x =  self.old_x
        elif self.rect.x < 0:  
            self.rect.x =  self.old_x
        #end if
        if self.rect.y > screen.get_height() - self.image.get_height():
            self.rect.y =  self.old_y
        elif self.rect.y < 0:
            self.rect.y =  self.old_y
        #end if
        
        self.speed_x = 0
        self.speed_y = 0

        self.old_y = self.rect.y 
        self.old_x = self.rect.x 
            
    def player_set_speed(self,x,y):
        self.speed_x = x
        self.speed_y = y

class Car(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,x,y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #end procedure
#end class


all_sprite_group = pygame.sprite.Group()

my_player = Player(YELLOW,40,40,5)
all_sprite_group.add(my_player)
            
wall_group = pygame.sprite.Group()
car_group = pygame.sprite.Group()

car_spawn_list = []

'''my_car = Car(RED,40,40,x,y)
all_sprite_group.add(my_car)
car_group.add(my_car)'''
        
    

            
        
          
#next row


pygame.init()
#game loop
while not done:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:#if left key is pressed
                my_player.player_set_speed(-40,0)
            elif event.key == pygame.K_RIGHT:
                my_player.player_set_speed(40,0)
            elif event.key == pygame.K_UP:
                my_player.player_set_speed(0,-40)
            elif event.key == pygame.K_DOWN:
                my_player.player_set_speed(0,40)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                my_player.player_set_speed(0,0)
            
            
    
    #
            
    
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
