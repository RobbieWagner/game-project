""" This code runs the game. Run this when you want to play"""

import arcade
from BattleScene import battleSceneRunner, battleSceneClasses
from Start import dedicationScreen
from ScreenPuller import screenPuller


def main():
    """Pulls up dedication screen"""
    window = screenPuller.Screenmake()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
