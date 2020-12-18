import arcade
import random
from Start import dedicationScreen
from BattleScene import battleSceneRunner, battleSceneClasses

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
        # Initialize window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "GAME")
        arcade.set_background_color(arcade.color.BLACK)

        self.game_started = False


        """Used in battleSceneRunner"""
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

        # number of enemies
        self.enemy_count = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

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

    # Draws sprites and other game objects (good)
    def on_draw(self):
        arcade.start_render()

        if not self.game_started:
            dedicationScreen.dedication_screen_draw(SCREEN_WIDTH, SCREEN_HEIGHT)
        else:
            # Draws all of the battle things
            self.enemy_list.draw()
            self.player_list.draw()
            self.box_list.draw()
            self.cursor_list.draw()
            battleSceneRunner.battle_scene_draw(SCREEN_WIDTH, SCREEN_HEIGHT, self.enemy_list, self.player_list, self.box_list, self.cursor_list, self.target_selected)

    # Updates game (good)
    def on_update(self, delta_time: float):
        if self.game_started:
            battleSceneRunner.update_battle(self.enemy_list, self.player_list, self.box_list, self.target_selected, self.your_turn, self.collider_sprite, self.collider_sprite.center_x, self.collider_sprite.center_y, self.cursor_sprite.center_x, self.cursor_sprite.center_y)

    # Lets cursor move (good)
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.game_started:
            self.cursor_sprite.center_x = x
            self.cursor_sprite.center_y = y


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.game_started:    
            battleSceneRunner.mouse_press(self.box_list, self.enemy_list, self.target_selected, self.cursor_sprite.center_x, self.cursor_sprite.center_y)        

    # Does key stuff (good)
    def on_key_press(self, key, modifiers):
            if key == arcade.key.SPACE:
                if not self.game_started:
                    self.game_started = True
                else:
                    battleSceneRunner.action_box_use(SCREEN_WIDTH, self.box_list)
            
            if key == arcade.key.D and self.game_started:
                battleSceneRunner.switch_box_right(SCREEN_WIDTH, self.box_list, self.player_list)

            if key == arcade.key.A and self.game_started:
                battleSceneRunner.switch_box_left(SCREEN_WIDTH, self.box_list, self.player_list)
