#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the game features file

import constants
import pygame


class ButtonClass:
    def __init__(self, color, position_x, position_y, width, height, text=""):
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(
            self.position_x, self.position_y, self.width, self.height
        )

    def draw_button(self, screen, text_size, text_font, outline=None):
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
            font = pygame.font.SysFont(text_font, text_size)
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

    def get_rect(self):
        return self.rect


class GetModifiedButton:
    def __init__(self):
        self._option_buttons_width = 180
        self._option_buttons_height = 100
        self._big_button_width = 300
        self._button_middle_position = constants.MIDDLE_X - self._big_button_width / 2

    def get_back_button(self):
        back_button = ButtonClass(
            constants.LIGHT_GREEN,
            constants.BACK_BUTTON_X,
            constants.BACK_BUTTON_Y,
            constants.BACK_BUTTON_WIDTH,
            constants.BACK_BUTTON_HEIGHT,
            constants.BACK_BUTTON_TEXT,
        )
        return back_button

    def get_re_button(self):
        re_button = ButtonClass(
            constants.LIGHT_GRAY,
            constants.BACK_BUTTON_X,
            constants.BACK_BUTTON_Y,
            constants.BACK_BUTTON_WIDTH,
            constants.BACK_BUTTON_HEIGHT,
            constants.RE_BUTTON_TEXT,
        )
        return re_button

    def get_start_scene_buttons(self):
        start_button = ButtonClass(constants.WHITE, 100, 100, 320, 130, "START")
        option_button = ButtonClass(constants.WHITE, 400, 400, 160, 90, "Options")
        quit_button = ButtonClass(constants.WHITE, 100, 400, 200, 90, "Quit Game")
        return start_button, option_button, quit_button

    def get_options_scene_buttons(self):
        about_button = ButtonClass(
            constants.LIGHT_GRAY,
            self._button_middle_position - 230,
            constants.MIDDLE_Y,
            self._option_buttons_width,
            self._option_buttons_height,
            "About",
        )
        sound_button = ButtonClass(
            constants.LIGHT_BLUE,
            self._button_middle_position,
            constants.MIDDLE_Y,
            self._big_button_width,
            self._option_buttons_height,
            "Sound: On/Off",
        )
        credits_button = ButtonClass(
            constants.GREEN,
            self._button_middle_position + 350,
            constants.MIDDLE_Y,
            self._option_buttons_width,
            self._option_buttons_height,
            "Credits",
        )
        back_button = self.get_back_button()
        return about_button, sound_button, credits_button, back_button


class TextClass:
    def sentence_generate(
        self, surface, text, position, font, color=pygame.Color(constants.BLACK)
    ):
        words = [word.split(" ") for word in text.splitlines()]  # this is a 2d array
        space = font.size(" ")[0]  # this is the space
        max_width, max_height = surface.get_size()
        x_pos, y_pos = position
        for line in words:
            for word in line:
                word_group = font.render(word, 0, color)
                word_width, word_height = word_group.get_size()
                if x_pos + word_width >= max_width:
                    x_pos = position[0]  # reset the x position
                    y_pos += word_height  # move on to the next row
                surface.blit(word_group, (x_pos, y_pos))
                x_pos += word_width + space
            x_pos = position[0]  # reset the x position
            y_pos += word_height  # move on to the next row


class SoundOnOff:
    def __init__(self):
        self._sound_paused = False

    def toggle_music(self):
        if self._sound_paused:
            pygame.mixer.music.unpause()
            self._sound_paused = False
        else:
            pygame.mixer.music.pause()
            self._sound_paused = True
        return self._sound_paused
