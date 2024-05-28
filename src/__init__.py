import pygame
from pygame.font import Font

# Constants
WIDTH = 640
HEIGHT = 480
CELL_SIZE = 20
STATUS_BAR_HEIGHT = 2 * CELL_SIZE
GAME_HEIGHT = HEIGHT - STATUS_BAR_HEIGHT
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = GAME_HEIGHT // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Key Bindings
KEY_BINDINGS = {
    "Move Up": pygame.K_UP,
    "Move Down": pygame.K_DOWN,
    "Move Left": pygame.K_LEFT,
    "Move Right": pygame.K_RIGHT,
    "Pause": pygame.K_p,
    "Quit": pygame.K_q
}

# Menu Options
MENU_OPTIONS = ["Start Game", "View Key Bindings", "Exit"]

# Fonts
TITLE_FONT_SIZE = 48
TEXT_FONT_SIZE = 36

# Initialize Pygame
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake Game")

TITLE_FONTS = Font(None, 48)
TEXT_FONTS = Font(None, 36)