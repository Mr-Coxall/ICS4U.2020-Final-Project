#!/usr/bin/env python3

# Created by Sean McLeod
# Created on June 2021
# This is the prison escape game

import pygame


def main():
    # initialize pygame
    pygame.init()
    # create screen
    screen = pygame.display.set_mode((800, 600))
    # create image
    splash_screen = pygame.image.load('Splash.jpg')
    # Game loop
    running = True
    while running:
        screen.blit(splash_screen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


if __name__ == '__main__':
    main()
