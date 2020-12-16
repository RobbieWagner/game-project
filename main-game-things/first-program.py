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

        # Sprites info
        self.enemy_sprite = None
        self.player_sprite = None

        # Hide mouse
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Image made in Piskel
        self.enemy_sprite = arcade.Sprite("SlugEnemy.png", SPRITE_SCALING_ENEMY)
        self.enemy_sprite.center_x = 150
        self.enemy_sprite.center_y = 150
        self.enemy_list.append(self.enemy_sprite)

        self.player_sprite = arcade.Sprite("Protagonist.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_update(self, delta_time: float):
        

    def on_draw(self):
        arcade.start_render()
        
        self.enemy_list.draw()
        self.player_list.draw()

        arcade.finish_render()
    
    def on_key_press(self, symbol: int, modifiers: int):



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()