#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the monster class

import pygame
from monsters import Monsters


class GolemClass(Monsters):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)
        self.golem_walk_right = [
            pygame.image.load("Sprites/golems/golem-walk (1).png"),
            pygame.image.load("Sprites/golems/golem-walk (2).png"),
            pygame.image.load("Sprites/golems/golem-walk (3).png"),
            pygame.image.load("Sprites/golems/golem-walk (4).png"),
            pygame.image.load("Sprites/golems/golem-walk (5).png"),
            pygame.image.load("Sprites/golems/golem-walk (6).png"),
        ]
        self.current_sprite = 0
        self.looking_right = True

    def golem_move(self):
        self.sprite_move(self.get_x_speed(), self.get_y_speed())
        if self.keep_inside_screen():
            self.set_x_speed(self.get_x_speed() * -1)
            self.looking_right = not self.looking_right

        self.current_sprite += 1
        if self.current_sprite >= len(self.golem_walk_right):
            self.current_sprite = 0

        self.set_sprite(self.golem_walk_right[self.current_sprite])

        if not self.looking_right:
            self.flip_sprite()
