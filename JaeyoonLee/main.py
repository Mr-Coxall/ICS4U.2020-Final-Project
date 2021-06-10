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


def splashScreen():
    start_ticks = pygame.time.get_ticks()

    # background image
    backgroundImageBlit("images\\virusSimulator_splash.png")

    # splash screen title
    titleText(60, adjustment=0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        displayUpdate()

        count = (pygame.time.get_ticks() - start_ticks) / 1000
        if count > constants.SPLASH_TIME:  # break after 3 seconds
            break


def menuScreen():
    # background image
    backgroundImageBlit("images\\virusSimulator_mainMemu.png")

    # main menu screen title
    titleText(100)

    buttonText = ["Start", "Option", "Help", "Quit"]
    buttons = [
        Button(
            constants.CENTER_X - 100,
            constants.CENTER_Y + (60 * index),
            200,
            50,
            buttonText[index],
        )
        for index in range(len(buttonText))
    ]

    while True:
        buttonActive = [False for _ in range(4)]
        clicked = False
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                for idx in range(4):
                    buttonActive[idx] = checkButtonClick(buttons[idx])
                    if buttonActive[idx]:
                        # buttonSound.play()
                        clicked = True
                if buttonActive[3]:
                    quit()

        for button in buttons:
            button.draw(screen)

        # button active
        if clicked:
            if buttonActive[0]:
                simulateScreen()
            elif buttonActive[1]:
                optionScreen()
            elif buttonActive[2]:
                helpScreen()
            backgroundImageBlit("images\\virusSimulator_mainMemu.png")
            titleText(100)

        displayUpdate()


def optionScreen():
    # background image
    backgroundImageBlit("images\\virusSimulator_options.png")

    backButton = Button(10, 10, 150, 50, "Back")
    backActive = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                backActive = checkButtonClick(backButton)

        backButton.draw(screen)

        # Setting text
        displayText("Setting", 50, (20, 100))
        displayText("Sound:", 40, (40, 200))
        for idx in range(len(constants.SETTING_TEXTS)):
            displayText(constants.SETTING_TEXTS[idx], 40, (40, 320 + (140 * idx)))

        # Variable text
        displayText("Variables", 50, (constants.CENTER_X + 20, 100))
        displayText("Covid mode", 40, (constants.WIDTH - 250, 120))
        for idx in range(len(constants.VARIABLE_TEXTS)):
            displayText(
                constants.VARIABLE_TEXTS[idx],
                40,
                (constants.CENTER_X + 40, (2 + idx) * 100),
            )

        drawLine((10, 140), (210, 140))
        drawLine((constants.CENTER_X + 10, 140), (constants.CENTER_X + 210, 140))
        drawLine((constants.CENTER_X, 150), (constants.CENTER_X, constants.HEIGHT - 50))

        if backActive:
            # buttonSound.play()
            break

        displayUpdate()


def helpScreen():
    # background image
    backgroundImageBlit("images\\virusSimulator_options.png")

    # help screen title
    titleText(80, title="About Virus Simulator", adjustment=250)

    backButton = Button(10, 10, 150, 50, "Back")
    backActive = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                backActive = checkButtonClick(backButton)

        backButton.draw(screen)

        for idx in range(len(constants.HELPS)):
            displayText(
                constants.HELPS[idx],
                48,
                (constants.CENTER_X, 300 + (72 * idx)),
                centre=True,
            )
        displayText(
            "Create by Jay Lee",
            48,
            (constants.CENTER_X, constants.HEIGHT - 48),
            centre=True,
        )

        if backActive:
            # buttonSound.play()
            break

        displayUpdate()


def simulateScreen():
    manager = Manager()

    optionBox = Button(550, 300, 300, 200, "", colour=constants.BLACK)
    settingButton = Button(600, 360, 200, 32, "Settings")
    quitButton = Button(600, 408, 200, 32, "Quit")
    optionActive = False
    quitGame = False

    imageNames = ["pause", "play", "fast"]
    timeImages = loadImages(imageNames)

    speed = 1

    while True:
        screen.fill(constants.GREY)

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    if not optionActive:
                        speed = 0
                        # pygame.mixer.music.pause()
                    else:
                        speed = 1
                        # pygame.mixer.music.unpause()
                    manager.setSpeed(speed)
                    optionActive = not optionActive
            elif event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if optionActive:
                    if checkButtonClick(settingButton):
                        # buttonSound.play()
                        optionScreen()
                    quitGame = checkButtonClick(quitButton)

                else:
                    for idx in range(3):
                        image = timeImages[idx].get_rect(center=(16 + (32 * idx), 108))
                        if image.collidepoint(mousePosition):
                            if idx == 2 and speed < 8:  # max time speed: x8
                                speed *= idx
                            else:
                                speed = idx
                            manager.setSpeed(speed)

        manager.movePerson(screen)
        manager.checkInfected()
        manager.checkDeath()

        health = manager.getNumberOfHealthPeople()
        infectious = manager.getNumberOfInfectedPeople()
        death = manager.getNumberOfDeadPeople()
        displayText("Healthy: " + str(health), 30, (5, 5), colour=constants.GREEN)
        displayText("Infectious: " + str(infectious), 30, (5, 35), colour=constants.RED)
        displayText("Death: " + str(death), 30, (5, 65), colour=constants.BLACK)

        for index in range(len(timeImages)):
            screen.blit(timeImages[index], (4 + (32 * index), 84))

        if optionActive:
            optionBox.draw(screen)
            settingButton.draw(screen)
            quitButton.draw(screen)

        if quitGame:
            break

        displayUpdate()


def displayText(strText, fontSize, position, colour=constants.WHITE, centre=False):
    font = getFont(fontSize)
    text = font.render(strText, True, colour)
    if centre:
        screen.blit(text, text.get_rect(center=position))
    else:
        screen.blit(text, position)


def quit():
    pygame.quit()
    sys.exit()


def resizeImage(image, newSize):
    return pygame.transform.scale(image, newSize)


def loadImages(imageNames):
    images = []
    for imageName in imageNames:
        path = getFilePath("images\\" + imageName + ".png")
        image = pygame.image.load(path)
        images.append(image)
    return images


def displayUpdate():
    pygame.display.update()
    fps.tick(constants.FPS)


def backgroundImageBlit(strPath):
    path = getFilePath(strPath)
    background = resizeImage(
        pygame.image.load(path), (constants.WIDTH, constants.HEIGHT)
    )
    screen.blit(background, (0, 0))


def titleText(size, title=constants.TITLE, adjustment=100):
    displayText(
        title,
        size,
        (constants.CENTER_X, constants.CENTER_Y - adjustment),
        centre=True,
    )


def getFilePath(filePath):
    return os.path.join(sourceFileDir, filePath)


def getFont(fontSize):
    return pygame.font.SysFont(constants.FONT, fontSize)


def drawLine(startPos, endPos, colour=constants.WHITE, lineWidth=2):
    pygame.draw.line(screen, colour, startPos, endPos, lineWidth)


def checkButtonClick(button):
    return button.getRect().collidepoint(pygame.mouse.get_pos())


if __name__ == "__main__":
    # find current path
    sourceFileDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(sourceFileDir)

    # initialize pygame
    pygame.init()
    pygame.display.set_caption(constants.TITLE)
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    splashScreen()

    # buttonSound = pygame.mixer.Sound(getFilePath("sounds\\button_click_sound.mp3"))
    pygame.mixer.music.load(getFilePath("sounds\\background_music.mp3"))
    pygame.mixer.music.play(-1)

    menuScreen()
