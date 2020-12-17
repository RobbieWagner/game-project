""" Sprite Sample Program """

import random
import arcade
import time

# --- Constants ---
SPRITE_SCALING_ENEMY = .5
SPRITE_SCALING_PLAYER = 1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_COLUMN = 0
HEALTH_COLUMN = 1
ENEMY_COUNT = random.randrange(3) + 1

class Enemy(arcade.Sprite):
    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)
        self.max_health = max_health
        self.cur_health = max_health

class Player(arcade.Sprite):
    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)
        self.max_health = max_health
        self.cur_health = max_health

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
        self.isSetup = False
        
        # Stuff box specific
        self.box_clicked = False

        self.yeah = False

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()
        self.collider_list = arcade.SpriteList()

        # All Sprite images made in Piskel
        # Enemies
        for i in range(ENEMY_COUNT):
            if i == 0:
                self.enemy_sprite = Enemy("SlugEnemy.png", 1, max_health=10)
                self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 200
                self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 
                self.enemy_list.append(self.enemy_sprite)
            elif i == 1:
                self.enemy_sprite = Enemy("SlugEnemy.png", .8, max_health=10)
                self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 225
                self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 + 100
                self.enemy_list.append(self.enemy_sprite)
            elif i == 2:
                self.enemy_sprite = Enemy("SlugEnemy.png", .8, max_health=10)
                self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 225
                self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 - 100
                self.enemy_list.append(self.enemy_sprite)
            else:
                print(len(self.enemy_list))
        print(len(self.enemy_list))

        # Player
        self.player_sprite = Player("Protagonist.png", 1, max_health=25)
        self.player_sprite.center_x = SCREEN_WIDTH / 2 - 200
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player_sprite)

        # Box to be clicked
        self.box_sprite = arcade.Sprite("Box.png", 1)
        self.box_sprite.center_x = SCREEN_WIDTH / 2 - 150
        self.box_sprite.center_y = SCREEN_HEIGHT / 2 + 50
        self.box_list.append(self.box_sprite)

        # Mouse cursor
        self.cursor_sprite = arcade.Sprite("Cursor.png", 1)
        self.cursor_sprite.center_x = SCREEN_WIDTH / 2
        self.cursor_sprite.center_y = SCREEN_HEIGHT / 2
        self.cursor_list.append(self.cursor_sprite)

        # Box for collision checks
        self.collider_sprite = Collider("Collider.png", 1)
        self.collider_sprite.center_x = SCREEN_WIDTH + 50
        self.collider_sprite.center_y = SCREEN_HEIGHT + 50
        self.collider_list.append(self.collider_sprite)

        self.isSetup = True

    def on_draw(self):
        arcade.start_render()
        
        # Draw the Sprites
        self.enemy_list.draw()
        self.player_list.draw()
        self.box_list.draw()
        self.cursor_list.draw()


        hi = 0
        # Draws the healthbars
        for enemy in self.enemy_list:
            no_health_point = self.enemy_sprite.center_x - 30
            length = 60 * self.enemy_sprite.cur_health / self.enemy_sprite.max_health
        
            if length > 0:
                arcade.draw_lrtb_rectangle_outline(no_health_point - 2, self.enemy_sprite.center_x + 32, self.enemy_sprite.center_y + 50, self.enemy_sprite.center_y + 42, arcade.color.GRAY, 2)
                arcade.draw_lrtb_rectangle_filled(no_health_point, no_health_point + length, self.enemy_sprite.center_y + 48, self.enemy_sprite.center_y + 44, arcade.color.RED)
            
            if not self.yeah:
                hi += 1
                print(hi)
        self.yeah = True
        
        arcade.draw_lrtb_rectangle_outline(0, SCREEN_WIDTH, SCREEN_HEIGHT / 8, 0, arcade.color.WHITE_SMOKE, 10)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # Moves cursor
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Sets box_clicked to True if the box is clicked
        if self.box_sprite.center_x + 20 > self.cursor_sprite.center_x > self.box_sprite.center_x - 20 and \
            self.box_sprite.center_y + 20 > self.cursor_sprite.center_y > self.box_sprite.center_y - 20:
            self.box_clicked = True

    def on_update(self, delta_time: float):
        # Moves the Collider over to the slug when the box gets clicked
        if self.box_clicked:
            indexes = []
            for enemy in self.enemy_list:
                indexes.append(self.enemy_list.index(enemy))
            target = random.randrange(len(indexes))
            for enemy in self.enemy_list:
                if target == self.enemy_list.index(enemy):
                    self.collider_sprite.center_x = self.enemy_sprite.center_x
                    self.collider_sprite.center_y = self.enemy_sprite.center_y

            # Adds enemies with a collider over them into the enemies_hit list
            enemies_hit = arcade.check_for_collision_with_list(self.collider_sprite, self.enemy_list)
            print(len(enemies_hit))
            # Damages enemies with Collider over them. Kills them if their health drops to 0
            for enemy in enemies_hit:
                self.enemy_sprite.cur_health -= 5
                print("hi")
                if self.enemy_sprite.cur_health <= 0:
                    time.sleep(.5)
                    enemy.remove_from_sprite_lists()
            
            self.box_clicked = False
            

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
