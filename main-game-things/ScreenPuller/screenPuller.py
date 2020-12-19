"""This is the main place where different screens are pulled.
Many functions are also called here"""

import arcade
import random
import time
from Start import dedicationScreen
from BattleScene import battleSceneRunner, battleSceneClasses
from Environment import environmentRunner, environmentClasses

SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 750

class Collider(arcade.Sprite):
    def update(self):
        
        if self.center_x < SCREEN_WIDTH + 50:
            self.center_x = SCREEN_WIDTH + 50

        if self.center_y < SCREEN_HEIGHT + 50:
            self.center_y = SCREEN_HEIGHT + 50


class Screenmake(arcade.Window):
    def __init__(self):

        """Skeleton"""

        # Initialize window and cursor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "GAME")
        arcade.set_background_color(arcade.color.BLACK)

        self.cursor_list = None
        self.cursor_sprite = None
        # Hide mouse
        self.set_mouse_visible(False)

        # keeps track of setup. No purpose (yet)
        self.isSetup = False

        """Used in environment (for walking around)"""
        self.in_environment = False

        # Sprites in environment
        self.adventurer_list = None
        self.wall_list = None

        self.adventurer_sprite = None
        self.wall_sprite = None

        """Used in battleSceneRunner (for battles)"""
        self.battle_started = False

        # Sprites in battle
        self.enemy_list = None
        self.player_list = None
        self.box_list = None
        self.collider_list = None

        # Sprites info
        self.enemy_sprite = None
        self.player_sprite = None
        self.box_sprite = None
        self.collider_sprite = None

        # Your turn indicator
        self.your_turn = False
        self.coin_flip = 0

        # Indicator for selected targets
        self.target_selected = False
        self.time_for_attack = False

        # number of enemies
        self.enemy_count = 0

        # number of alive players
        self.players_alive = 0

    def setup(self):
        """Set up the game and initialize the variables."""

        """Skeleton setup"""
        # Mouse cursor
        self.cursor_sprite = arcade.Sprite("Cursor.png", 1)
        self.cursor_sprite.center_x = SCREEN_WIDTH / 2
        self.cursor_sprite.center_y = SCREEN_HEIGHT / 2
        self.cursor_list.append(self.cursor_sprite)

        """Environment setup"""
        # Wall creation and placement
        for i in range(int(SCREEN_WIDTH / 64 + 1)):
            self.wall_sprite = environmentClasses.Wall("Box.png", 1)
            self.wall_sprite.center_x = i * 64
            self.wall_sprite.center_y = 0
            self.wall_list.append(self.wall_sprite)
        for i in range(int(SCREEN_WIDTH / 64 + 1)):
            self.wall_sprite = environmentClasses.Wall("Box.png", 1)
            self.wall_sprite.center_x = i * 64
            self.wall_sprite.center_y = SCREEN_HEIGHT
            self.wall_list.append(self.wall_sprite)
        for i in range(int(SCREEN_HEIGHT/ 64 + 1)):
            self.wall_sprite = environmentClasses.Wall("Box.png", 1)
            self.wall_sprite.center_y = i * 64
            self.wall_sprite.center_x = SCREEN_WIDTH
            self.wall_list.append(self.wall_sprite)
        for i in range(int(SCREEN_HEIGHT/ 64 + 1)):
            self.wall_sprite = environmentClasses.Wall("Box.png", 1)
            self.wall_sprite.center_y = i * 64
            self.wall_sprite.center_x = 0
            self.wall_list.append(self.wall_sprite)
        
        # Adventurer
        self.adventurer_sprite = environmentClasses.Adventurer("Protagonist.png", 1)
        self.adventurer_list.append(self.adventurer_sprite)

        """Battle sequence setup"""
        # Sprite lists
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.box_list = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()
        self.collider_list = arcade.SpriteList()

        self.enemy_count = random.randrange(3) + 1

        # All Sprite images made in Piskel
        # Enemies
        for i in range(self.enemy_count):
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

        self.players_alive = len(self.player_list)

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

    # Draws sprites and other game objects
    def on_draw(self):
        arcade.start_render()

        if not self.battle_started and not self.in_environment:
            dedicationScreen.dedication_screen_draw(SCREEN_WIDTH, SCREEN_HEIGHT)
        
        elif self.battle_started:
            # Draws all of the battle things
            self.enemy_list.draw()
            if self.players_alive > 0:
                self.player_list.draw()
                if len(self.enemy_list) > 0:
                    self.box_list.draw()
            self.cursor_list.draw()
            battleSceneRunner.battle_scene_draw(SCREEN_WIDTH, SCREEN_HEIGHT, self.enemy_list, self.player_list, self.box_list, self.target_selected, self.players_alive)
            if len(self.enemy_list) == 0:
                time.sleep(1)
                self.battle_started = False
                self.in_environment = True

        elif self.in_environment:
            # Draws environment
            self.cursor_list.draw()
            self.wall_list.draw()
            self.adventurer_list.draw()

    # Updates game
    def on_update(self, delta_time: float):
        if self.battle_started:
            if len(self.enemy_list) > 0 and self.players_alive > 0:
                if self.your_turn:

                    #checks to see if any boxes were clicked
                    for box in self.box_list:
                        if box.is_clicked and box.box_type == "attack":
                            if self.target_selected:
                                indexes = []
                                for enemy in self.enemy_list:
                                    indexes.append(self.enemy_list.index(enemy))
                                for enemy in self.enemy_list:
                                    if enemy.center_x - 40 < self.cursor_sprite.center_x < enemy.center_x + 40 \
                                        and enemy.center_y - 25 < self.cursor_sprite.center_y < enemy.center_y + 25:
                                        self.collider_sprite.center_x = battleSceneRunner.position_collider_x(enemy)
                                        self.collider_sprite.center_y = battleSceneRunner.position_collider_y(enemy)

                                         # Adds enemies with a collider over them into the enemies_hit list
                                        enemies_hit = arcade.check_for_collision_with_list(self.collider_sprite, self.enemy_list)

                                        battleSceneRunner.hit_enemy(enemies_hit)
                                        self.target_selected = False
                                        self.your_turn = False
                                        for box in self.box_list:
                                            box.is_clicked = False

                        elif box.is_clicked and box.box_type == "heal":
                            battleSceneRunner.heal_player(self.player_list, box)
                            box.is_clicked = False
                            self.your_turn = False
                        
                else:
                    hit = random.randrange(3)
                    if hit == 0:
                        indexes = []
                        for player in self.player_list:
                            indexes.append(self.player_list.index(player))
                        target = random.randrange(len(indexes))
                        for player in self.player_list:
                            if target == self.player_list.index(player):
                                self.collider_sprite.center_x = battleSceneRunner.position_collider_x(player)
                                self.collider_sprite.center_y = battleSceneRunner.position_collider_y(player)
                        players_hit = arcade.check_for_collision_with_list(self.collider_sprite, self.player_list)
                        for player in players_hit:
                            self.players_alive = battleSceneRunner.enemy_hit_player(player, self.players_alive)
                    self.your_turn = True
    
    # Lets cursor move
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.battle_started or self.in_environment:
            self.cursor_sprite.center_x = x
            self.cursor_sprite.center_y = y


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.battle_started:    
            self.target_selected = battleSceneRunner.check_for_selection(self.box_list, self.enemy_list, self.cursor_sprite.center_x, self.cursor_sprite.center_y)        

    # Does key stuff
    def on_key_press(self, key, modifiers):
            if key == arcade.key.SPACE:
                if not self.battle_started:
                    self.battle_started = True
                elif self.battle_started and len(self.enemy_list) > 0:
                    battleSceneRunner.action_box_use(SCREEN_WIDTH, self.box_list)
            
            if key == arcade.key.D and self.battle_started and len(self.enemy_list) > 0:
                battleSceneRunner.switch_box_right(SCREEN_WIDTH, self.box_list, self.player_list)

            if key == arcade.key.A and self.battle_started and len(self.enemy_list) > 0:
                battleSceneRunner.switch_box_left(SCREEN_WIDTH, self.box_list, self.player_list)
