from constants import *
from circleshape import CircleShape
import pygame
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y,PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        return PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation += self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotation -= self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
