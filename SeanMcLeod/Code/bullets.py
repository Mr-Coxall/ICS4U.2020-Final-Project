#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the bullet class


import constants
import pygame
from pygame import mixer


class BulletClass:
    def __init__(self, screen, x_speed, y_speed):
        super().__init__()
        self._image = pygame.transform.rotate(
            pygame.image.load(constants.BULLET_IMAGE), constants.ROTATE_THREE_TIMES
        )
        self._x_speed = x_speed
        self._y_speed = y_speed
        self._screen = screen

    def handle_bullets(self, first_bullet_list, second_bullet_list, to_shoot):
        # remove if collided or out of the screen
        for bullet in first_bullet_list:
            bullet.y += self._y_speed
            if to_shoot.colliderect(bullet):
                first_bullet_list.remove(bullet)
                return True
            elif bullet.y >= constants.SCREEN_HEIGHT * 2:
                first_bullet_list.remove(bullet)

        for bullet in second_bullet_list:
            bullet.y -= self._y_speed
            if to_shoot.colliderect(bullet):
                second_bullet_list.remove(bullet)
                return True
            elif bullet.y >= constants.SCREEN_HEIGHT * 2:
                second_bullet_list.remove(bullet)

    def draw(self, first_bullet_list, second_bullet_list):
        for bullet in first_bullet_list:
            pygame.draw.rect(self._screen, constants.RED, bullet)
        for bullet in second_bullet_list:
            pygame.draw.rect(self._screen, constants.WHITE, bullet)

    def create_bullets(
        self, first_bullet_list, second_bullet_list, first_rect, second_rect
    ):
        bullet = pygame.Rect(
            first_rect.x + first_rect.width / 2,
            first_rect.y + first_rect.height,
            constants.BULLET_WIDTH,
            constants.BULLET_HEIGHT,
        )
        first_bullet_list.append(bullet)

        bullet = pygame.Rect(
            second_rect.x + second_rect.width / 2,
            second_rect.y - second_rect.height / 2 + 10,
            constants.BULLET_WIDTH,
            constants.BULLET_HEIGHT,
        )
        second_bullet_list.append(bullet)

        laser_sound = mixer.Sound(constants.LASER_SOUND)
        laser_sound.play()
