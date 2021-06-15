#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on June 2021
# This is the game class file for "The Long Way Home"

# import statements
import arcade

# import constants
import constants


class longWayGame(arcade.Window):
    # main game class
    def __init__(self):
        # initialise variables (constructor)

        # Call the parent class and set up the window
        super().__init__(
            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE
        )

        # create list for sprites
        self.wall_list = None
        self.sign_list = None
        self.player_list = None
        self.coin_list = None
        self.death_list = None
        self.bg_list = None
        self.fg_list = None

        # create player sprite variable
        self.player_sprite = None

        # create physics engine
        self.physics_eng = None

        # keep track of scrolling
        self.view_left = 0
        self.view_bottom = 0

        # score
        self.score = 0

        # right edge of map
        self.end_of_map = 0

        # Level
        self.level = 1

        # load sounds
        self.coin_sound = arcade.load_sound(":resources:assets/coin.wav")
        self.jump_sound = arcade.load_sound(":resources:assets/jump.wav")
        self.death_sound = arcade.load_sound(":resources:assets/lava-death.wav")

        # set background colour of window
        arcade.set_background_color(constants.BG_COLOUR)

    def setup(self, level):
        # function for gameplay

        # keep track of scrolling
        self.view_left = 0
        self.view_bottom = 0

        # score
        self.score = 0

        # create sprite lists
        self.player_list = arcade.SpriteList()
        self.sign_list = arcade.SpriteList()
        self.death_list = arcade.SpriteList()
        self.bg_list = arcade.SpriteList()
        self.fg_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # set player sprite
        player_source = ":resources:assets/llama.gif"
        self.player_sprite = arcade.Sprite(player_source, constants.PLAYER_SCALING)
        self.player_sprite.center_x = constants.START_X
        self.player_sprite.center_y = constants.START_Y
        self.player_list.append(self.player_sprite)

        # platform layer name
        platform_name = "Platform"
        # coin layer name
        coin_name = "coins"
        # background layer name
        bg_name = "Background"
        # foreground layer name
        fg_name = "Foreground"
        # layer name
        death_name = "death"

        # add Tiled map
        map_name = f":resources:Assets/platformer{level}.tmx"

        # read tiled map
        current_level = arcade.tilemap.read_tmx(map_name)

        # calculate right edge of map in px
        self.end_of_map = current_level.map_size.width * constants.GRID_PX

        # set platforms
        self.wall_list = arcade.tilemap.process_layer(
            map_object=current_level,
            layer_name=platform_name,
            scaling=constants.TILE_SCALING,
            use_spatial_hash=True,
        )

        # set coins
        self.coin_list = arcade.tilemap.process_layer(
            current_level,
            coin_name,
            constants.TILE_SCALING,
            use_spatial_hash=True,
        )

        # set death tiles
        self.death_list = arcade.tilemap.process_layer(
            current_level,
            death_name,
            constants.TILE_SCALING,
            use_spatial_hash=True,
        )

        # set background tiles
        self.bg_list = arcade.tilemap.process_layer(
            current_level, bg_name, constants.TILE_SCALING
        )

        # set foreground tiles
        self.fg_list = arcade.tilemap.process_layer(
            current_level, fg_name, constants.TILE_SCALING
        )

        # set sign sprite
        sign_source = ":resources:assets/sign.png"
        self.sign_sprite = arcade.Sprite(sign_source, constants.PLAYER_SCALING)
        self.sign_sprite.center_x = 1150
        self.sign_sprite.center_y = 120
        self.sign_list.append(self.sign_sprite)

        # use arcade class physics engine to simulate gravity and physics
        self.physics_eng = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.wall_list, constants.GRAVITY
        )

    def on_draw(self):
        # render screen

        arcade.start_render()

        # draw sprites
        self.wall_list.draw()
        self.coin_list.draw()
        self.death_list.draw()
        self.player_list.draw()
        self.sign_list.draw()
        self.bg_list.draw()
        self.fg_list.draw()

        # draw score text on screen
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 25, 290, constants.TXT_COLOUR, 18)

    def on_key_press(self, key, modifiers):
        # called whenever key is pressed

        # if statement for arrow key/WASD presses
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_eng.can_jump():
                self.player_sprite.change_y = constants.PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        # called whenever key is released

        # if statement for arrow key/WASD presses
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        # contains movement and game logic

        # move player using physics engine
        self.physics_eng.update()

        # coin collision check
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )

        # loop for coin removal
        for coin in coin_hit_list:
            # remove coin
            coin.remove_from_sprite_lists()
            # play coin get sound
            arcade.play_sound(self.coin_sound)
            # add 1 to score
            self.score += 1

        # check if user fell off map
        if self.player_sprite.center_y < -10:
            self.player_sprite.center_x = constants.START_X
            self.player_sprite.center_y = constants.START_Y

            # play death sound
            arcade.play_sound(self.death_sound)

        # check for collision with lava
        if arcade.check_for_collision_with_list(self.player_sprite, self.death_list):
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0
            self.player_sprite.center_x = constants.START_X
            self.player_sprite.center_y = constants.START_Y

            # play death sound
            arcade.play_sound(self.death_sound)

        # check if user got to end of level
        if self.player_sprite.center_x >= self.end_of_map:
            # advance to next level
            self.level += 1

            # load next level
            self.setup(self.level)
