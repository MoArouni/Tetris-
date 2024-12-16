import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (24, 89, 117)

SPRITE_DIR_PATH = 'assets/sprites'
FONT_PATH = 'assets/font/FREAKSOFNATUREMASSIVE.ttf'

ANIM_TIME_INTERVAL = 150  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15

TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
# Import the Pygame library with an alias 'pg'
import pygame as pg

# Create a vector class from Pygame for 2D vector operations
vec = pg.math.Vector2

# Set constants for the game
FPS = 60
FIELD_COLOR = (50, 50, 50)
BG_COLOR = (20, 100, 130)

# Set file paths for sprites and font
SPRITE_DIR_PATH = 'assets/sprites'
FONT_PATH = 'assets/font/FREAKSOFNATUREMASSIVE.ttf'

# Set time intervals for animations
ANIM_TIME_INTERVAL = 150  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15

# Set the size of a single tile and the size of the game field in tiles
TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

# Set scaling factors for the field and calculate the window resolution
FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

# Set initial and next position offsets for tetrominoes
INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)

# Define movement directions for the tetrominoes
MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

# Define shapes of tetrominoes and their relative positions
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
