# Import necessary modules and settings from external files
from settings import *
from tetris import Tetris, Text
import sys
import pathlib

# Define the main application class
class App:
    def __init__(self):
        # Initialize Pygame
        pg.init()

        # Set window caption and create the game window
        pg.display.set_caption('Tetris')
        self.screen = pg.display.set_mode(WIN_RES)

        # Create Pygame clock for controlling frame rate
        self.clock = pg.time.Clock()

        # Set up animation triggers and timers
        self.set_timer()

        # Load images for the game
        self.images = self.load_images()

        # Initialize Tetris game and text display
        self.tetris = Tetris(self)
        self.text = Text(self)

    # Function to load images from the sprite directory and scale them to TILE_SIZE
    def load_images(self):
        files = [item for item in pathlib.Path(SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images

    # Function to set up animation triggers and timers
    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    # Function to update the game state
    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    # Function to draw the game elements on the screen
    def draw(self):
        # Fill the screen with background color
        self.screen.fill(color=BG_COLOR)

        # Fill the game field with the field color
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))

        # Draw Tetris game and text elements
        self.tetris.draw()
        self.text.draw()

        # Update the display
        pg.display.flip()

    # Function to handle Pygame events
    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False

        for event in pg.event.get():
            # Quit the game if the user closes the window or presses ESC
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            # Handle key presses for Tetris controls
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)

            # Set animation triggers based on timer events
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    # Function to run the game loop
    def run(self):
        while True:
            # Handle Pygame events
            self.check_events()

            # Update the game state
            self.update()

            # Draw the game elements on the screen
            self.draw()


# Entry point of the program
if __name__ == '__main__':
    # Create an instance of the App class and run the game
    app = App()
    app.run()
