#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the map class

import constants
import pygame


class Maps:
    def __init__(self, sprite, tile_x_distance, tile_y_distance, screen, level):
        self._screen = screen
        self._sprite = sprite
        self._width = self._sprite.get_width()
        self._height = self._sprite.get_height()
        self._maps = []
        self._level = level
        self._tile_x_distance = tile_x_distance
        self._tile_y_distance = tile_y_distance
        self._rotated_sprite = pygame.transform.rotate(
            self._sprite, constants.RIGHT_ANGLE
        )
        self._rotated_width = self._rotated_sprite.get_width()
        self._rotated_height = self._rotated_sprite.get_height()
        self._new_rect = self._sprite.get_rect()
        self._reduce_distance = self._tile_y_distance / 2
        self._game_scene_one_map = """





wwwwwwwwww  ww""".splitlines()

        self._game_scene_two_map = """
 rr
 rwww w
 r     r
wwwwwww
     r
 r   r
 wwww ww

wwwww wwww
""".splitlines()
        self._maps.append(self._game_scene_one_map)
        self._maps.append(self._game_scene_two_map)

    def build_map(self, sprite2):
        for nth_line, line in enumerate(self._maps[self._level - 1]):
            for nth_character, character in enumerate(line):
                if character == "w":
                    self._screen.blit(
                        self._sprite,
                        (
                            nth_character * self._tile_x_distance,
                            nth_line * self._tile_y_distance,
                        ),
                    )
                    new_rect = pygame.Rect(
                        nth_character * self._tile_x_distance,
                        nth_line * self._tile_y_distance,
                        self._width,
                        self._height,
                    )
                    # check collision
                    if new_rect.colliderect(sprite2):
                        return True
                elif character == "r":
                    rotated_rect = pygame.Rect(
                        nth_character * self._tile_x_distance,
                        nth_line * self._tile_y_distance - self._reduce_distance,
                        self._rotated_width,
                        self._rotated_height,
                    )
                    self._screen.blit(
                        self._rotated_sprite,
                        (
                            nth_character * self._tile_x_distance,
                            nth_line * self._tile_y_distance - self._reduce_distance,
                        ),
                    )
                    # check collision
                    if rotated_rect.colliderect(sprite2):
                        return True
