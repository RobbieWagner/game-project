import arcade

SCREEN_WIDTH = 1375
SCREEN_HEIGHT = 750

class Enemy(arcade.Sprite):
    def __init__(self, type, image, scale, max_health):
        self.type = type
        super().__init__(image, scale)
        self.max_health = max_health
        self.cur_health = max_health


class Player(arcade.Sprite):
    def __init__(self, name, image, scale, max_health):
        self.name = name
        super().__init__(image, scale)
        self.max_health = max_health
        self.cur_health = max_health


class Box(arcade.Sprite):
    def __init__(self, image, scale, is_clicked, box_type, associated_player):
        super().__init__(image, scale)
        self.is_clicked = is_clicked
        self.box_type = box_type
        self.associated_player = associated_player

class Collider(arcade.Sprite):
    def update(self):
        
        if self.center_x < SCREEN_WIDTH + 50:
            self.center_x = SCREEN_WIDTH + 50

        if self.center_y < SCREEN_HEIGHT + 50:
            self.center_y = SCREEN_HEIGHT + 50
