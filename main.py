# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()  # Create a clock to control the frame rate
    dt=0  # Initialize delta time
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)  # Create a player instance

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)  # Update the player with delta time
        pygame.Surface.fill(screen,color="black")  # Fill the screen with black
        player.draw(screen)  # Draw the player
        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS
        dt=pygame.time.Clock().tick(60) / 1000.0  # Calculate delta time in seconds
    
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
