#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the shadow class

import constants
import pygame
from monsters import Monsters


class ShadowClass(Monsters):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)
        self._shadow_list = []
        super().set_rect(
            pygame.Rect(
                constants.SHADOW_X,
                constants.SHADOW_Y,
                constants.SCREEN_WIDTH,
                super().get_height(),
            )
        )

    def upload(self):
        for counter in range(constants.SHADOW_NUMBER):
            self._shadow_list.append(super().get_sprite())
            # pygame.draw.rect(self._screen, (255, 0, 0), self.rect)
            self._screen.blit(
                super().get_sprite(),
                (constants.SHADOW_DISTANCE * counter, super().get_rect().y),
            )
        super().sprite_move(super().get_x_speed(), super().get_y_speed())
