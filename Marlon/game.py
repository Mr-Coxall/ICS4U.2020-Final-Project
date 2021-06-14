#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the game class file for "The Long Way Home"

# import statements
import arcade
import constants


class longWayGame(arcade.Window):
    # main game class
    def __init__(self):
        # initialise variables (constructor)

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # create list for sprites
        self.wall_list = None
        self.player_list = None
        self.coin_list = None
        self.enemy_list = None

        # create player sprite variable
        self.player_sprite = None

        # create physics engine
        self.physics_eng = None

        # set background colour of window
        arcade.set_background_color(constants.BG_COLOUR)

    def setup(self):
        # function for gameplay

        # keep track of scrolling
        self.view_left = 0
        self.view_bottom = 0

        # create sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        # set player sprite
        player_source = ":resources:assets/Lava.gif"
        self.player_sprite = arcade.Sprite(player_source, constants.PLAYER_SCALING)
        self.player_sprite.center_x = 32
        self.player_sprite.center_y = 104
        self.player_list.append(self.player_sprite)

        # add Tiled map
        my_level_one = ":resources:assets/platformer.tmx"
        # layer name
        platform_name = 'Platform'
        # layer name
        coin_name = 'coins'

        # read tiled map
        level_one = arcade.tilemap.read_tmx(my_level_one)

        # set platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=
                                                      level_one,
                                                       layer_name =
                                                       platform_name,
                                                       scaling =
                                                       constants.TILE_SCALING,
                                                       use_spatial_hash=True)

        # set coins
        self.coin_list = arcade.tilemap.process_layer(level_one, coin_name,
                                                      constants.TILE_SCALING)

        # use arcade class physics engine to simulate gravity and physics
        self.physics_eng = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                          self.wall_list,
                                                          constants.GRAVITY)

    def on_draw(self):
        # render screen

        arcade.start_render()

        # draw sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        # called whenever key is pressed

        # if statement for arrow key/WASD presses
        if key in [arcade.key.UP, arcade.key.W]:
            if self.physics_eng.can_jump():
                self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # called whenever key is released

        # if statement for arrow key/WASD presses
        if key in [arcade.key.LEFT, arcade.key.A]:
            self.player_sprite.change_x = 0
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        # contains movement and game logic

        # move player using physics engine
        self.physics_eng.update()

        # scrolling -------------------------------------------------
        # check if viewport needs to be changed
        changed = False

        # Scroll left
        left_boundary = self.view_left + constants.LEFT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + constants.SCREEN_WIDTH\
                         - constants.RIGHT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + constants.SCREEN_HEIGHT \
                       - constants.TOP_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + constants.BOTTOM_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # if statement for if change is detected
        if changed:
            # scroll to int (pixel) on screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # perform scroll, call arcade class
            arcade.set_viewport(self.view_left,
                                constants.SCREEN_WIDTH
                                + self.view_left,
                                self.view_bottom,
                                constants.SCREEN_HEIGHT
                                + self.view_bottom)
