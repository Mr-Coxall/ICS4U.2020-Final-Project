import sys

import pygame


class CheckPrisonerEvents:
    def __init__(self):
        self.key_left = False
        self.key_right = False
        self.key_up = False
        self.key_down = False
        self.key_is_up = False
        self.key_is_down = False

    def check_events(self):
        # every loop, set these values to False in order to refresh them
        self.key_left = False
        self.key_right = False
        self.key_up = False
        self.key_down = False
        self.key_is_up = False
        self.key_is_down = False
        # for events, check what key is pressed and return the values
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.key_is_down = True
                if event.key == pygame.K_LEFT:
                    self.key_left = True
                if event.key == pygame.K_RIGHT:
                    self.key_right = True
                if event.key == pygame.K_UP:
                    self.key_up = True
                if event.key == pygame.K_DOWN:
                    self.key_down = True

            if event.type == pygame.KEYUP:
                self.key_is_up = True
            if event.type == pygame.QUIT:
                sys.exit()

        return (
            self.key_is_down,
            self.key_left,
            self.key_right,
            self.key_up,
            self.key_down,
            self.key_is_up,
        )
