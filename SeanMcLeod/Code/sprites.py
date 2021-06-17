#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the monster class

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
        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()
        self.rect = pygame.Rect(self._sprite_x, self._sprite_y, self.width, self.height)
        self.current_sprite = 0

    def sprite_upload(self):
        self._screen.blit(self._sprite, (self.rect.x, self.rect.y))

    def flip_sprite(self):
        self._sprite = pygame.transform.flip(self._sprite, True, False)

    def set_rect(self, new_rect):
        self.rect = new_rect

    def modify_sprite_size(self, multiplier):
        # get sprite's size
        sprite_size = self._sprite.get_size()
        # increase size of sprite and rect
        self._sprite = pygame.transform.scale(
            self._sprite, (sprite_size[0] * multiplier, sprite_size[1] * multiplier)
        )
        self.rect.size = self._sprite.get_size()

    def check_collision(self, sprite1, sprite2):
        if sprite1.colliderect(sprite2):
            return True
        else:
            return False

    def sprite_move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

    def sprite_animation(self, sprite_list):
        self.current_sprite += 1
        if self.current_sprite >= len(sprite_list):
            self.current_sprite = 0

    def keep_inside_screen(self):
        if (
            self.rect.x >= constants.SCREEN_WIDTH - self._sprite.get_width()
            or self.rect.x <= 0
            or self.rect.y >= constants.SCREEN_HEIGHT - self._sprite.get_width()
            or self.rect.y <= 0
        ):
            self.rect.clamp_ip(self._screen.get_rect())
            return True
        else:
            return False

    def get_rect(self):
        return self.rect

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

    def print_anything(self):
        print("hey!")

    def draw_rect(self):
        pygame.draw.rect(self._screen, (255, 0, 0), self.rect)
