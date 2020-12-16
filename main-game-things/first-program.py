""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_ENEMY = .5
SPRITE_SCALING_PLAYER = 1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_COLUMN = 0
HEALTH_COLUMN = 1


class Player(arcade.Sprite):
    def __init__(self):
        self.health = 20
        self.hit = False

    def update(self):
        if self.hit:
            self.health -= 5
            self.hit = False


class Enemy(arcade.Sprite):
    def __init__(self):
        self.health = 20
        self.hit = False

    def update(self):
        if self.hit:
            self.health -= 5
            self.hit = False


class Collider(arcade.Sprite):
    def update(self):
        if self.center_x < SCREEN_WIDTH + 50 and not self.box_clicked:
            self.center_x = SCREEN_WIDTH + 50

        if self.center_y < SCREEN_HEIGHT + 50 and not self.box_clicked:
            self.center_y = SCREEN_HEIGHT + 50


class MyGame(arcade.Window):

    def __init__(self):
        # Initialize window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Slug Fight")

        # Sprites in game
        self.enemy_list = None
        self.player_list = None
        self.box_list = None
        self.cursor_list = None
        self.collider_list = None

        # Sprites info
        self.enemy_sprite = None
        self.player_sprite = None
        self.box_sprite = None
        self.cursor_sprite = None
        self.collider_sprite = None

        # Hide mouse
        self.set_mouse_visible(False)

        # Countdown variable
        self.countdown = 30
        self.isSetup = False
        
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
        self.collider_list = arcade.SpriteList()

        # Image made in Piskel
        self.enemy_sprite = Enemy("SlugEnemy.png", SPRITE_SCALING_ENEMY)
        self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 200
        self.enemy_sprite.center_y = SCREEN_HEIGHT / 2
        self.enemy_list.append(self.enemy_sprite)

        # Image made in Piskel
        self.player_sprite = Player("Protagonist.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = SCREEN_WIDTH / 2 - 200
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # Image made in Piskel
        self.box_sprite = arcade.Sprite("Box.png", 1)
        self.box_sprite.center_x = SCREEN_WIDTH / 2 - 150
        self.box_sprite.center_y = SCREEN_HEIGHT / 2 + 50
        self.box_list.append(self.box_sprite)

        # Image made in Piskel
        self.cursor_sprite = arcade.Sprite("Cursor.png", 1)
        self.cursor_sprite.center_x = SCREEN_WIDTH / 2
        self.cursor_sprite.center_y = SCREEN_HEIGHT / 2
        self.cursor_list.append(self.cursor_sprite)

        # Image made in Piskel
        self.collider_sprite = arcade.Sprite("Collider.png", 1)
        self.collider_sprite.center_x = SCREEN_WIDTH + 50
        self.collider_sprite.center_y = SCREEN_HEIGHT + 50
        self.collider_list.append(self.collider_sprite)

        self.isSetup = True

    def on_draw(self):
        arcade.start_render()
        
        self.enemy_list.draw()
        self.player_list.draw()
        self.box_list.draw()
        self.cursor_list.draw()

        arcade.draw_lrtb_rectangle_outline(0, SCREEN_WIDTH, SCREEN_HEIGHT / 8, 0, arcade.color.WHITE_SMOKE, 10)

        arcade.finish_render()
    
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.cursor_sprite.center_x + 20 > x > self.cursor_sprite.center_x - 20 and \
            self.cursor_sprite.center_y + 20 > y > self.cursor_sprite.center_y - 20:
            self.box_clicked = True

    def on_update(self, delta_time: float):
        if self.box_clicked:
            self.collider_sprite.center_x = self.enemy_sprite.center_x
            self.collider_sprite.center_y = self.enemy_sprite.center_y
            
            enemies_hit = arcade.check_for_collision_with_list(self.collider_sprite, self.enemy_list)
            for enemy in enemies_hit:
                self.hit = True
            self.box_clicked = False
            

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
