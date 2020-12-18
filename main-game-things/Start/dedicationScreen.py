import arcade
    
def dedication_screen_draw(screen_width, screen_height):
    arcade.draw_text("FOR THOSE WHO HOLD THE WEIGHT OF THE WORLD ON THEIR SHOULDERS", screen_width / 2 - 300, screen_height * 3 / 4, arcade.color.BLACK, 15, 600, "center")
    arcade.draw_text("PRESS SPACE TO START", screen_width / 2 - 200, screen_height / 4, arcade.color.WHITE, 15, 400, "center")
