#importing pygame
import pygame

#defining colours
Black = (0,0,0)
White = (255,255,255)
Blue = (50,50,255)
Yellow = (255,255,0)

#initialise pygame
pygame.init()

#black screen
size = (640 , 480)
screen = pygame.display.set_mode(size)
#title of the window
pygame.display.set_caption("my window")
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
    #screen background is black
    screen.fill(Black)
    #drawing shapes
    pygame.draw.rect(screen,Blue,(220,165,200,150))
    pygame.draw.circle(screen,Yellow,(40,100),40,0)
    #flip display to show new position of objects
    pygame.display.flip()
    clock.tick(60)
#end game loop
    pygame.quit()