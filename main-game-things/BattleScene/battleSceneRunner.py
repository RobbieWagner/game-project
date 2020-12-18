""" Sprite Sample Program """

import random
import arcade
import time
from BattleScene import battleSceneClasses

# --- Constants ---
SPRITE_SCALING_ENEMY = .5
SPRITE_SCALING_PLAYER = 1
SCREEN_WIDTH = 1375
SCREEN_HEIGHT = 750
SPRITE_COLUMN = 0
HEALTH_COLUMN = 1
ENEMY_COUNT = random.randrange(3) + 1


class Collider(arcade.Sprite):
    def update(self):
        
        if self.center_x < SCREEN_WIDTH + 50:
            self.center_x = SCREEN_WIDTH + 50

        if self.center_y < SCREEN_HEIGHT + 50:
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

        # Your turn indicator
        self.your_turn = False
        self.coin_flip = 0

        # Indicator for selected targets
        self.target_selected = False

        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)

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
            type = random.randrange(2)
            if type == 0:
                if i == 0:
                    self.enemy_sprite = battleSceneClasses.Enemy("slug", "SlugEnemy.png", .8, max_health=10)
                    self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 400
                    self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 16 
                    self.enemy_list.append(self.enemy_sprite)
                elif i == 1:
                    self.enemy_sprite = battleSceneClasses.Enemy("slug", "SlugEnemy.png", .6, max_health=5)
                    self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 425
                    self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 16 + 200
                    self.enemy_list.append(self.enemy_sprite)
                elif i == 2:
                    self.enemy_sprite = battleSceneClasses.Enemy("slug", "SlugEnemy.png", .6, max_health=5)
                    self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 425
                    self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 16 - 200
                    self.enemy_list.append(self.enemy_sprite)
            elif type == 1:
                if i == 0:
                    self.enemy_sprite = battleSceneClasses.Enemy("spider", "SpiderEnemy.png", 1, max_health=15)
                    self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 400
                    self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 16 
                    self.enemy_list.append(self.enemy_sprite)
                elif i == 1:
                    self.enemy_sprite = battleSceneClasses.Enemy("spider", "SpiderEnemy.png", .8, max_health=10)
                    self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 425
                    self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 16 + 200
                    self.enemy_list.append(self.enemy_sprite)
                elif i == 2:
                    self.enemy_sprite = battleSceneClasses.Enemy("spider", "SpiderEnemy.png", .8, max_health=10)
                    self.enemy_sprite.center_x = SCREEN_WIDTH / 2 + 425
                    self.enemy_sprite.center_y = SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 16 - 200
                    self.enemy_list.append(self.enemy_sprite)


        # Player
        self.player_sprite = battleSceneClasses.Player("Protagonist", "Protagonist.png", 1, max_health=25)
        self.player_sprite.center_x = SCREEN_WIDTH / 2 - 400
        self.player_sprite.center_y = SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 16
        self.player_list.append(self.player_sprite)

        # Boxes to be clicked
        self.box_sprite = battleSceneClasses.Box("Melee_Attack_Sword.png", .5, False, "attack", "Protagonist")
        self.box_list.append(self.box_sprite)
        self.box_sprite = battleSceneClasses.Box("Heal.png", .5, False, "heal", "Protagonist")
        self.box_list.append(self.box_sprite)
        self.box_sprite = battleSceneClasses.Box("Box.png", 1, False, "no", "Protagonist")
        self.box_list.append(self.box_sprite)

        # Arranges boxes
        for box in self.box_list:
            for player in self.player_list:
                if self.box_list.index(box) == 0 and player.name == box.associated_player:
                    box.center_x = player.center_x
                    box.center_y = player.center_y + 100
                else:
                    box.center_x = SCREEN_WIDTH + 50
                    box.center_y = SCREEN_HEIGHT + 50
                

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

        # Decides who goes first
        self.coin_flip = random.randrange(2)
        if self.coin_flip == 0:
            self.your_turn = True
        else:
            self.your_turn = False

        self.isSetup = True

    def on_draw(self):
        arcade.start_render()
        
        # Draw the Sprites
        self.enemy_list.draw()
        self.player_list.draw()
        self.box_list.draw()
        self.cursor_list.draw()

        # Draws the healthbars for enemies and players
        for enemy in self.enemy_list:
            no_health_point = enemy.center_x - 30
            length = 60 * enemy.cur_health / enemy.max_health
        
            if length > 0:
                arcade.draw_lrtb_rectangle_outline(no_health_point - 2, enemy.center_x + 32, enemy.center_y - 45, enemy.center_y - 53, arcade.color.GRAY, 2)
                arcade.draw_lrtb_rectangle_filled(no_health_point, no_health_point + length, enemy.center_y - 47, enemy.center_y - 51, arcade.color.RED)
                arcade.draw_text(enemy.type, no_health_point - 2, enemy.center_y - 68, arcade.color.WHITE, 10, 40, "left")

        for player in self.player_list:
            no_health_point = player.center_x - 30
            length = 60 * player.cur_health / player.max_health

            if length > 0:
                if length < 15:
                    color = arcade.color.RED
                elif length < 30:
                    color = arcade.color.YELLOW
                else:
                    color = arcade.color.GREEN
                arcade.draw_lrtb_rectangle_outline(no_health_point - 2, player.center_x + 32, player.center_y - 75, player.center_y - 83, arcade.color.GRAY, 2)
                arcade.draw_lrtb_rectangle_filled(no_health_point, no_health_point + length, player.center_y - 77, player.center_y - 81, color)
                arcade.draw_text(f"{player.cur_health}/{player.max_health}", no_health_point - 5, player.center_y - 100, arcade.color.WHITE, 10, 50, "left")

        # Draws highlights of enemy boxes if attacking
        for box in self.box_list:
            if box.box_type == "attack" and box.is_clicked and not self.target_selected:
                for enemy in self.enemy_list:
                    arcade.draw_lrtb_rectangle_outline(enemy.center_x - 40, enemy.center_x + 40, enemy.center_y + 25, enemy.center_y - 25, arcade.color.LIGHT_RED_OCHRE, 2)

        if len(self.player_list) == 0:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 3 / 4, arcade.color.RED, 15, 100, "center")
        if len(self.enemy_list) == 0:
            arcade.draw_text("YOU WIN", SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT * 3 / 4, arcade.color.WHITE, 15, 100, "center")
        
        arcade.draw_lrtb_rectangle_outline(0, SCREEN_WIDTH, SCREEN_HEIGHT / 8, 0, arcade.color.WHITE_SMOKE, 10)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # Moves cursor
        self.cursor_sprite.center_x = x
        self.cursor_sprite.center_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Sets box_clicked to True if the box is clicked
        for box in self.box_list:
            if box.center_x + 20 > self.cursor_sprite.center_x > box.center_x - 20 and \
                box.center_y + 20 > self.cursor_sprite.center_y > box.center_y - 20:
                box.is_clicked = True
            if box.is_clicked and box.box_type == "attack":
                for enemy in self.enemy_list:
                    if enemy.center_x - 40 < self.cursor_sprite.center_x < enemy.center_x + 40 and enemy.center_y - 25 < self.cursor_sprite.center_y < enemy.center_y + 25:
                        self.target_selected = True

    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.SPACE:
            for box in self.box_list:
                if not box.center_x == SCREEN_WIDTH + 50:
                    box.is_clicked = True
        
        if key == arcade.key.D:
            value = 0
            for box in self.box_list:
                if not box.center_x == SCREEN_WIDTH + 50 and not self.box_list.index(box) == len(self.box_list) - 1:
                    value = self.box_list.index(box) + 1
                elif not box.center_x == SCREEN_WIDTH + 50 and self.box_list.index(box) == len(self.box_list) - 1:
                    value = 0
            for box in self.box_list:
                for player in self.player_list:
                    if value == self.box_list.index(box) and player.name == box.associated_player:
                        box.center_x = player.center_x
                        box.center_y = player.center_y + 100
                    else:
                        box.center_x = SCREEN_WIDTH + 50
                        box.center_y = SCREEN_WIDTH + 50

        if key == arcade.key.A:
            value = 0
            for box in self.box_list:
                if not box.center_x == SCREEN_WIDTH + 50 and not self.box_list.index(box) == 0:
                    value = self.box_list.index(box) - 1
                elif not box.center_x == SCREEN_WIDTH + 50 and self.box_list.index(box) == 0:
                    value = len(self.box_list) - 1
            for box in self.box_list:
                for player in self.player_list:
                    if value == self.box_list.index(box) and player.name == box.associated_player:
                        box.center_x = player.center_x
                        box.center_y = player.center_y + 100
                    else:
                        box.center_x = SCREEN_WIDTH + 50
                        box.center_y = SCREEN_WIDTH + 50

    def on_update(self, delta_time: float):
        # Moves the Collider over to the slug when the box gets clicked
        if len(self.enemy_list) > 0 and len(self.player_list) > 0:
            if self.your_turn:

                #checks to see if any boxes were clicked
                for box in self.box_list:
                    if box.is_clicked and box.box_type == "attack":
                        if self.target_selected:
                            indexes = []
                            for enemy in self.enemy_list:
                                indexes.append(self.enemy_list.index(enemy))
                            for enemy in self.enemy_list:
                                if enemy.center_x - 40 < self.cursor_sprite.center_x < enemy.center_x + 40 and enemy.center_y - 25 < self.cursor_sprite.center_y < enemy.center_y + 25:
                                    self.collider_sprite.center_x = enemy.center_x
                                    self.collider_sprite.center_y = enemy.center_y

                            # Adds enemies with a collider over them into the enemies_hit list
                            enemies_hit = arcade.check_for_collision_with_list(self.collider_sprite, self.enemy_list)
                            
                            # Damages enemies with Collider over them. Kills them if their health drops to 0
                            for enemy in enemies_hit:
                                enemy.cur_health -= 5
                                if enemy.cur_health <= 0:
                                    time.sleep(.5)
                                    enemy.remove_from_sprite_lists()
                            self.target_selected = False
                            self.your_turn = False
                            box.is_clicked = False
                    
                    # Heals player associated with box
                    elif box.is_clicked and box.box_type == "heal":
                        for player in self.player_list:
                            if player.name == box.associated_player and player.cur_health <= player.max_health - 3:
                                player.cur_health += 3
                            elif player.name == box.associated_player and player.cur_health < player.max_health:
                                player.cur_health = player.max_health
                        box.is_clicked = False
                        self.your_turn = False
            
            # Enemy attacks player
            else:
                hit = random.randrange(2)
                if hit == 0:
                    indexes = []
                    for player in self.player_list:
                        indexes.append(self.player_list.index(player))
                    target = random.randrange(len(indexes))
                    for player in self.player_list:
                        if target == self.player_list.index(player):
                            self.collider_sprite.center_x = player.center_x
                            self.collider_sprite.center_y = player.center_y
                    
                    players_hit = arcade.check_for_collision_with_list(self.collider_sprite, self.player_list)

                    for player in players_hit:
                        player.cur_health -= 5
                        if player.cur_health <= 0:
                            time.sleep(.5)
                            player.remove_from_sprite_lists()
                self.your_turn = True

        
def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

""" 
if __name__ == "__main__":
    main()
"""