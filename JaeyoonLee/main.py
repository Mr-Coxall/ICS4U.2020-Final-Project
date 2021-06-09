#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This program simulates a virus spreading.


import os
import sys

import constants
import pygame
from Button import Button
from Manager import Manager


def splashScreen(fps, screen):
    start_ticks = pygame.time.get_ticks()
    backgroundFilePath = os.path.join(
        sourceFileDir, "images\\virusSimulator_splash.png"
    )

    # background image
    background = resizeImage(
        pygame.image.load(backgroundFilePath),
        (constants.MAX_WIDTH, constants.MAX_HEIGHT),
    )
    screen.blit(background, (0, 0))

    # splash screen title
    displayText(
        screen,
        "Splash Screen",
        60,
        (constants.CENTER_X, constants.CENTER_Y),
        constants.WHITE,
        centre=True,
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps.tick(constants.FPS)

        count = (pygame.time.get_ticks() - start_ticks) / 1000
        if count > constants.SPLASH_TIME:  # break after 3 seconds
            break


def menuScreen(fps, screen):
    backgroundFilePath = os.path.join(
        sourceFileDir, "images\\virusSimulator_mainMemu.png"
    )

    buttons = []
    buttonText = ["Start", "Option", "Help", "Quit"]
    for index in range(4):
        buttons.append(
            Button(
                constants.CENTER_X - 100,
                constants.CENTER_Y + (60 * index),
                200,
                50,
                constants.WHITE,
                buttonText[index],
                constants.RED,
            )
        )

    # background image
    background = resizeImage(
        pygame.image.load(backgroundFilePath),
        (constants.MAX_WIDTH, constants.MAX_HEIGHT),
    )
    screen.blit(background, (0, 0))

    # main menu screen title
    displayText(
        screen,
        "Virus Simulator",
        100,
        (constants.CENTER_X, constants.CENTER_Y - 100),
        constants.WHITE,
        centre=True,
    )

    while True:
        buttonActive = [False for _ in range(4)]
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for idx in range(4):
                    button = buttons[idx].getRect()
                    buttonActive[idx] = button.collidepoint(mousePosition)
                if buttonActive[3]:
                    pygame.quit()
                    sys.exit()

        for button in buttons:
            button.draw(screen)

        # button active
        if buttonActive[0]:
            simulateScreen(fps, screen)
        elif buttonActive[1]:
            print("Option")
        elif buttonActive[2]:
            print("Help")

        pygame.display.update()
        fps.tick(constants.FPS)


def simulateScreen(fps, screen):
    manager = Manager()

    timeImages = []
    imageNames = ["pause", "play", "fast"]
    for index in range(len(imageNames)):
        path = os.path.join(sourceFileDir, "images\\" + imageNames[index] + ".png")
        image = pygame.image.load(path)
        timeImages.append(image)

    speed = 1

    while True:
        screen.fill(constants.GREY)

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for idx in range(len(timeImages)):
                    image = timeImages[idx].get_rect(center=(17 + (32 * idx), 108))
                    if image.collidepoint(mousePosition):
                        if idx == 0:  # pause
                            speed = 0
                        elif idx == 1:  # play
                            speed = 1
                        elif idx == 2 and speed < 8:  # max time speed: x8
                            speed *= 2
                        manager.setSpeed(speed)

        manager.movePerson(screen)
        manager.checkInfected()

        health = manager.getNumberOfHealthPeople()
        infectious = manager.getNumberOfInfectedPeople()
        death = manager.getNumberOfDeadPeople()
        displayText(screen, "Healthy: " + str(health), 30, (5, 5), constants.GREEN)
        displayText(
            screen, "Infectious: " + str(infectious), 30, (5, 35), constants.RED
        )
        displayText(screen, "Death: " + str(death), 30, (5, 65), constants.BLACK)

        for index in range(len(timeImages)):
            screen.blit(timeImages[index], (5 + (32 * index), 84))

        pygame.display.update()
        fps.tick(constants.FPS)


def main():
    pygame.init()
    pygame.display.set_caption("Virus Simulator")
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.MAX_WIDTH, constants.MAX_HEIGHT))

    splashScreen(fps, screen)
    menuScreen(fps, screen)


def displayText(screen, strText, fontSize, position, colour, centre=False):
    font = getFont(fontSize)
    text = font.render(strText, True, colour)
    if centre:
        screen.blit(text, text.get_rect(center=position))
    else:
        screen.blit(text, position)


def resizeImage(image, newSize):
    image = pygame.transform.scale(image, newSize)
    return image


def getFont(fontSize):
    return pygame.font.SysFont("notosanscjkkrblack", fontSize)


if __name__ == "__main__":
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(sourceFileDir)
    main()
