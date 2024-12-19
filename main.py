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

        #MoArouni Change : Modify the window creation to allow resizing 
        self.screen = pg.display.set_mode(WIN_RES, pg.RESIZABLE)

        # Create Pygame clock for controlling frame rate
        self.clock = pg.time.Clock()

        # Set up animation triggers and timers
        self.set_timer()

        # Load images for the game
        self.images = self.load_images()

        # Initialize Tetris game and text display
        self.tetris = Tetris(self)
        self.text = Text(self)

        self.paused = False

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
        if not self.paused and not self.text.menu_toggled: 
            self.tetris.update()
        self.clock.tick(FPS)
        


    # Function to draw the game elements on the screen
    def draw(self):
        # Fill the screen with background color
        self.screen.fill(color=BG_COLOR)

        #scale the game field dynamically based on FIELD_RES and TILE_SIZE
        field_rect = pg.Rect(0, 0, FIELD_RES[0], FIELD_RES[1])
        self.screen.fill(color=FIELD_COLOR, rect=field_rect)

        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))

        # Draw Tetris game and text elements
        self.tetris.draw()
        self.text.draw()

        # Update the display
        pg.display.flip()
    

    def update_animation_interval(self, interval):
        ANIM_TIME_INTERVAL = interval  # Update the main interval
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)  # Update the timer
        print(f"Animation time interval updated to {interval} ms")


    # Function to handle Pygame events
    def check_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and self.text.menu_toggled == False:
                    self.text.paused = not self.text.paused
                    self.paused = not self.paused
                    print("Game Paused :")
                else:
                    self.tetris.control(pressed_key=event.key)
            
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pg.mouse.get_pos()
                    if self.text.is_button_clicked(mouse_pos, self.text.menu_position, self.text.menu_size):  # Only log if the menu is clicked
                        self.text.menu_toggled = not self.text.menu_toggled
                    if self.text.menu_toggled : 
                        self.text.handle_button_clicks(mouse_pos)
                        if self.text.is_button_clicked(mouse_pos, self.text.easy_position, self.text.easy_size):
                            print("Difficulty set to Easy")
                            self.update_animation_interval(150)
                            self.text.difficulty_toggled = False
                            self.text.menu_toggled = True
                        elif self.text.is_button_clicked(mouse_pos, self.text.medium_position, self.text.medium_size):
                            print("Difficulty set to Medium")
                            self.update_animation_interval(140)
                            self.text.difficulty_toggled = False
                            self.text.menu_toggled = True
                        elif self.text.is_button_clicked(mouse_pos, self.text.hard_position, self.text.hard_size):
                            print("Difficulty set to Hard")
                            self.update_animation_interval(130)
                            self.text.difficulty_toggled = False
                            self.text.menu_toggled = True
                        elif self.text.is_button_clicked(mouse_pos, self.text.insane_position, self.text.insane_size):
                            print("Difficulty set to Insane")
                            self.update_animation_interval(115)
                            self.text.difficulty_toggled = False
                            self.text.menu_toggled = True
                        elif self.text.is_button_clicked(mouse_pos, self.text.impossible_position, self.text.impossible_size):
                            print("Difficulty set to Impossible")
                            self.update_animation_interval(100)
                            self.text.difficulty_toggled = False
                            self.text.menu_toggled = True






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


# Modified the main application to include a dynamic and resizable game window.
# Added menu toggle functionality with options for difficulty selection, restart, and exit.
# Integrated a pause and resume feature to control game flow.
# Enhanced the event handling system to handle button interactions and difficulty changes.
# Streamlined the game loop to reflect updates in the sidebar and menu states.
