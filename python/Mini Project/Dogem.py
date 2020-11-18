import pygame
import random

#defining colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0,)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#black screen
size = (1000,1000)
screen = pygame.display.set_mode(size)
#title of the window
pygame.display.set_caption("MINI Project")
#exit game falg set to false
done = False
#screen refress rate
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):  #blueprint for an object with methods and attribute #and object is an instance of a class
    def __init__(self,colour,width,height):
        super().__init__()
        
        #set player dimentions
        self.speed = 0
        self.speed.x = 0
        self.speed.y = 0
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        
        #set position of player
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
    #end procedure
        
    def player_set_speed_x(self,speed):
        self.speed.x = speed
    
    def player_set_speed_y(self,speed):
        self.speed.y = speed
    #end procedure
        
    def update(self):
        self.rect.x = self.rect.x + self.speed.x
        self.rect.y = self.rect.y + self.speed.y
        #endless scroll
        if self.rect.x > 1000:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 1000
    #end procedure        
#end class        
        
pygame.init()

all_sprite_group = pygame.sprite.Group()
my_player = Player(YELLOW,50,50)
all_sprite_group.add(my_player)


#game loop
while not done:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:#if left key is pressed
                my_player.player_set_speed_x(-50)
                
            elif event.key == pygame.K_RIGHT:
                my_player.player_set_speed_x(50)
                
            elif event.key == pygame.K_UP:
                my_player.player_set_speed_y(-50)
                
            elif event.key == pygame.K_DOWN:
                my_player.set_speed_y(50)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                my_player.player_set_speed(0)
            

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
