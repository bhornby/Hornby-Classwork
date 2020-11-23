import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30,30])
        self.image.fill(YELLOW)
        # Set position
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.lives = 3

    def player_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val

all_sprites_list = pygame.sprite.Group()
player = Player()
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.player_speed(-1,0)
        """
        if keys[pygame.K_DOWN]:
            player.player_speed(-1,1)
        elif keys[pygame.K_UP]:
            player.player_speed(-1,-1)
        """
    elif keys[pygame.K_RIGHT]:
        player.player_speed(1,0)
        """
        if keys[pygame.K_DOWN]:
            player.player_speed(1,1)
        elif keys[pygame.K_UP]:
            player.player_speed(1,-1)
        """
    elif keys[pygame.K_UP]:
        player.player_speed(0,-1)
    elif keys[pygame.K_DOWN]:
        player.player_speed(0,1)

    # --- Game logic should go here
    all_sprites_list.update()
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
