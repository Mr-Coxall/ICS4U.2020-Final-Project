#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the display class

import constants
import pygame
from golem_class import GolemClass
from maps import Maps
from monsters import Monsters
from prisoner_class import PrisonerClass
from shadow_class import ShadowClass
from ship_class import ShipClass
from sprites import Sprites


class SetUpDisplay:
    def __init__(self, screen):
        self._screen = screen

    def set_up_game_scene_one(self):
        prisoner_x = 700
        prisoner_y = 450
        tile_x_increment = 60
        tile_y_increment = 50

        # create sprites
        prisoner = pygame.image.load(constants.PRISONER_IMAGE)
        golem = pygame.image.load(constants.GOLEM_IMAGE)
        dragon = pygame.image.load(constants.DRAGON_IMAGE)
        tile = pygame.image.load(constants.CELL_IMAGE)
        door = pygame.image.load(constants.DOOR_IMAGE)

        # objects
        my_prisoner = PrisonerClass(
            prisoner,
            prisoner_x,
            prisoner_y,
            constants.PRISONER_X_SPEED,
            constants.PRISONER_Y_SPEED,
            self._screen,
        )
        my_golem = GolemClass(
            golem,
            constants.GOLEM_ONE_X,
            constants.GOLEM_ONE_Y,
            constants.GOLEM_SPEED[0],
            constants.GOLEM_SPEED[1],
            self._screen,
        )
        my_golem_two = GolemClass(
            golem,
            constants.GOLEM_TWO_X,
            constants.GOLEM_TWO_Y,
            constants.GOLEM_SPEED[0],
            constants.GOLEM_SPEED[1],
            self._screen,
        )
        my_dragon = Monsters(
            dragon,
            constants.DRAGON_X,
            constants.DRAGON_Y,
            0,
            0,
            self._screen,
        )
        my_cell_map = Maps(
            tile,
            tile_x_increment,
            tile_y_increment,
            self._screen,
            1,
        )
        my_door = Sprites(
            door,
            constants.FIRST_DOOR_X,
            constants.FIRST_DOOR_Y,
            0,
            0,
            self._screen,
        )

        return my_prisoner, my_golem, my_golem_two, my_dragon, my_cell_map, my_door

    def set_up_game_scene_two(self):
        prisoner_x = 400
        prisoner_y = 200
        tile_x_increment = 100
        tile_y_increment = 57

        # create sprites
        prisoner = pygame.image.load(constants.PRISONER_IMAGE)
        tile = pygame.image.load(constants.WIRE_IMAGE)
        door = pygame.image.load(constants.CASTLE_DOOR_IMAGE)
        chest = pygame.image.load(constants.CHEST_IMAGE)
        key = pygame.image.load(constants.KEY_IMAGE)
        shadow = pygame.image.load(constants.SHADOW_IMAGE)

        # create object
        my_prisoner = PrisonerClass(
            prisoner,
            prisoner_x,
            prisoner_y,
            constants.PRISONER_X_SPEED,
            constants.PRISONER_Y_SPEED,
            self._screen,
        )
        my_door = Sprites(
            door, constants.SECOND_DOOR_X, constants.SECOND_DOOR_Y, 0, 0, self._screen
        )
        my_cell_map = Maps(tile, tile_x_increment, tile_y_increment, self._screen, 2)
        my_chest = Sprites(
            chest, constants.CHEST_X, constants.CHEST_Y, 0, 0, self._screen
        )
        my_key = Sprites(key, constants.KEY_X, constants.KEY_Y, 0, 0, self._screen)
        my_shadow = ShadowClass(
            shadow,
            constants.SHADOW_X,
            constants.SHADOW_Y,
            constants.SHADOW_X_SPEED,
            constants.SHADOW_Y_SPEED,
            self._screen,
        )

        return my_prisoner, my_door, my_cell_map, my_chest, my_key, my_shadow

    def set_up_game_scene_three(self):
        prisoner_x = 400
        prisoner_y = 500

        # create sprites
        prisoner = pygame.image.load(constants.PRISONER_IMAGE)
        ship = pygame.image.load(constants.SHIP_IMAGE)

        # create object
        my_prisoner = PrisonerClass(
            prisoner,
            prisoner_x,
            prisoner_y,
            constants.PRISONER_X_SPEED,
            constants.PRISONER_Y_SPEED,
            self._screen,
        )
        my_ship = ShipClass(
            ship,
            constants.SHIP_X,
            constants.SHIP_Y,
            constants.SHIP_X_SPEED,
            constants.SHIP_Y_SPEED,
            self._screen,
        )

        return my_prisoner, my_ship
