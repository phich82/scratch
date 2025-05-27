import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
SQUARE_SIZE = 100
WIDTH = BOARD_WIDTH * SQUARE_SIZE
HEIGHT = (BOARD_HEIGHT + 1) * SQUARE_SIZE
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

# Function to create the board
def create_board():
    board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board

# Function to draw the board
def draw_board(board):
    for c in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int((r + 1) * SQUARE_SIZE + SQUARE_SIZE / 2)), 45)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int((r + 1) * SQUARE_SIZE + SQUARE_SIZE / 2)), 45)
    pygame.display.update()

# Function to drop a piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check if a location is valid
def is_valid_location(board, col):
    return board[0][col] == 0

# Function to get the next open row
def get_next_open_row(board, col):
    for r in range(BOARD_HEIGHT - 1, -1, -1):
        if board[r][col] == 0:
            return r

# Function to check for a win
def check_win(board, piece):
    # Check horizontal
    for c in range(BOARD_WIDTH - 3):
        for r in range(BOARD_HEIGHT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Check vertical
    for c in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Check positively sloped diagonals
    for c in range(BOARD_WIDTH - 3):
        for r in range(BOARD_HEIGHT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Check negatively sloped diagonals
    for c in range(BOARD_WIDTH - 3):
        for r in range(3, BOARD_HEIGHT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

# Game loop
board = create_board()
draw_board(board)
game_over = False
turn = 0

font = pygame.font.SysFont('monospace', 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Ask for Player 1 Input
            if turn % 2 == 0:
                posx = event.pos[0]
                col = int(posx // SQUARE_SIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if check_win(board, 1):
                        label = font.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40,10))
                        game_over = True
                    
                    turn += 1
                    draw_board(board)

            # Ask for Player 2 Input
            else:
                posx = event.pos[0]
                col = int(posx // SQUARE_SIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if check_win(board, 2):
                        label = font.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40,10))
                        game_over = True

                    turn += 1
                    draw_board(board)
    
    if game_over:
        pygame.time.wait(3000)