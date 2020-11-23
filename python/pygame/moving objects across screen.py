import pygame
import math
#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

#initialising pygame
pygame.init()

#set blank screen
width = 640
height = 480
size = (width,height)
screen = pygame.display.set_mode(size)

#title of window
pygame.display.set_caption("bens house of the rising sun")

#varaibles
sun_x = -40
sun_y = 100

#screen refresh
clock = pygame.time.Clock()

#game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
    #nextevent
     
    #game logic    
    sun_x = sun_x + 2
    if sun_x > (width + 40) :
        sun_x = 0
    #endif
    #converting x into radians so that approximately 180 degrees fits onto the allocated screen size.
    #then scaling y so it doesnt only move between the range 0 to 1 and only on 1 pixel
    sun_y = 260 + int(math.sin(float(sun_x)/200)*-230)
    
    
    #screen background BLACK
    screen.fill(BLACK)
    
    #draw the shapes sun and block
    pygame.draw.rect(screen,BLUE, (220,200,200,150))
    pygame.draw.circle(screen,YELLOW, (sun_x,sun_y),40,0)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
    