import pygame
from src import settings

class Paddle:
    def __init__(self):
        self.width = settings.PADDLE_WIDTH
        self.height = settings.PADDLE_HEIGHT
        self.x = (settings.SCREEN_WIDTH - self.width) // 2
        self.y = 350
        self.speed = settings.PADDLE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == 'left' and self.rect.left > 0:
            self.rect.x -= self.speed
        if direction == 'right' and self.rect.right < settings.SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, settings.BLUE, self.rect, border_radius = 4)

    
