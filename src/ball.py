import pygame, random
from src import settings

class Ball:
    def __init__(self):
        self.radius = settings.BALL_RADIUS
        self.reset()

    def reset(self):
        self.x = settings.SCREEN_WIDTH // 2
        self.y = 350
        self.speed_x = random.choice([-4, 4])
        self.speed_y = -4
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= settings.SCREEN_WIDTH:
            self.speed_x *= -1

        if self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, settings.WHITE, self.rect.center, self.radius)