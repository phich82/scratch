import pygame
import random

pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dino properties
dino_x = 50
dino_y = 450
dino_y_velocity = 0
dino_is_jumping = False
GRAVITY = 1

# Obstacle properties
obstacle_x = 800
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game states
game_running = True
game_over = False

def draw_dino(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, 40, 50))

def draw_obstacle(x):
    pygame.draw.rect(screen, BLACK, (x, 450, obstacle_width, obstacle_height))

def display_score():
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

def display_game_over():
    game_over_text = font.render("Game Over! Press Space to Restart", True, BLACK)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, text_rect)

clock = pygame.time.Clock()

while game_running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not dino_is_jumping:
                    dino_y_velocity = -20
                    dino_is_jumping = True
            if event.key == pygame.K_SPACE and game_over:
                # Reset game
                game_over = False
                obstacle_x = 800
                score = 0
                dino_y = 450
                dino_y_velocity = 0
                dino_is_jumping = False

    if not game_over:
        # Dino jump logic
        dino_y += dino_y_velocity
        dino_y_velocity += GRAVITY
        if dino_y >= 450:
            dino_y = 450
            dino_is_jumping = False

        # Obstacle movement
        obstacle_x -= obstacle_speed
        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH + random.randint(200, 500)
            score += 1

        # Collision detection
        if dino_x < obstacle_x + obstacle_width and \
           dino_x + 40 > obstacle_x and \
           dino_y < 450 + obstacle_height and \
           dino_y + 50 > 450:
            game_over = True

        draw_dino(dino_x, dino_y)
        draw_obstacle(obstacle_x)
        display_score()

    else:
        display_game_over()

    pygame.display.update()
    clock.tick(60)

pygame.quit()