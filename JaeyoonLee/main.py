#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This program simulates a virus spreading.


import sys

import constants
import pygame
from Manager import Manager


def splashScreen(fps, screen):
    start_ticks = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        background = pygame.image.load(
            "C:\\JaeyoonLee\\ICS4U\\FinalProject\\ICS4U.2020-Final-Project\\JaeyoonLee\\images\\virusSimulator_mainMemu.png"
        )
        background = pygame.transform.scale(
            background, (constants.MAX_WIDTH, constants.MAX_HEIGHT)
        )
        screen.blit(background, (0, 0))
        font = pygame.font.SysFont("notosanscjkkrblack", 60)
        text = font.render("Splash Screen", True, constants.WHITE)
        centerX = (constants.MAX_WIDTH - text.get_rect().width) // 2
        centerY = (constants.MAX_HEIGHT - text.get_rect().height) // 2
        screen.blit(text, (centerX, centerY))
        pygame.display.update()
        fps.tick(constants.FPS)
        count = (pygame.time.get_ticks() - start_ticks) / 1000
        if count > constants.SPLASH_TIME:  # break after 3 seconds
            break


def simulateScreen(fps, screen):
    manager = Manager()

    while True:
        screen.fill(constants.GREY)

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        manager.movePerson(screen)
        manager.checkInfected()

        displayText(
            screen,
            "Healthy: " + str(manager.getNumberOfHealthPeople()),
            (5, 5),
            constants.GREEN,
        )
        displayText(
            screen,
            "Infectious: " + str(manager.getNumberOfInfectedPeople()),
            (5, 35),
            constants.RED,
        )
        displayText(
            screen,
            "Death: " + str(manager.getNumberOfDeadPeople()),
            (5, 65),
            constants.BLACK,
        )
        pygame.display.update()
        fps.tick(constants.FPS)


def main():
    pygame.init()
    pygame.display.set_caption("Virus Simulator")
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.MAX_WIDTH, constants.MAX_HEIGHT))

    splashScreen(fps, screen)
    simulateScreen(fps, screen)


def displayText(screen, strText, position, colour):
    font = pygame.font.SysFont("notosanscjkkrblack", constants.FONT_SIZE)
    text = font.render(strText, True, colour)
    screen.blit(text, position)


if __name__ == "__main__":
    main()
