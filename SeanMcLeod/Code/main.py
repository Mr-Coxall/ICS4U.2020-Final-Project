#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the prison escape game

import sys

import constants
import pygame
from button_class import ButtonClass
from check_prisoner_events import CheckPrisonerEvents
from set_up_display import SetUpDisplay


def third_game_scene():
    # create clock
    clock = pygame.time.Clock()

    print("THIRD!!")
    # create background
    background = pygame.image.load("Backgrounds/Game Scene 3.jpg")

    # create object
    my_setup = SetUpDisplay(screen)
    my_prisoner, my_ship = my_setup.set_up_game_scene_three()
    my_prisoner_event = CheckPrisonerEvents()

    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))

        # move prisoner
        (
            key_is_down,
            key_left,
            key_right,
            key_up,
            key_down,
            key_is_up,
        ) = my_prisoner_event.check_events()
        my_prisoner.prisoner_move(
            key_is_down, key_left, key_right, key_up, key_down, key_is_up
        )

        # choose what image the prisoner should be(there are 10 images for animation)
        my_prisoner.prisoner_animation()
        # flip prisoner
        my_prisoner.prisoner_flip()
        # keep prisoner inside of screen
        my_prisoner.keep_inside_screen()
        # increase prisoner size
        my_prisoner.modify_sprite_size(constants.DOUBLE_SIZE)

        # upload sprites
        my_prisoner.sprite_upload()
        my_ship.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(constants.CLOCK_TICK)


def second_game_scene():
    clock = pygame.time.Clock()
    chest_open = False
    door_open = False
    key_appear = True
    shadow_appear = False

    print("welcome!")
    # create background
    background = pygame.image.load("Backgrounds/Game Scene 2.png")
    # upload image
    chest_opened = pygame.image.load("Sprites/chest-open.png")

    # set up objects
    my_setup = SetUpDisplay(screen)
    (
        my_prisoner,
        my_door,
        my_cell_map,
        my_chest,
        my_key,
        my_shadow,
    ) = my_setup.set_up_game_scene_two()

    # get ready to check prisoner events
    my_prisoner_event = CheckPrisonerEvents()

    # increase chest size
    my_chest.modify_sprite_size(constants.DOUBLE_SIZE)

    running = True
    while running:

        # upload image
        screen.blit(background, (0, 0))

        # get rect
        prisoner_rect = my_prisoner.get_rect()
        door_rect = my_door.get_rect()
        chest_rect = my_chest.get_rect()
        key_rect = my_key.get_rect()

        # build map
        my_cell_map.build_map(prisoner_rect)

        # move prisoner
        (
            key_is_down,
            key_left,
            key_right,
            key_up,
            key_down,
            key_is_up,
        ) = my_prisoner_event.check_events()
        my_prisoner.prisoner_move(
            key_is_down, key_left, key_right, key_up, key_down, key_is_up
        )

        # prisoner animation
        my_prisoner.prisoner_animation()
        # flip prisoner
        my_prisoner.prisoner_flip()
        # choose what image the prisoner should be(there are 10 images for animation)
        my_prisoner.keep_inside_screen()
        # upload prisoner image
        my_prisoner.sprite_upload()

        if my_chest.check_collision(chest_rect, prisoner_rect):
            chest_open = True
            my_chest.set_sprite(chest_opened)
            my_chest.modify_sprite_size(constants.DOUBLE_SIZE)

        if chest_open:
            if key_appear:
                my_key.sprite_upload()
            if my_prisoner.check_collision(prisoner_rect, key_rect):
                # chest_open = False
                door_open = True
                key_appear = False
                shadow_appear = True

        if shadow_appear:
            # upload shadows
            my_shadow.upload()
        # collision detection
        my_shadow.attack(prisoner_rect)

        # collision detection
        if my_door.check_collision(door_rect, prisoner_rect):
            if door_open:
                running = False
            else:
                print("Cant open!!")

        # upload sprites
        my_chest.sprite_upload()
        my_door.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(constants.CLOCK_TICK)


def first_game_scene():
    # create clock
    clock = pygame.time.Clock()

    # create background
    background = pygame.image.load("Backgrounds/Game Scene 1.png")

    # create objects
    my_setup = SetUpDisplay(screen)
    (
        my_prisoner,
        my_golem,
        my_golem_two,
        my_dragon,
        my_cell_map,
        my_door,
    ) = my_setup.set_up_game_scene_one()

    # check prisoner event
    my_check_event = CheckPrisonerEvents()

    # modify dragon size
    my_dragon.modify_sprite_size(constants.DOUBLE_SIZE)

    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))

        # get rect
        prisoner_rect = my_prisoner.get_rect()
        door_rect = my_door.get_rect()

        # build map
        my_cell_map.build_map(prisoner_rect)

        # get events
        (
            key_is_down,
            key_left,
            key_right,
            key_up,
            key_down,
            key_is_up,
        ) = my_check_event.check_events()
        # move prisoner
        my_prisoner.prisoner_move(
            key_is_down, key_left, key_right, key_up, key_down, key_is_up
        )
        # choose what image the prisoner should be(there are 10 images for animation)
        my_prisoner.prisoner_animation()
        # change sprite size of prisoner
        my_prisoner.modify_sprite_size(constants.DOUBLE_SIZE)
        # flip prisoner
        my_prisoner.prisoner_flip()
        # restrict movement to inside of screen
        my_prisoner.keep_inside_screen()
        # upload prisoner image
        my_prisoner.sprite_upload()

        # move golem one
        my_golem.golem_move()
        # upload golem one
        my_golem.sprite_upload()

        # move golem two
        my_golem_two.golem_move()
        # upload golem two
        my_golem_two.sprite_upload()

        # check collision
        my_dragon.attack(prisoner_rect)
        my_golem.attack(prisoner_rect)
        my_golem_two.attack(prisoner_rect)
        # when prisoner gets to the door, end loop and move scene
        if my_door.check_collision(door_rect, prisoner_rect):
            running = False

        # upload dragon and door
        my_dragon.sprite_upload()
        my_door.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(10)


def splash_screen():
    # create background
    background = pygame.image.load("Backgrounds/Splash.jpg")

    # upload image
    screen.blit(background, (0, 0))

    # update splash screen once
    pygame.display.update()

    # wait 1000ms
    pygame.time.wait(constants.WAIT)


def start_screen():
    button_x = 100
    button_y = 100
    button_width = 320
    button_height = 130
    text_size = 90
    outline = 5

    # create background
    background = pygame.image.load("Backgrounds/StartScreen.jpg")

    # create object
    my_button = ButtonClass(
        constants.WHITE, button_x, button_y, button_width, button_height, "START"
    )

    # Game loop
    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))

        # create button
        my_button.draw_button(screen, text_size, outline)

        for event in pygame.event.get():
            # get mouse position
            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                if my_button.is_over(mouse_position):
                    my_button.color = constants.BLACK
                else:
                    my_button.color = constants.WHITE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if my_button.is_over(mouse_position):
                    running = False
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        # refresh the screen every frame
        pygame.display.update()


if __name__ == "__main__":
    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    splash_screen()
    start_screen()
    first_game_scene()
    second_game_scene()
    third_game_scene()
