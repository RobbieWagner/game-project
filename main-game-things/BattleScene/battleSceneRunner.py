""" Sprite Sample Program """

import random
import arcade
import time
from BattleScene import battleSceneClasses

def battle_scene_draw(screen_width, screen_height, enemy_list, player_list, box_list, target_selected, alive_players):
    # Draws the healthbars for enemies and players
    for enemy in enemy_list:
        no_health_point = enemy.center_x - 30
        length = 60 * enemy.cur_health / enemy.max_health
    
        if length > 0:
            arcade.draw_lrtb_rectangle_outline(no_health_point - 2, enemy.center_x + 32, enemy.center_y - 45, enemy.center_y - 53, arcade.color.GRAY, 2)
            arcade.draw_lrtb_rectangle_filled(no_health_point, no_health_point + length, enemy.center_y - 47, enemy.center_y - 51, arcade.color.RED)
            arcade.draw_text(enemy.type, no_health_point - 2, enemy.center_y - 68, arcade.color.WHITE, 10, 40, "left")

    for player in player_list:
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
    for box in box_list:
        if box.box_type == "attack" and box.is_clicked and not target_selected:
            for enemy in enemy_list:
                arcade.draw_lrtb_rectangle_outline(enemy.center_x - 40, enemy.center_x + 40, enemy.center_y + 25, enemy.center_y - 25, arcade.color.LIGHT_RED_OCHRE, 2)

    if alive_players == 0:
        arcade.draw_text("GAME OVER", screen_width / 2 - 50, screen_height * 3 / 4, arcade.color.RED, 15, 100, "center")
    if len(enemy_list) == 0:
        arcade.draw_text("YOU WIN", screen_width / 2 - 50, screen_height * 3 / 4, arcade.color.WHITE, 15, 100, "center")
    
    arcade.draw_lrtb_rectangle_outline(0, screen_width, screen_height / 8, 0, arcade.color.WHITE_SMOKE, 10)

def position_collider_x(sprite):
    # Moves the Collider over to the slug when the box gets clicked (x direction)
    new_collider_x = sprite.center_x
    return new_collider_x

def position_collider_y(sprite):
    # Moves the Collider over to the slug when the box gets clicked (x direction)
    new_collider_y = sprite.center_y
    return new_collider_y

def hit_enemy(enemies_hit):
    for enemy in enemies_hit:
        enemy.cur_health -= 5
        if enemy.cur_health <= 0:
            time.sleep(.5)
            enemy.remove_from_sprite_lists()

def heal_player(player_list, box):
            # Heals player associated with box
                for player in player_list:
                    if player.name == box.associated_player and player.cur_health <= player.max_health - 3:
                        player.cur_health += 3
                    elif player.name == box.associated_player and player.cur_health < player.max_health:
                        player.cur_health = player.max_health
    
    # Enemy attacks player
def enemy_hit_player(player, players_alive):
    player.cur_health -= 5
    if player.cur_health <= 0:
        time.sleep(.5)
        players_alive -= 1
    return players_alive

def mouse_press(box_list, enemy_list, cursor_sprite_center_x, cursor_sprite_center_y):
    # Tracks which enemy is selected
    for box in box_list:
        if box.is_clicked and box.box_type == "attack":
            for enemy in enemy_list:
                if enemy.center_x - 40 < cursor_sprite_center_x < enemy.center_x + 40 \
                    and enemy.center_y - 25 < cursor_sprite_center_y < enemy.center_y + 25:
                    return True
    return False

def action_box_use(screen_width, box_list):
    for box in box_list:
        if not box.center_x == screen_width + 50:
            box.is_clicked = True

def switch_box_right(screen_width, box_list, player_list):
    value = 0
    for box in box_list:
        if not box.center_x == screen_width + 50 and not box_list.index(box) == len(box_list) - 1:
            value = box_list.index(box) + 1
        elif not box.center_x == screen_width + 50 and box_list.index(box) == len(box_list) - 1:
            value = 0
    for box in box_list:
        for player in player_list:
            if value == box_list.index(box) and player.name == box.associated_player:
                box.center_x = player.center_x
                box.center_y = player.center_y + 100
            else:
                box.center_x = screen_width + 50
                box.center_y = screen_width + 50

def switch_box_left(screen_width, box_list, player_list):
    value = 0
    for box in box_list:
        if not box.center_x == screen_width + 50 and not box_list.index(box) == 0:
            value = box_list.index(box) - 1
        elif not box.center_x == screen_width + 50 and box_list.index(box) == 0:
            value = len(box_list) - 1
    for box in box_list:
        for player in player_list:
            if value == box_list.index(box) and player.name == box.associated_player:
                box.center_x = player.center_x
                box.center_y = player.center_y + 100
            else:
                box.center_x = screen_width + 50
                box.center_y = screen_width + 50
