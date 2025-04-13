import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, screen): 
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), SHOT_RADIUS)
        
    def update(self, dt):
        self.position += self.velocity * dt
        