from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )
    
    def update(self, dt): 
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_angle1 = self.velocity.rotate(random_angle)
        new_angle2 = self.velocity.rotate(-random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_angle1 * 1.2
        asteroid2.velocity = new_angle2 * 1.2
        return [asteroid1, asteroid2]


        

    
