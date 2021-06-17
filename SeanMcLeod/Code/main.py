import sys

import constants
import pygame
from ButtonClass import ButtonClass
from CheckPrisonerEvents import CheckPrisonerEvents
from PrisonerClass import PrisonerClass

# from Maps import Maps


def first_game_scene():
    prisoner_x = 700
    prisoner_y = 450
    clock = pygame.time.Clock()

    # create background
    background = pygame.image.load("Backgrounds/Game Scene 1.png")

    # create sprites
    prisoner = pygame.image.load("Sprites/prisoners/prisoner.png")
    # tile = pygame.image.load("Sprites/cell.png")

    # objects
    my_prisoner = PrisonerClass(
        prisoner,
        prisoner_x,
        prisoner_y,
        constants.PRISONER_X_SPEED,
        constants.PRISONER_Y_SPEED,
        screen,
    )
    # my_cell_map = Maps(tile, 60, 50, screen, 1)
    my_check_event = CheckPrisonerEvents()

    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))

        # get rect
        # prisoner_rect = my_prisoner.get_rect()

        # build map
        # my_cell_map.build_map(prisoner_rect)

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
        my_prisoner.modify_sprite_size(2)
        # flip prisoner
        my_prisoner.prisoner_flip()
        # upload prisoner image
        my_prisoner.sprite_upload()

        # refresh the screen every frame
        pygame.display.update()
        # slow down to see the animations move
        clock.tick(constants.CLOCK_TICK)


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
