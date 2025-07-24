# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers =  updatable
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y= SCREEN_HEIGHT / 2
    player = Player(x,y)
    asteroid_field = AsteroidField()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                   asteroid.split() 


      
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
         





if __name__ == "__main__":
    main()
