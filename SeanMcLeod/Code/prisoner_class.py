import pygame
from Sprites import Sprites


class PrisonerClass(Sprites):
    def __init__(self, sprite, sprite_x, sprite_y, x_speed, y_speed, screen):
        super().__init__(sprite, sprite_x, sprite_y, x_speed, y_speed, screen)
        self.prisoners = [
            pygame.image.load("Sprites/prisoners/prisoner2.png"),
            pygame.image.load("Sprites/prisoners/prisoner3.png"),
            pygame.image.load("Sprites/prisoners/prisoner4.png"),
            pygame.image.load("Sprites/prisoners/prisoner5.png"),
            pygame.image.load("Sprites/prisoners/prisoner6.png"),
            pygame.image.load("Sprites/prisoners/prisoner7.png"),
            pygame.image.load("Sprites/prisoners/prisoner8.png"),
            pygame.image.load("Sprites/prisoners/prisoner9.png"),
        ]
        self.is_animating = False
        self.looking_right = False
        self.prisoner_x_change = 0
        self.prisoner_y_change = 0

    def prisoner_animation(self):
        self.sprite_animation(self.prisoners)
        if self.is_animating:
            self.set_sprite(self.prisoners[self.current_sprite])
        else:
            self.set_sprite(pygame.image.load("Sprites/prisoners/prisoner.png"))

    def prisoner_flip(self):
        if not self.looking_right:
            self.flip_sprite()

    def prisoner_move(
        self, key_is_down, key_left, key_right, key_up, key_down, key_is_up
    ):
        if key_is_down:
            if key_left:
                self.is_animating = True
                self.looking_right = False
                self.prisoner_x_change = -self.get_x_speed()
            if key_right:
                self.is_animating = True
                self.looking_right = True
                self.prisoner_x_change = self.get_x_speed()
            if key_up:
                self.is_animating = True
                self.prisoner_y_change = -self.get_y_speed()
            if key_down:
                self.is_animating = True
                self.prisoner_y_change = self.get_y_speed()
        if key_is_up:
            self.is_animating = False
            self.prisoner_x_change = 0
            self.prisoner_y_change = 0

        self.sprite_move(self.prisoner_x_change, self.prisoner_y_change)
