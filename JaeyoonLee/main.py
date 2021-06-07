#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This program simulates a virus spreading.


import sys

import constants
import pygame
from Manager import Manager


def main():
    pygame.init()
    pygame.display.set_caption("Virus Simulator")
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.MAX_WIDTH, constants.MAX_HEIGHT))

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


def displayText(screen, strText, position, colour):
    font = pygame.font.SysFont("notosanscjkkrblack", constants.FONT_SIZE)
    text = font.render(strText, True, colour)
    screen.blit(text, position)


if __name__ == "__main__":
    main()
