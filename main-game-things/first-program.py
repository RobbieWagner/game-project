""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_ENEMY = .5
SPRITE_SCALING_PLAYER = 1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self):
        # Initialize window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Slug")

        # Sprites in game
        self.enemy_list = None
        self.player_list = None
        self.box_list = None
        self.cursor_list = None

        # Sprites info
        self.enemy_sprite = None
        self.player_sprite = None
        self.box_sprite = None
        self.cursor_sprite = None

        # Hide mouse
        self.set_mouse_visible(False)

        # Countdown variable
        self.countdown = 30
        self.setup = False
        
        # Stuff box specific
        self.box_clicked = False

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()

        # Image made in Piskel
        self.enemy_sprite = arcade.Sprite("SlugEnemy.png", SPRITE_SCALING_ENEMY)
        self.enemy_sprite.center_x = 150
        self.enemy_sprite.center_y = 50
        self.enemy_list.append(self.enemy_sprite)

        self.player_sprite = arcade.Sprite("Protagonist.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        self.box_sprite = arcade.Sprite("Box.png", 1)
        self.box_sprite.center_x = 200
        self.box_sprite.center_y = 75
        self.box_list.append(self.box_sprite)

        self.cursor_sprite = arcade.Sprite("Cursor.png", 1)
        self.cursor_sprite.center_x = SCREEN_WIDTH / 2
        self.cursor_sprite.center_y = SCREEN_HEIGHT / 2
        self.cursor_list.append(self.cursor_sprite)

        self.setup = True

    def on_update(self, delta_time: float):
        if self.setup:
            
            if self.countdown:
                self.countdown -= 1

    def on_draw(self):
        arcade.start_render()
        
        self.enemy_list.draw()
        self.player_list.draw()
        self.box_list.draw()
        self.cursor_list.draw()

        arcade.finish_render()
    
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()