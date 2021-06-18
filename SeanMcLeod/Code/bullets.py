#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the bullet class

import constants
import pygame


class BulletClass(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, x_speed, y_speed):
        super().__init__()
        self.image = pygame.transform.rotate(
            pygame.image.load(constants.BULLET_IMAGE), constants.ROTATE_THREE_TIMES
        )
        self._pos_y = pos_y
        self._pos_x = pos_x
        self._x_speed = x_speed
        self._y_speed = y_speed
        self.rect = pygame.Rect(
            self._pos_x, self._pos_y, self.image.get_width(), self.image.get_height()
        )

    def update(self, to_shoot):
        self.rect.y += self._y_speed

        if self.rect.y >= constants.SCREEN_HEIGHT:
            # if the bullet passes the screen, delete the bullet(for memory).
            self.kill()

        if self.rect.colliderect(to_shoot):
            print("SHOT")
