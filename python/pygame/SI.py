import pygame
pygame.init()

#defining colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

#set display
size  = (700,500)
screen_width = 700
screen_heigt = 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("test")

clock = pygame.time.Clock()
#loop until user clicks close button
done = False
#start possition
ellipse_x = 80
ellipse_y = 50

ellipse_x1 = 150
ellipse_y1 = 50

ellipse_x2= 250
ellipse_y2=50
#speed and direction change
ellipse_change_x = 1


    
 
# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
     
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the rectangle
    
 
    pygame.draw.ellipse(screen, GREEN, [ellipse_x, ellipse_y, 40, 30])
 
    # Move the rectangle starting point
    ellipse_x += ellipse_change_x
    
    if ellipse_x > 100 or ellipse_x < 50:
        ellipse_change_x = ellipse_change_x * -1
        
        
     #2nd alien   
    pygame.draw.ellipse(screen, GREEN, [ellipse_x1, ellipse_y1, 40, 30])
 
    # Move the rectangle starting point
    ellipse_x1 += ellipse_change_x
    
    if ellipse_x1 > 150 or ellipse_x1 < 100 :
        ellipse_change_x = ellipse_change_x * -1
        
        
    #3rd alien   
    pygame.draw.ellipse(screen, GREEN, [ellipse_x2, ellipse_y2, 40, 30])
 
    # Move the rectangle starting point
    ellipse_x2 += ellipse_change_x
    
    if ellipse_x2 > 200 or ellipse_x2 < 150:
        ellipse_change_x = ellipse_change_x * -1
        
        
    
    
    
    
        


 
    
        
    
        
    
    



    

    
        
        
        
    
    
        
    
        
    

    #refreshes the screen
    pygame.display.flip()
    
    #limits to 60 fps
    clock.tick(60)

pygame.quit()











