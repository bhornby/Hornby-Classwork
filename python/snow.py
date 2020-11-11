#importing pygame
import pygame
import math
import random

#defining colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#initialise pygame
pygame.init()

#black screen
size = (640 , 480)
screen = pygame.display.set_mode(size)
#title of the window
pygame.display.set_caption("Snow")
#exit game falg set to false
done = False
#screen refress rate
clock = pygame.time.Clock()

#game loop
while not done:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #game logic goes here
            
    #creating a list of snow
    snow_group = pygame.sprite.Group()
    #creating a list of all sprites 
    all_sprite_group = pygame.sprite.Group()
    
    class Snow(pygame.sprite.Sprite):
        #define the constructor
        def __init__ (self, colour ,width, height, speed):
            super().__init__()
            
            #create a sprite and dill it with colour
            self.image = pygame.Surface([width,height])
            self.image.fill(colour)
            self.speed = speed
            
            #set position of the sprite
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(0,600)
            self.rect.y = random.randrange(0,400)
            
        #end procedure
    #end class
            
        #class update function    
        def update(self):
            self.rect.y = self.rect.x + self.speed
        #end procedure
            
    #creating the snowflakes
    number_of_flakes = 50
    for x in range(number_of_flakes):
        my_snow = Snow(WHITE, 5 ,5, 1)
        snow_group.add(my_snow)
        all_sprite_group.add(my_snow)
    #next x
    
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