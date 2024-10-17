import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, bullet):
        bullet.kill()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20.0, 50.0)
            vecA = self.velocity.rotate(angle)
            vecB = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astA = Asteroid(self.position.x, self.position.y, new_radius)
            astB = Asteroid(self.position.x, self.position.y, new_radius)
            astA.velocity = vecA * 1.2
            astB.velocity = vecB * 1.2
