#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the main file for "The Long Way Home" game

# import arcade class
import arcade
# import game class from game file
from game import longWayGame


# main function
def main():
    # creates window instance
    newWindow = longWayGame()
    # calls class methods
    newWindow.setup()
    # calls arcade class method
    arcade.run()


if __name__ == "__main__":
    main()
