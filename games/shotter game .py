import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Shooting Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player properties
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 20
player_speed = 5

# Bullet properties
bullet_size = 10
bullet_speed = 10
bullets = []

# Enemy properties
enemy_size = 30
enemy_speed = 2
enemies = []

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game states
game_running = True
game_over = False


def create_enemy():
    enemy_x = random.randint(0, screen_width - enemy_size)
    enemy_y = 0
    enemies.append([enemy_x, enemy_y])


def draw_player(x, y):
    pygame.draw.rect(screen, white, (x, y, player_size, player_size))


def draw_bullet(x, y):
    pygame.draw.circle(screen, red, (x, y), bullet_size)


def draw_enemy(x, y):
    pygame.draw.rect(screen, white, (x, y, enemy_size, enemy_size))


def display_score():
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))


def display_game_over():
    game_over_text = font.render("Game Over! Score: " + str(score), True, white)
    text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(game_over_text, text_rect)


# Game loop
clock = pygame.time.Clock()
enemy_spawn_timer = 0

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_size // 2, player_y])
            if event.key == pygame.K_r and game_over:
                # Restart the game
                game_over = False
                score = 0
                enemies = []
                bullets = []
                player_x = screen_width // 2 - player_size // 2

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Enemy spawn logic
    enemy_spawn_timer += clock.get_rawtime()
    if enemy_spawn_timer > 1000:  # Spawn every 1 second
        create_enemy()
        enemy_spawn_timer = 0

    # Bullet movement and collision detection
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
            continue
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
            bullet_rect = pygame.Rect(bullet[0] - bullet_size, bullet[1] - bullet_size, 2 * bullet_size, 2 * bullet_size)
            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

    # Enemy movement and collision detection with player
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            game_over = True
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        if enemy_rect.colliderect(player_rect):
            game_over = True

    # Draw everything
    screen.fill(black)
    draw_player(player_x, player_y)
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])
    display_score()
    if game_over:
        display_game_over()

    pygame.display.update()
    clock.tick(60)

pygame.quit()