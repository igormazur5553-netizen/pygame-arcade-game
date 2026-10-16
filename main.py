import pygame, sys
from src import settings
from src.paddle import Paddle
from src.ball import Ball
from src.block import Block
from src.game_stats import GameStats
from src.database import Database

def create_blocks():
    blocks = []
    for row in range(settings.BLOCK_ROWS):
        for col in range(settings.BLOCK_COLS):
            x = col * (settings.BLOCK_WIDTH + settings.BLOCK_MARGIN) + 40
            y = row * (settings.BLOCK_HEIGHT + settings.BLOCK_MARGIN) + settings.BLOCK_TOP_OFFSET
            blocks.append(Block(x, y, row))
    return blocks

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption('Arcade Arkanoid')
    clock = pygame.time.Clock()

    db = Database()
    paddle = Paddle()
    ball = Ball()
    blocks = create_blocks()
    stats = GameStats()

    running = True
    while running:
        clock.tick(settings.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and stats.game_over:
                    paddle = Paddle()
                    ball = Ball()
                    blocks = create_blocks()
                    stats = GameStats()

        if not stats.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move('left')
            if keys[pygame.K_RIGHT]:
                paddle.move('right')

            ball.move()

            if ball.rect.colliderect(paddle.rect):
                ball.speed_y *= -1
                ball.rect.bottom = paddle.rect.top

            for block in blocks[:]:
                if ball.rect.colliderect(block.rect):
                    ball.speed_y *= -1
                    blocks.remove(block)
                    stats.score += 10
                    break

            if ball.rect.bottom >= settings.SCREEN_HEIGHT:
                stats.lives -= 1
                if stats.lives <= 0:
                    stats.game_over = True
                    db.save_score('Igor', stats.score)
                else:
                    ball.reset()

            if not blocks:
                stats.game_over = True
                db.save_score('Igor', stats.score)

        screen.fill(settings.BLACK)
        paddle.draw(screen)
        ball.draw(screen)
        for block in blocks:
            block.draw(screen)
        stats.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
