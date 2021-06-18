#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the ship class

import constants
from bullets import BulletClass
from monsters import Monsters


class ShipClass(Monsters):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)

    def ship_move(self):
        super().sprite_move(super().get_x_speed(), super().get_y_speed())
        if self.keep_inside_screen():
            super().set_x_speed(super().get_x_speed() * -1)

    def create_bullet(self):
        return BulletClass(
            super().get_rect().x + constants.SHIP_MIDDLE_X,
            super().get_rect().y + constants.SHIP_MIDDLE_Y,
            constants.BULLET_X_SPEED,
            constants.BULLET_Y_SPEED,
        )
