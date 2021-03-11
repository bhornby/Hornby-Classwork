import pygame
import random

#defining colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0,)
BLUE = (135,206,235)
YELLOW = (255,255,0)
GREEN= (124,252,0)

screen = pygame.display.set_mode(size)

#title of the window
pygame.display.set_caption("HITMAN")

#exit game falg set to false
done = False

#screen refresh rate
clock = pygame.time.Clock()

pygame.init()
#game loop
while not done:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
#end game loop
pygame.quit()

