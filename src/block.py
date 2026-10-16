import pygame
from src import settings

class Block:
    def __init__(self, x, y, row):
        self.rect = pygame.Rect(x, y, settings.BLOCK_WIDTH, settings.BLOCK_HEIGHT)
        colors = [settings.RED, settings.YELLOW, settings.GREEN, settings.BLUE]
        self.color = colors[row % len(colors)]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius = 2)