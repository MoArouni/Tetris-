# Import necessary modules and settings from external files
from settings import *
import random

# Import Pygame module
import pygame as pg

# Define the Block class representing individual blocks in the game
class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        # Initialize the Block with a reference to its tetromino, position, and status
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_POS_OFFSET
        self.alive = True

        # Call the superclass constructor and set the image and rect attributes
        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image
        self.rect = self.image.get_rect()

        # Initialize special effects variables
        self.sfx_image = self.image.copy()
        self.sfx_image.set_alpha(110)
        self.sfx_speed = random.uniform(0.2, 0.6)
        self.sfx_cycles = random.randrange(6, 8)
        self.cycle_counter = 0

    # Function to check if the special effects animation has ended
    def sfx_end_time(self):
        if self.tetromino.tetris.app.anim_trigger:
            self.cycle_counter += 1
            if self.cycle_counter > self.sfx_cycles:
                self.cycle_counter = 0
                return True

    # Function to run the special effects animation
    def sfx_run(self):
        self.image = self.sfx_image
        self.pos.y -= self.sfx_speed
        self.image = pg.transform.rotate(self.image, pg.time.get_ticks() * self.sfx_speed)

    # Function to check if the block is alive and handle special effects
    def is_alive(self):
        if not self.alive:
            if not self.sfx_end_time():
                self.sfx_run()
            else:
                self.kill()

    # Function to rotate the block around a specified pivot position
    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos

    # Function to set the rect position based on the block's current or next position
    def set_rect_pos(self):
        pos = [self.next_pos, self.pos][self.tetromino.current]
        self.rect.topleft = pos * TILE_SIZE

    # Function to update the block's status and position
    def update(self):
        self.is_alive()
        self.set_rect_pos()

    # Function to check if a collision occurs at a specified position
    def is_collide(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (
                y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True


# Define the Tetromino class representing a group of blocks forming a tetromino
class Tetromino:
    def __init__(self, tetris, current=True):
        # Initialize the Tetromino with a reference to its tetris game, shape, image, and blocks
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.image = random.choice(tetris.app.images)
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landing = False
        self.current = current

    # Function to rotate the tetromino
    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        # Check for collision before applying rotation
        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]

    # Function to check for collision between the tetromino and other blocks
    def is_collide(self, block_positions):
        return any(map(Block.is_collide, self.blocks, block_positions))

    # Function to move the tetromino in a specified direction
    def move(self, direction):
        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)

        # Move the tetromino if no collision occurs, otherwise mark it as landing
        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            self.landing = True

    # Function to update the tetromino's position (mainly used for downward movement)
    def update(self):
        self.move(direction='down')
