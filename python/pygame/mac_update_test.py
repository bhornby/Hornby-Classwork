import pygame

BLUE = (50,50,255)

pygame.init()

width = 640
height = 480
size = (width,height)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

#game loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #endif
    #nextevent
            
    screen.fill(BLUE)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
    
