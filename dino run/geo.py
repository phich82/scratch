import pygame

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash (Simplified)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
player_size = 30
player_x = 50
player_y = HEIGHT - player_size - 50
player_speed = 5
player_jump_strength = 15
is_jumping = False
player_y_velocity = 0

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_x = WIDTH
obstacle_speed = 5
obstacles = []

# Game variables
clock = pygame.time.Clock()
running = True
score = 0
font = pygame.font.Font(None, 36)

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_size, player_size))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def generate_obstacle():
    obstacles.append([WIDTH, HEIGHT - obstacle_height - 50])

def display_score():
    text_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text_surface, (10, 10))

# Game loop
frame_count = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                player_y_velocity = -player_jump_strength

    # Player movement
    if is_jumping:
        player_y += player_y_velocity
        player_y_velocity += 1  # Gravity
        if player_y >= HEIGHT - player_size - 50:
            player_y = HEIGHT - player_size - 50
            is_jumping = False
            player_y_velocity = 0

    # Obstacle generation and movement
    if frame_count % 100 == 0:
        generate_obstacle()
    frame_count += 1

    for obstacle in obstacles:
        obstacle[0] -= obstacle_speed
        if obstacle[0] < -obstacle_width:
            obstacles.remove(obstacle)
            score += 1

        # Collision detection
        if player_x < obstacle[0] + obstacle_width and player_x + player_size > obstacle[0] and player_y < obstacle[1] + obstacle_height and player_y + player_size > obstacle[1]:
            running = False  # Game over

    # Drawing
    screen.fill(BLACK)
    draw_player(player_x, player_y)
    for obstacle in obstacles:
        draw_obstacle(obstacle[0], obstacle[1])
    display_score()

    pygame.display.update()
    clock.tick(60)

pygame.quit()