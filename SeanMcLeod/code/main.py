#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the prison escape game

import sys

import pygame


def first_game_scene(screen):
    # create background
    background = pygame.image.load("Game Scene 1.jpg")

    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        # refresh the screen every frame
        pygame.display.update()


def splash_screen(screen):
    # create background
    background = pygame.image.load("Splash.jpg")

    # upload image
    screen.blit(background, (0, 0))

    # update splash screen once
    pygame.display.update()

    # wait 1000ms
    pygame.time.wait(1000)


def start_screen(screen):
    # constants
    rect_x_position = 100
    rect_y_position = 150
    text_size = 100

    # create background
    background = pygame.image.load("StartScreen.jpg")

    # initialize color
    black = (0, 0, 0)
    white = (255, 255, 255)
    # initialize font
    font = pygame.font.Font(None, text_size)
    # this is the text
    text = font.render("START", False, black)

    # Game loop
    running = True
    while running:
        # upload image
        screen.blit(background, (0, 0))
        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        # create button(surface, color, position & dimensions)
        button = pygame.draw.rect(
            screen,
            white,
            [rect_x_position, rect_y_position, text_size * 2.5, text_size],
        )

        # upload text
        screen.blit(text, (rect_x_position + 20, rect_y_position + 20))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if mouse presses button, move to game scene 1
                if button.collidepoint(mouse_position):
                    running = False
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        # refresh the screen every frame
        pygame.display.update()


def main():
    # initialize pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((800, 600))

    splash_screen(screen)
    start_screen(screen)
    first_game_scene(screen)


if __name__ == "__main__":
    main()
