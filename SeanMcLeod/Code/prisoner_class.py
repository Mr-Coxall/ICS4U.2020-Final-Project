#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the prisoner class

import pygame
from sprites import Sprites


class PrisonerClass(Sprites):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)
        self._prisoners = [
            pygame.image.load("Sprites/prisoners/prisoner2.png"),
            pygame.image.load("Sprites/prisoners/prisoner3.png"),
            pygame.image.load("Sprites/prisoners/prisoner4.png"),
            pygame.image.load("Sprites/prisoners/prisoner5.png"),
            pygame.image.load("Sprites/prisoners/prisoner6.png"),
            pygame.image.load("Sprites/prisoners/prisoner7.png"),
            pygame.image.load("Sprites/prisoners/prisoner8.png"),
            pygame.image.load("Sprites/prisoners/prisoner9.png"),
        ]
        self._is_animating = False
        self._looking_right = False
        self._prisoner_x_change = 0
        self._prisoner_y_change = 0

    def prisoner_animation(self):
        super().sprite_animation(self._prisoners)
        if self._is_animating:
            super().set_sprite(self._prisoners[super().get_current_sprite()])
        else:
            super().set_sprite(pygame.image.load("Sprites/prisoners/prisoner.png"))

    def prisoner_flip(self):
        if not self._looking_right:
            super().flip_sprite()

    def prisoner_move(
        self, key_is_down, key_left, key_right, key_up, key_down, key_is_up
    ):
        if key_is_down:
            if key_left:
                self._is_animating = True
                self._looking_right = False
                self._prisoner_x_change = -super().get_x_speed()
            if key_right:
                self._is_animating = True
                self._looking_right = True
                self._prisoner_x_change = super().get_x_speed()
            if key_up:
                self._is_animating = True
                self._prisoner_y_change = -super().get_y_speed()
            if key_down:
                self._is_animating = True
                self._prisoner_y_change = super().get_y_speed()
        if key_is_up:
            self._is_animating = False
            self._prisoner_x_change = 0
            self._prisoner_y_change = 0

        super().sprite_move(self._prisoner_x_change, self._prisoner_y_change)
