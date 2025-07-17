# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player



def main():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()  # Create a clock to control the frame rate
    updatable=pygame.sprite.Group()  # Create a group for updatable objects
    drawable=pygame.sprite.Group()  # Create a group for drawable objects   
    Player.containers = (updatable, drawable)  # Set the containers for Player class
    dt=0  # Initialize delta time
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)  # Create a player instance

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
       
        pygame.Surface.fill(screen,color="black")  # Fill the screen with black

        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS
        dt=pygame.time.Clock().tick(60) / 1000.0  # Calculate delta time in seconds
    
if __name__ == "__main__":
    main()
