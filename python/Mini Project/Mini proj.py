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
        self.rect.y = screen.get_height()- self.image.get_height()
        
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
    def __init__(self,colour,width,height,x,y,speed):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    #end procedure
    def update(self):
        self.rect.x = self.rect.x - self.speed
        if self.rect.x < 0:
            car_group.remove(self)
            all_sprite_group.remove(self)
        #end if   
    #end procedure
#end class


all_sprite_group = pygame.sprite.Group()

my_player = Player(YELLOW,40,40,5)

all_sprite_group.add(my_player)
            
car_group = pygame.sprite.Group()

car_lane_list = [1*block_size,2*block_size,3*block_size,5*block_size,6*block_size,7*block_size,10*block_size,12*block_size,13*block_size,14*block_size,]

def car_spawn():
    x = screen.get_width()
    r = random.randint(0,9)
    y = car_lane_list[random.randint(0,len(car_lane_list)-1)]
    speed = random.randint(3,6)
    if r%7 == 0:
        my_car = Car(RED,block_size,block_size,x,y,speed)
        all_sprite_group.add(my_car)
        car_group.add(my_car)
    #end if
#end procedure
        
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
            
           
    
    
            
    car_spawn()
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
