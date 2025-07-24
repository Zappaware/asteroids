from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__()

    def draw(self):
        pygame.draw.circle(screen, "white", x, y, radius, 2)
    
    def update(self, dt):
        self.move(dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * self.velocity * dt


        

    
