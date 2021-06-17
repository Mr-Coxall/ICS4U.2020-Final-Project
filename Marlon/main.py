#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the main file for "The Long Way Home" game

# import arcade class
import arcade

# import constants
import constants

# import game class from game file
from startup import startView


# main function
def main():
    # creates window instance
    window = arcade.Window(
        constants.SCREEN_WIDTH,
        constants.SCREEN_HEIGHT,
        constants.SCREEN_TITLE,
    )
    start_view = startView()
    window.show_view(start_view)
    start_view.setup()
    # calls arcade class method
    arcade.run()


if __name__ == "__main__":
    main()
