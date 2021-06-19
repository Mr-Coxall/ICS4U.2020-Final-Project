#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the prison escape game

import sys

import constants
import pygame
from bullets import BulletClass
from check_prisoner_events import CheckPrisonerEvents
from game_features import GetModifiedButton, SoundOnOff, TextClass
from pygame import mixer
from set_up_scenes import SetUpScenes


def did_you_win(is_win):
    # font
    main_font = pygame.font.SysFont(constants.FONT_COMIC, constants.TITLE_SIZE)
    if is_win:
        text = "You Win!"
    else:
        text = "You Lose!"
    # text
    main_text = main_font.render(text, False, constants.BLACK)

    # object
    my_button = GetModifiedButton()
    re_button = my_button.get_re_button()

    # Game loop
    running = True
    while running:
        # screen fill
        screen.fill(constants.WHITE)

        # display text
        screen.blit(main_text, (constants.MIDDLE_X - 100, constants.TITLE_Y))

        # create button
        re_button.draw_button(
            screen,
            constants.BACK_BUTTON_TEXT_SIZE,
            constants.FONT_CORBEL,
            constants.BUTTON_OUTLINE,
        )

        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if re_button.is_over(mouse_position):
                    start_screen()

        # refresh the screen every frame
        pygame.display.update()


def credits_page():
    # text
    title_font = pygame.font.SysFont(constants.TITLE_FONT, constants.TITLE_SIZE)
    title_text = title_font.render("Credits", False, constants.BLACK)

    main_font = pygame.font.SysFont(constants.FONT_COMIC, 16)

    # object
    my_button = GetModifiedButton()
    back_button = my_button.get_back_button()
    my_long_text = TextClass()
    set_scene = SetUpScenes(screen)

    # Game loop
    running = True
    while running:
        # upload image
        screen.fill(constants.GREEN)

        # display title
        screen.blit(title_text, (constants.MIDDLE_X - 100, constants.TITLE_Y))
        # display text
        my_long_text.sentence_generate(
            screen, constants.CREDIT_TEXT, (190, 150), main_font
        )

        # draw back_button
        set_scene.draw_back_button(back_button)

        # event handle
        if set_scene.credit_and_about_event(back_button):
            option_page()

        # refresh the screen every frame
        pygame.display.update()


def about_page():
    # text
    title_font = pygame.font.SysFont(constants.TITLE_FONT, constants.TITLE_SIZE)
    title_text = title_font.render("About", False, constants.BLACK)

    main_font = pygame.font.SysFont(constants.FONT_COMIC, 30)

    # object
    my_button = GetModifiedButton()
    back_button = my_button.get_back_button()
    set_scene = SetUpScenes(screen)

    my_long_text = TextClass()

    # Game loop
    running = True
    while running:
        # upload image
        screen.fill(constants.LIGHT_GRAY)

        # display title
        screen.blit(title_text, (constants.MIDDLE_X - 100, constants.TITLE_Y))
        # display text
        my_long_text.sentence_generate(
            screen, constants.ABOUT_TEXT, (100, 200), main_font
        )

        # draw back_button
        set_scene.draw_back_button(back_button)

        # event handle
        if set_scene.credit_and_about_event(back_button):
            option_page()

        # refresh the screen every frame
        pygame.display.update()


def option_page():
    text_size = 50

    # create objects
    my_button = GetModifiedButton()
    (
        about_button,
        sound_button,
        credits_button,
        back_button,
    ) = my_button.get_options_scene_buttons()
    sound_toggle = SoundOnOff()

    # text
    my_font = pygame.font.SysFont(constants.TITLE_FONT, constants.TITLE_SIZE)
    text_surface = my_font.render("Options", False, constants.BLACK)

    # Game loop
    running = True
    while running:
        # upload image
        screen.fill(constants.WHITE)

        # display title
        screen.blit(text_surface, (constants.MIDDLE_X - 120, constants.TITLE_Y))

        # create button
        about_button.draw_button(
            screen, text_size, constants.FONT_CORBEL, constants.BUTTON_OUTLINE
        )
        sound_button.draw_button(
            screen, text_size, constants.FONT_CORBEL, constants.BUTTON_OUTLINE
        )
        credits_button.draw_button(
            screen, text_size, constants.FONT_CORBEL, constants.BUTTON_OUTLINE
        )
        back_button.draw_button(
            screen,
            constants.BACK_BUTTON_TEXT_SIZE,
            constants.FONT_CORBEL,
            constants.BUTTON_OUTLINE,
        )

        for event in pygame.event.get():
            # get mouse position
            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                # change color when mouse is over button
                if about_button.is_over(mouse_position):
                    about_button.color = constants.LIGHT_RED
                else:
                    about_button.color = constants.LIGHT_GRAY
                if sound_button.is_over(mouse_position):
                    sound_button.color = constants.LIGHT_RED
                else:
                    sound_button.color = constants.LIGHT_BLUE
                if credits_button.is_over(mouse_position):
                    credits_button.color = constants.LIGHT_RED
                else:
                    credits_button.color = constants.GREEN
            if event.type == pygame.MOUSEBUTTONDOWN:
                # move to certain page when button clicked
                if about_button.is_over(mouse_position):
                    about_page()
                if credits_button.is_over(mouse_position):
                    credits_page()
                if sound_button.is_over(mouse_position):
                    sound_toggle.toggle_music()
                if back_button.is_over(mouse_position):
                    start_screen()
            if event.type == pygame.QUIT:
                sys.exit()

        # refresh the screen every frame
        pygame.display.update()


