#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the check prisoner event class

import sys

import pygame


class CheckPrisonerEvents:
    @staticmethod
    def check_events():
        # every loop, set these values to False in order to refresh them
        key_left = False
        key_right = False
        key_up = False
        key_down = False
        key_is_up = False
        key_is_down = False
        # for events, check what key is pressed and return the values
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_is_down = True
                if event.key == pygame.K_LEFT:
                    key_left = True
                if event.key == pygame.K_RIGHT:
                    key_right = True
                if event.key == pygame.K_UP:
                    key_up = True
                if event.key == pygame.K_DOWN:
                    key_down = True

            if event.type == pygame.KEYUP:
                key_is_up = True
            if event.type == pygame.QUIT:
                sys.exit()

        return key_is_down, key_left, key_right, key_up, key_down, key_is_up
