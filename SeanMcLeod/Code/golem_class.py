#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the golem class

import pygame
from monsters import Monsters


class GolemClass(Monsters):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)
        self._golem_walk_right = [
            pygame.image.load("Sprites/golems/golem-walk (1).png"),
            pygame.image.load("Sprites/golems/golem-walk (2).png"),
            pygame.image.load("Sprites/golems/golem-walk (3).png"),
            pygame.image.load("Sprites/golems/golem-walk (4).png"),
            pygame.image.load("Sprites/golems/golem-walk (5).png"),
            pygame.image.load("Sprites/golems/golem-walk (6).png"),
        ]
        self._looking_right = True

    def golem_move(self):
        super().sprite_move(super().get_x_speed(), super().get_y_speed())
        if super().keep_inside_screen():
            super().set_x_speed(super().get_x_speed() * -1)
            self._looking_right = not self._looking_right

        self.set_animation()

        super().set_sprite(self._golem_walk_right[super().get_current_sprite()])

        if not self._looking_right:
            super().flip_sprite()

    def set_animation(self):
        # loop through the sprite list and if it reaches the end, start back at sprite 0
        super().set_current_sprite(super().get_current_sprite() + 1)
        if super().get_current_sprite() >= len(self._golem_walk_right):
            super().set_current_sprite(0)
