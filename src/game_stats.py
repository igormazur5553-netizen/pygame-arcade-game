import pygame
from src import settings

class GameStats:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.font = pygame.font.SysFont('Arial', 24)

    def draw(self, screen):
        score_text = self.font.render(f'Score: {self.score}', True, settings.WHITE)
        lives_text = self.font.render(f'Lives: {self.lives}', True, settings.WHITE)
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (700, 20))

        if self.game_over:
            game_over_font = pygame.font.SysFont('Arial', 48)
            over_text = game_over_font.render('GAME OVER - Press R to Restart', True, settings.WHITE)
            screen.blit(over_text, (100, 300))