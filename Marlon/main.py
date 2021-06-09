#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the main file for "The Long Way Home" game

import arcade
import constants

class MyGame(arcade.Window):
    # main game class
    def __init__(self):

       # Call the parent class and set up the window
       super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # set background colour of window
       arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        # function to be used for gameplay
        pass

    def on_draw(self):
        # redener screen

        arcade.start_render()
        # Code to draw the screen goes here


def main():
    # creates window instance
    window = MyGame()
    # calls class methods
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
