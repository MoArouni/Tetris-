# each tetremino is made of 4 blocks -> which is why we will have a class Block
# then we will use this block class to make a tetremino class
# and we will use both of these classes to make a tetris class
# finally we will use all 3 of these classes to make a class App

# Import necessary modules and settings from external files
from settings import *
import math
import sys
from tetromino import Tetromino
import pygame.freetype as ft

# Define a class for displaying text on the game screen
class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)
        self.menu_toggled = False
        self.difficulty_toggled = False
        self.paused = False


        self.menu_position = (WIN_W * 0.65, WIN_H * 0.12)  # Position of "MENU"
        self.menu_size = (TILE_SIZE * 4, TILE_SIZE)  # Size of "MENU" button

        self.difficulty_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] // 3)
        self.difficulty_size = (TILE_SIZE * 10, TILE_SIZE)  # Size of difficulty button

        self.restart_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] // 2)
        self.restart_size = (TILE_SIZE * 10, TILE_SIZE)  # Size of restart button

        self.go_back_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] * 2 // 3)
        self.go_back_size = (TILE_SIZE * 10, TILE_SIZE)  # Size of go back button

        self.leave_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] * 5 // 6)
        self.leave_size = (TILE_SIZE * 10, TILE_SIZE)  # Size of leave button

        # Difficulty options positions
        self.easy_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] // 6)       # Between "Choose Difficulty" and "Restart Game"
        self.medium_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] * 5 // 12) 
        self.hard_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] * 7 // 12)      # Between "Restart Game" and "Go Back to Menu"
        self.insane_position = (FIELD_RES[0] // 2 - 80, FIELD_RES[1] * 13 // 18) 
        self.impossible_position =(FIELD_RES[0] // 2 - 80, FIELD_RES[1] * 11 // 12)    # Between "Go Back to Menu" and "Leave"

    def is_button_clicked(self, mouse_pos, button_position, button_size):
        """
        Checks if the mouse click is within the bounds of the button.

        :param mouse_pos: The position of the mouse (x, y).
        :param button_position: The position of the top-left corner of the button (x, y).
        :param button_size: The width and height of the button (width, height).
        :return: True if the button is clicked, False otherwise.
        """
        # Extract the button's position and size
        x, y = button_position
        width, height = button_size

        # Calculate the button's bounds as a rectangle
        bounds = pg.Rect(x, y, width, height)

        # Check if the mouse position is within the button's bounds
        clicked = bounds.collidepoint(mouse_pos)
        print(f"Clicked: {clicked}")
        
        return clicked

    def handle_button_clicks(self, mouse_pos):
        """
        Check which button is clicked and perform the corresponding action.
        """
        if self.is_button_clicked(mouse_pos, self.difficulty_position, self.difficulty_size):
            self.difficulty_toggled = True


        elif self.is_button_clicked(mouse_pos, self.leave_position, self.leave_size):
            # Leave: Quit the game
            pg.quit()
            sys.exit()

        elif self.is_button_clicked(mouse_pos, self.go_back_position, self.go_back_size):
            # Go Back to Menu: Hide menu options, show old sidebar text, and pause the game
            self.menu_toggled = False  # Close the menu
            self.difficulty_toggled = False

        elif self.is_button_clicked(mouse_pos, self.restart_position, self.restart_size):
            # Restart: Initialize a new Tetris game
            self.menu_toggled = False
            self.difficulty_toggled = False
            self.app.tetris = Tetris(self.app)  # Reset the game
            

    def draw(self):
        #not menu section
        x_position = WIN_W * 0.65
        title_position = (x_position, WIN_H * 0.02)
        menu_position = (x_position, WIN_H * 0.12)
        next_position = (x_position, WIN_H * 0.22)
        score_label_position = (x_position, WIN_H * 0.67)
        score_position = (x_position, WIN_H * 0.8)
        pause = (WIN_W * 0.3, WIN_H * 0.5)
        
        #menu section
        # Central x-position for all buttons
        # Central x-position for all buttons
        center_x = FIELD_RES[0] // 2 - TILE_SIZE * 5

        # Button sizes
        self.easy_size = self.hard_size = (TILE_SIZE * 4, TILE_SIZE)
        self.medium_size = self.insane_size = (TILE_SIZE * 8, TILE_SIZE)
        self.impossible_size = (TILE_SIZE * 10, TILE_SIZE)

        
        if self.difficulty_toggled:
            self.font.render_to(self.app.screen, self.easy_position,
                                text="Easy", fgcolor="white", size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, self.medium_position,
                                text="Medium", fgcolor="white", size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, self.hard_position,
                                text="Hard", fgcolor="white", size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, self.insane_position,
                                text="Insane", fgcolor="white", size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, self.impossible_position,
                                text="Impossible", fgcolor="white", size=int(TILE_SIZE * 1.2))
        # Calculate x position to center all text
        elif self.menu_toggled:
            # Draw menu options
            self.font.render_to(self.app.screen, self.difficulty_position,
                                text='Choose Difficulty', fgcolor="white",
                                size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, self.restart_position,
                                text='Restart Game', fgcolor="white",
                                size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, self.go_back_position,
                                text='Go Back to Game', fgcolor="white",
                                size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, self.leave_position,
                                text='Leave', fgcolor="white",
                                size=int(TILE_SIZE * 1.2))
            
            # Only show difficulty options if in difficulty selection state
            
            
        else :  
            # Render the text with dynamic color for "MENU"
            self.font.render_to(self.app.screen, title_position,
                                text='TETRIS', fgcolor="white",
                                size=int(TILE_SIZE * 1.5))
            self.font.render_to(self.app.screen, menu_position,
                                text='MENU', fgcolor="white",
                                size=int(TILE_SIZE * 1.2))
            
            self.font.render_to(self.app.screen, next_position,
                                text='NEXT : ', fgcolor='white',
                                size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, score_label_position,
                                text='SCORE : ', fgcolor='white',
                                size=int(TILE_SIZE * 1.2))
            self.font.render_to(self.app.screen, score_position,
                                text=f'{self.app.tetris.score}', fgcolor='white',
                                size=int(TILE_SIZE * 1.65))
            if self.paused : 
                self.font.render_to(self.app.screen, pause,
                                text='PAUSED', fgcolor='white',
                                size=int(TILE_SIZE * 1.65))
                



# Define the main Tetris game class
class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)
        self.speed_up = False

        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    # Function to update the score based on the number of full lines
    def get_score(self):
        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0

    # Function to check and remove full lines from the field
    def check_full_lines(self):
        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

                self.full_lines += 1

    # Function to place the blocks of the current tetromino in the field array
    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    # Function to initialize the field array with zeros
    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    # Function to check if the game is over
    def is_game_over(self):
        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True

    # Function to check if the current tetromino has landed and take appropriate actions
    def check_tetromino_landing(self):
        if self.tetromino.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.speed_up = False
                self.put_tetromino_blocks_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)

    # Function to handle player controls
    def control(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate()
        elif pressed_key == pg.K_DOWN:
            self.speed_up = True

    # Function to draw the grid on the game screen
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'blue',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    # Function to update the game state
    def update(self):
        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
            self.get_score()
        self.sprite_group.update()

    # Function to draw the game elements on the screen
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)
