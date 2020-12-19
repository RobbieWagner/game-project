import arcade

class Adventurer(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)

class Wall(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)

class Encounter(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        