#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the game_over class file for "The Long Way Home"

# import statements
import arcade


class game_over(arcade.View):
    # class for splash screen
    def __init__(self):
        # set up splash
        super().__init__()

        self.texture = arcade.load_texture(":resources:assets/game_over.png")

    def on_show(self):
        # set background
        arcade.set_background_color(arcade.csscolor.WHITE)

    def on_draw(self):
        # draw view
        arcade.start_render()

        # draw sprites
        self.texture.draw_sized(600, 230, 1200, 150)

        # add text
        arcade.draw_text(
            "The game is finished.",
            600,
            100,
            arcade.color.PURPLE_HEART,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Thanks for playing!",
            600,
            45,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
