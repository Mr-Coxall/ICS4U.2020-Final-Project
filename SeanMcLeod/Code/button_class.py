#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the button class

import pygame


class ButtonClass:
    def __init__(self, color, position_x, position_y, width, height, text=""):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self, screen, text_size, outline=None):
        # draw button
        if outline:
            pygame.draw.rect(
                screen,
                outline,
                (
                    self.position_x - 2,
                    self.position_y - 2,
                    self.width + 4,
                    self.height + 4,
                ),
                0,
            )

        pygame.draw.rect(
            screen,
            self.color,
            (self.position_x, self.position_y, self.width, self.height),
            0,
        )

        if self.text != "":
            # draw text
            font = pygame.font.SysFont("comicsansms", text_size)
            text = font.render(self.text, True, (0, 0, 0))
            screen.blit(
                text,
                (
                    self.position_x + (self.width / 2 - text.get_width() / 2),
                    self.position_y + (self.height / 2 - text.get_height() / 2),
                ),
            )

    def is_over(self, mouse_pos):
        # check if the mouse is over the button
        if self.position_x < mouse_pos[0] < self.position_x + self.width:
            if self.position_y < mouse_pos[1] < self.position_y + self.height:
                return True

        return False
