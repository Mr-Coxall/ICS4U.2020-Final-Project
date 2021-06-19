#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the ship class

from monsters import Monsters


class ShipClass(Monsters):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)

    def ship_move(self):
        super().sprite_move(super().get_x_speed(), super().get_y_speed())
        if super().keep_inside_screen():
            super().set_x_speed(super().get_x_speed() * -1)
