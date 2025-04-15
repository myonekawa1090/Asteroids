import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid (CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, screen): 
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self): 
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS: 
            return
        else: 
            rand_angle = random.uniform(20, 50)
            velocity_a = self.velocity.rotate(rand_angle)
            velocity_b = self.velocity.rotate(-rand_angle)
            old_radius = self.radius
            self.radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_a.velocity = velocity_a * ASTEROID_SPLIT_SPEED_RATE
            asteroid_b = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_b.velocity = velocity_b * ASTEROID_SPLIT_SPEED_RATE