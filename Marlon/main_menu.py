#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the startup class file for "The Long Way Home"

# import statements
import arcade

# import game
from game import longWayGame


class mainMenu(arcade.View):
    # class for splash screen
    def __init__(self):
        # set up splash
        super().__init__()

        self.texture = arcade.load_texture(":resources:assets/logo.png")

    def on_draw(self):
        # draw view
        arcade.start_render()

        # draw sprites
        self.texture.draw_sized(600, 230, 1200, 150)

        # add text
        arcade.draw_text(
            "Use the WASD or Arrow keys to move."
            " Avoid lava & spikes. Get to the end of the levels.",
            600,
            100,
            arcade.color.PURPLE_HEART,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "(Click to continue)",
            600,
            45,
            arcade.color.BLACK,
            font_size=10,
            anchor_x="center",
        )

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # if user presses button start
        game_view = longWayGame()
        game_view.setup(game_view.level)
        self.window.show_view(game_view)
