# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()  # Initialize all imported pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()  # Create a clock to control the frame rate

    asteroids=pygame.sprite.Group()  # Create a group for asteroids
    updatable=pygame.sprite.Group()  # Create a group for updatable objects
    drawable=pygame.sprite.Group()  # Create a group for drawable objects  

    AsteroidField.containers = (updatable,)  # Set the containers for AsteroidField class
    Player.containers = (updatable, drawable)  # Set the containers for Player class
    Asteroid.containers = (asteroids, updatable, drawable)  # Set the containers for Asteroid class

    clock = pygame.time.Clock()  # Create a clock to control the frame rate
    dt=0  # Initialize delta time
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)  # Create a player instance
    asteroid_field = AsteroidField()  # Create an asteroid field instance

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
       
        pygame.Surface.fill(screen,color="black")  # Fill the screen with black

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS
        dt=clock.tick(60) / 1000.0  # Calculate delta time in seconds
    
if __name__ == "__main__":
    main()
