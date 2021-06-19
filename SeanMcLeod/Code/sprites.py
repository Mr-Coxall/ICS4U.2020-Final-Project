# !/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the sprites class

import constants
import pygame


class Sprites:
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        self._sprite = sprite
        self._sprite_x = sprite_x
        self._sprite_y = sprite_y
        self._x_speed = x_speed
        self._y_speed = y_speed
        self._screen = screen
        self._width = self._sprite.get_width()
        self._height = self._sprite.get_height()
        self._rect = pygame.Rect(
            self._sprite_x, self._sprite_y, self._width, self._height
        )
        self._current_sprite = 0

    def sprite_upload(self):
        self._screen.blit(self._sprite, (self._rect.x, self._rect.y))

    def flip_sprite(self):
        self._sprite = pygame.transform.flip(self._sprite, True, False)

    def set_rect(self, new_rect):
        self._rect = new_rect

    def modify_sprite_size(self, multiplier):
        # get sprite's size
        sprite_size = self._sprite.get_size()
        # increase size of sprite and _rect
        self._sprite = pygame.transform.scale(
            self._sprite, (sprite_size[0] * multiplier, sprite_size[1] * multiplier)
        )
        self._rect.size = self._sprite.get_size()

    def check_collision(self, sprite1, sprite2):
        if sprite1.colliderect(sprite2):
            return True
        else:
            return False

    def sprite_move(self, x_change, y_change):
        self._rect.x += x_change
        self._rect.y += y_change

    def sprite_animation(self, sprite_list):
        self._current_sprite += 1
        if self._current_sprite >= len(sprite_list):
            self._current_sprite = 0

    def keep_inside_screen(self):
        if (
            self._rect.x >= constants.SCREEN_WIDTH - self._sprite.get_width()
            or self._rect.x <= 0
            or self._rect.y >= constants.SCREEN_HEIGHT - self._sprite.get_height()
            or self._rect.y <= 0
        ):
            self._rect.clamp_ip(self._screen.get_rect())
            return True
        else:
            return False

    def get_rect(self):
        return self._rect

    def get_sprite_x(self):
        return self._sprite_x

    def set_sprite_x(self, new_sprite_x):
        self._sprite_x = new_sprite_x

    def get_sprite_y(self):
        return self._sprite_y

    def set_sprite_y(self, new_sprite_y):
        self._sprite_y = new_sprite_y

    def get_x_speed(self):
        return self._x_speed

    def set_x_speed(self, new_x_speed):
        self._x_speed = new_x_speed

    def get_y_speed(self):
        return self._y_speed

    def set_y_speed(self, new_y_speed):
        self._y_speed = new_y_speed

    def get_sprite(self):
        return self._sprite

    def set_sprite(self, new_sprite):
        self._sprite = new_sprite

    def get_width(self):
        return self._sprite.get_width()

    def set_width(self, new_width):
        self._width = new_width

    def get_height(self):
        return self._sprite.get_height()

    def set_height(self, new_height):
        self._height = new_height

    def get_current_sprite(self):
        return self._current_sprite

    def set_current_sprite(self, new_current_sprite):
        self._current_sprite = new_current_sprite

    def draw_rect(self):
        pygame.draw.rect(self._screen, (255, 0, 0), self._rect)
