#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the startup class file for "The Long Way Home"

# import statements
import arcade

# import game
from main_menu import mainMenu


class splashScreen(arcade.Sprite):
    # class for startup screen

    def __init__(self):

        # set up parent class
        super().__init__()

        # variables
        self.cur_texture = 0

        # load textures
        main_path = ":resources:Assets/Splash-LOGO-"

        self.splash_textures = []
        for sprite in range(8):
            self.texture = arcade.load_texture(f"{main_path}{sprite}.png")
            self.splash_textures.append(self.texture)

    def update_animation(self, delta_time: float = 1 / 60):
        # updates animation

        self.cur_texture += 1
        if self.cur_texture > 7 * 5:
            self.cur_texture = 0
        frame = self.cur_texture // 5
        self.texture = self.splash_textures[frame]


class startView(arcade.View):
    # class for splash screen
    def __init__(self):
        # set up splash
        super().__init__()

        self.splash_list = None

    def setup(self):
        self.splash_list = arcade.SpriteList()

        self.splash = splashScreen()
        self.splash.center_x = 600
        self.splash.center_y = 200
        self.splash_list.append(self.splash)

    def on_show(self):
        # set background
        arcade.set_background_color(arcade.csscolor.WHITE)

    def on_draw(self):
        # draw view
        arcade.start_render()

        # draw sprites
        self.splash_list.draw()

        # add text
        arcade.draw_text(
            "MP Productions™",
            600,
            75,
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

    def on_update(self, delta_time):
        # update animation

        # updates splash screen animation
        self.splash_list.update_animation()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # if user presses button start
        game_view = mainMenu()
        self.window.show_view(game_view)
