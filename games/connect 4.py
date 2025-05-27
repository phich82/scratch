import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Define the shapes of the tetrominoes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],  # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
]

# Define the colors of the tetrominoes
SHAPE_COLORS = [
    CYAN,
    MAGENTA,
    ORANGE,
    BLUE,
    YELLOW,
    GREEN,
    RED,
]

# Define the size of the grid and the blocks
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 30

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen_width = GRID_WIDTH * BLOCK_SIZE
screen_height = GRID_HEIGHT * BLOCK_SIZE
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Tetris")

# Define the Tetromino class
class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.rotation = 0
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        rotated_shape = list(zip(*self.shape[::-1]))
        if self.is_valid_move(rotated_shape, self.x, self.y):
            self.shape = rotated_shape
            self.rotation = (self.rotation + 1) % 4

    def move(self, dx, dy):
        if self.is_valid_move(self.shape, self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy
    
    def is_valid_move(self, shape, x, y):
        for row_index, row in enumerate(shape):
            for col_index, cell in enumerate(row):
                if cell:
                    grid_x = x + col_index
                    grid_y = y + row_index
                    if grid_x < 0 or grid_x >= GRID_WIDTH or grid_y >= GRID_HEIGHT or (grid_y >= 0 and grid[grid_y][grid_x] is not None):
                        return False
        return True

    def draw(self):
        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            (self.x + col_index) * BLOCK_SIZE,
                            (self.y + row_index) * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE,
                        ),
                    )

# Define the game grid
grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Define the current tetromino
current_tetromino = Tetromino(random.choice(SHAPES))

# Define the game loop
game_over = False
clock = pygame.time.Clock()
fall_speed = 1
fall_timer = 0

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_tetromino.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                current_tetromino.move(1, 0)
            elif event.key == pygame.K_DOWN:
                current_tetromino.move(0, 1)
            elif event.key == pygame.K_UP:
                current_tetromino.rotate()

    # Update the game state
    fall_timer += clock.get_rawtime()
    clock.tick()

    if fall_timer / 1000 >= fall_speed:
        fall_timer = 0
        if current_tetromino.is_valid_move(current_tetromino.shape, current_tetromino.x, current_tetromino.y + 1):
            current_tetromino.move(0, 1)
        else:
            for row_index, row in enumerate(current_tetromino.shape):
                for col_index, cell in enumerate(row):
                    if cell:
                        grid[current_tetromino.y + row_index][current_tetromino.x + col_index] = current_tetromino.color

            # Check for completed lines
            for row_index in range(GRID_HEIGHT):
                if all(grid[row_index]):
                    del grid[row_index]
                    grid.insert(0, [None for _ in range(GRID_WIDTH)])

            current_tetromino = Tetromino(random.choice(SHAPES))
            if not current_tetromino.is_valid_move(current_tetromino.shape, current_tetromino.x, current_tetromino.y):
                game_over = True

    # Draw the screen
    screen.fill(BLACK)

    # Draw the grid
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                )
            else:
                pygame.draw.rect(
                    screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1
                )

    # Draw the current tetromino
    current_tetromino.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()