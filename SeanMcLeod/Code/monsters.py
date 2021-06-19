#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the monster class
from sprites import Sprites


class Monsters(Sprites):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)

    def attack(self, prey):
        if super().check_collision(super().get_rect(), prey):
            return True