def third_game_scene():
    # create clock
    clock = pygame.time.Clock()
    cool_down_counter = constants.BULLET_WAIT
    first_ship_bullets = []
    second_ship_bullets = []

    # create background
    background = pygame.image.load(constants.SCENE_THREE)

    # create object
    my_setup = SetUpScenes(screen)
    (
        my_prisoner,
        my_ship,
        my_ship_two,
        my_door,
    ) = my_setup.set_up_game_scene_three()
    my_prisoner_event = CheckPrisonerEvents()
    my_bullet = BulletClass(screen, constants.BULLET_X_SPEED, constants.BULLET_Y_SPEED)

    running = True
    while running:
        cool_down_counter += 1

        # upload image
        screen.blit(background, (0, 0))

        # get rect
        prisoner_rect = my_prisoner.get_rect()
        door_rect = my_door.get_rect()

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
        # # flip prisoner
        my_prisoner.prisoner_flip()
        # keep prisoner inside of screen
        my_prisoner.keep_inside_screen()
        # increase prisoner size
        my_prisoner.modify_sprite_size(constants.DOUBLE_SIZE)

        # fire a bullet if the counter refreshed
        if cool_down_counter > constants.BULLET_SHOOT_RATE:
            cool_down_counter = 0
            my_bullet.create_bullets(
                first_ship_bullets,
                second_ship_bullets,
                my_ship.get_rect(),
                my_ship_two.get_rect(),
            )

        # draw the bullets
        my_bullet.draw(first_ship_bullets, second_ship_bullets)

        # check bullet events
        did_shoot = my_bullet.handle_bullets(
            first_ship_bullets, second_ship_bullets, prisoner_rect
        )

        # move ship
        my_ship.ship_move()
        my_ship_two.ship_move()

        # check collisions
        if my_ship.attack(prisoner_rect) or did_shoot:
            hit_sound = mixer.Sound(constants.HIT_SOUND)
            hit_sound.play()
            did_you_win(False)
        if my_door.check_collision(door_rect, prisoner_rect):
            did_you_win(True)
        # upload sprites
        my_door.sprite_upload()
        my_prisoner.sprite_upload()
        my_ship.sprite_upload()
        my_ship_two.sprite_upload()

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

    # create background
    background = pygame.image.load(constants.SCENE_TWO)
    # upload image
    chest_opened = pygame.image.load(constants.CHEST_OPEN)

    # set up objects
    my_setup = SetUpScenes(screen)

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
        did_map_collide = my_cell_map.build_map(prisoner_rect)

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
                    key_sound = mixer.Sound(constants.KEY_SOUND)
                    key_sound.play()
                    door_open = True
                    key_appear = False
                    shadow_appear = True

        if shadow_appear:
            # upload shadows
            my_shadow.upload()
        # collision detection
        if my_shadow.attack(prisoner_rect) or did_map_collide:
            electrocute = mixer.Sound(constants.ELECTRIC_SOUND)
            hit_sound = mixer.Sound(constants.HIT_SOUND)
            if did_map_collide:
                electrocute.play()
            else:
                hit_sound.play()
            did_you_win(False)

        # collision detection
        if my_door.check_collision(door_rect, prisoner_rect):
            if door_open:
                third_game_scene()
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
    background = pygame.image.load(constants.SCENE_ONE)

    # create music
    mixer.music.load(constants.GAME_SOUND)
    mixer.music.play(-1)

    # create objects
    my_setup = SetUpScenes(screen)
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
        did_map_collide = my_cell_map.build_map(prisoner_rect)

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
        if (
            my_dragon.attack(prisoner_rect)
            or my_golem.attack(prisoner_rect)
            or my_golem_two.attack(prisoner_rect)
            or did_map_collide
        ):
            hit_sound = mixer.Sound(constants.HIT_SOUND)
            electrocute = mixer.Sound(constants.ELECTRIC_SOUND)
            if did_map_collide:
                electrocute.play()
            else:
                hit_sound.play()
            # player lost
            did_you_win(False)
        # when prisoner gets to the door, end loop and move scene
        if my_door.check_collision(door_rect, prisoner_rect):
            second_game_scene()

        # upload dragon and door
        my_dragon.sprite_upload()
        my_door.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(constants.CLOCK_TICK)


def splash_screen():
    # create background
    background = pygame.image.load(constants.SPLASH_SCREEN)

    # upload image
    screen.blit(background, (0, 0))

    # update splash screen once
    pygame.display.update()

    # wait 1000ms
    pygame.time.wait(constants.WAIT)


def start_screen():
    text_size = 90
    outline = 5

    # create background
    background = pygame.image.load(constants.START_SCREEN)

    # create object
    my_buttons = GetModifiedButton()
    (
        start_button,
        option_button,
        quit_button,
    ) = my_buttons.get_start_scene_buttons()

    # Game loop
    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))

        # create button
        start_button.draw_button(screen, text_size, constants.FONT_COMIC, outline)
        option_button.draw_button(screen, text_size - 50, constants.FONT_COMIC, outline)
        quit_button.draw_button(screen, text_size - 50, constants.FONT_COMIC, outline)

        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if start_button.is_over(mouse_position):
                    start_button.color = constants.YELLOW
                else:
                    start_button.color = constants.WHITE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_over(mouse_position):
                    first_game_scene()
                elif option_button.is_over(mouse_position):
                    option_page()
                elif quit_button.is_over(mouse_position):
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
        # update screen
        pygame.display.update()


if __name__ == "__main__":
    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # create music
    mixer.music.load(constants.START_SOUND)
    mixer.music.play()

    splash_screen()
    start_screen()
    first_game_scene()
    second_game_scene()
    third_game_scene()
