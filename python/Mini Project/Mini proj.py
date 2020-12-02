import pygame
import random
from os import path

#defining colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0,)
BLUE = (135,206,235)
YELLOW = (255,255,0)
GREEN= (124,252,0)

block_size = 40
#black screen
size = (20 * block_size,16 * block_size)

HS_FILE = "highscore.txt"

car_lane_list = [[2,6,8],
                 [4,9,3],
                 [3,5,9,10,13],
                 [6,8,9,11,14],
                 [4,7,2,9,],
                 [1,3,5,6,7,14,],
                 [1,5,6,8,9,10,14],
                 [1,2,3,7,10,11,13],
                 [2,4,5,6,7,8,10,13,14],
                 [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
                 ]

screen = pygame.display.set_mode(size)

#title of the window
pygame.display.set_caption("CRUSTY ROAD")


#time
#exit game falg set to false
done = False

#screen refresh rate
clock = pygame.time.Clock()

def reset_game():    
    global all_sprite_group
    all_sprite_group = pygame.sprite.Group()
    
    global car_group
    car_group = pygame.sprite.Group()
     
    global portal_group 
    portal_group = pygame.sprite.Group()
    
    global my_player
    my_player = Player(YELLOW,block_size,block_size,5)
    
    
    global level
    level = 0
    
    
    global p
    global o
    p=0
    o=0
    
    all_sprite_group.add(my_player)
    load_data()
#end procedure
    
def load_data():
    #load highscore
    global highscore
    dir = path.dirname(__file__)
    with open(path.join(dir, HS_FILE),'w') as f: #w opens file for reading and writing
        try:
            highscore = int(f.read())
        except:
            highscore = 0


class Player(pygame.sprite.Sprite):  #blueprint for an object with methods and attribute #and object is an instance of a class
    def __init__(self,colour,width,height,speed):
        super().__init__()
        
        #set player dimentions
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.score = 0
        self.old_score = 0
        self.lives = 1
        self.time = 0
        self.old_time = 0
        self.start_time = 0
        
        
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
        
        self.old_score = self.score 
        self.old_time = self.time
        if self.start_time == 0:
            self.start_time = pygame.time.get_ticks()//1000
        self.time = pygame.time.get_ticks()//1000 - self.start_time
        
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
class Portal(pygame.sprite.Sprite):
    def __init__(self,colour,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 9*block_size
        self.rect.y = 0*block_size
    #end procedure
        
class Grass(pygame.sprite.Sprite):
    def __init__(self,colour,width,height,x,y):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
          
def car_spawn(level):
    o = 4
    p = 6
    x = screen.get_width()
    r = random.randint(0,9)
    l = car_lane_list[level]
    y = l[random.randint(0,len(l)-1)]
    y = y*block_size
    #next b,c
    speed = random.randint(o,p)
    if r%7 == 0:
        my_car = Car(RED,block_size,block_size,x,y,speed)
        all_sprite_group.add(my_car)
        car_group.add(my_car)
    #end if
#end procedure

def portal_spawn():
    my_portal = Portal(WHITE,block_size,block_size)
    all_sprite_group.add(my_portal)
    portal_group.add(my_portal)
#end procedure

def show_score(x,y):
    font = pygame.font.SysFont('Arial', 20, True, False)
    text = font.render("Score: " + str(my_player.score),True,WHITE)
    screen.blit(text, (x,y))
#end functions
def show_time(x,y):
    font = pygame.font.SysFont('Arial', 20, True, False)
    text = font.render("Time: " + str(my_player.time),True,WHITE)
    screen.blit(text, (x,y))
def show_level(x,y):
    font = pygame.font.SysFont('Arial', 20, True, False)
    text = font.render("Level: " + str(level + 1),True,WHITE)
    screen.blit(text, (x,y))

def show_hs(x,y):
    font = pygame.font.SysFont('Arial', 20, True, False)
    text = font.render("HighScore: " + str(highscore),True,WHITE)
    screen.blit(text, (x,y))
    
    
reset_game()
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
                my_player.score = my_player.score + 1
            elif event.key == pygame.K_DOWN:
                my_player.player_set_speed(0,40)
                my_player.score = my_player.score - 1
            elif event.key == pygame.K_RETURN and my_player.lives < 1:
                reset_game()
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                my_player.player_set_speed(0,0)
            
    player_hit_group = pygame.sprite.spritecollide(my_player, car_group, True)
    for x in player_hit_group:
        my_player.lives = my_player.lives - 1
    #next x
    
    player_hit_list = pygame.sprite.spritecollide(my_player, portal_group, True)
    if player_hit_list:
        my_player.rect.x = screen.get_width()//2 - my_player.image.get_width()
        my_player.rect.y = screen.get_height()- my_player.image.get_height()
        p = p + 3
        o = o + 3
        level = level + 1
        if level >= len(car_lane_list):
            level = 0
        
        #end if
    #next x
        
    
    
    if my_player.lives < 1:
        screen.fill(WHITE)
        font= pygame.font.SysFont('Arial', 50, True, False)
        font2= pygame.font.SysFont('Arial', 30, True, False)
        
        if my_player.old_score > highscore:
            highscore = my_player.old_score
            with open(path.join(dir, HS_FILE),'w') as f:
                f.write(str(my_player.old_score))
        #end if
        #array of tuples
        text = [(font.render("GAME OVER",True,BLACK),4),
                (font2.render("Level Reached " + str(level +1),True,BLACK),2.1),
                (font2.render("Score: " + str(my_player.old_score),True,BLACK),1.9),\
                (font2.render("Highscore: " + str(highscore),True,BLACK),2.4),
                (font2.render("Time: " + str(my_player.old_time),True,BLACK),1.6),
                (font.render("HIT RETURN TO PLAY AGAIN",True,BLACK),3)
                ]
        for t,h in text:    
            screen.blit(t, (screen.get_width()//2 - t.get_width()//2,screen.get_height()//h - t.get_height()//2))
        #next t,h
    else:
        #update all sprites    
        all_sprite_group.update()
        #screen background is black
        screen.fill(BLUE)
        #draw function
        all_sprite_group.draw(screen)
          
       
    portal_spawn()
    car_spawn(level)
    show_score(20,45)
    show_time(20,70)
    show_level(20,20)
    show_hs(20,0)
    pygame.display.flip()
    clock.tick(60)
    
#end game loop
pygame.quit()
