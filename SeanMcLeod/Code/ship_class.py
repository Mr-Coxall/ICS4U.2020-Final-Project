#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the ship class

from monsters import Monsters


class ShipClass(Monsters):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)
