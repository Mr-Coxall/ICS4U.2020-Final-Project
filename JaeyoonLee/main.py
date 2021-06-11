#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This program simulates a virus spreading.


import os
import sys

import constants
import pygame
from Button import Button, SelectionBox
from Manager import Manager


def splashScreen():
    # background image
    backgroundImageBlit(constants.SPLASH_IMG)

    # splash screen title
    titleText(60, adjustment=0)

    pygame.display.update()

    pygame.time.wait(1000)


def menuScreen():
    # background image
    backgroundImageBlit(constants.MENU_IMG)

    # main menu screen title
    titleText(100)

    buttonText = constants.MENU_TEXTS
    buttons = [
        Button(600, 400 + (60 * index), 200, 50, buttonText[index])
        for index in range(len(buttonText))
    ]

    while True:
        buttonActive = [False for _ in range(4)]
        clicked = False

        # event check
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.MOUSEBUTTONUP:
                for idx in range(4):
                    buttonActive[idx] = checkButtonClick(buttons[idx])
                    if buttonActive[idx]:
                        clicked = True
                if buttonActive[3]:
                    pygame.quit()
                    sys.exit()

        # button active
        if clicked:
            # buttonSound.play()
            if buttonActive[0]:
                simulateScreen()
            elif buttonActive[1]:
                optionScreen()
            elif buttonActive[2]:
                helpScreen()
            backgroundImageBlit(constants.MENU_IMG)
            titleText(100)

        for button in buttons:
            button.draw(screen)

        displayUpdate()


def optionScreen():
    # background image
    backgroundImageBlit(constants.OPTION_IMG)

    backButton, backActive = genBackButton()

    colourOptions = constants.PEOPLE_COLOURS
    colourTexts = constants.PEOPLE_OPTIONS

    colourSettings = [
        SelectionBox(
            450,
            320 + (140 * idx),
            200,
            40,
            constants.OPTION_BOX,
            colourTexts[idx],
            colourOptions[idx],
        )
        for idx in range(3)
    ]

    while not backActive:
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.MOUSEBUTTONUP:
                backActive = checkButtonClick(backButton)
                for colourSetting in colourSettings:
                    colourSetting.update()

        backButton.draw(screen)
        for colourSetting in colourSettings:
            colourSetting.draw(screen)

        # set texts and lines on screen
        setTextAndLine()

        displayUpdate()

    # buttonSound.play()


def helpScreen():
    # background image
    backgroundImageBlit(constants.OPTION_IMG)

    backButton, backActive = genBackButton()

    # help screen title
    titleText(80, title="About Virus Simulator", adjustment=250)

    while not backActive:
        for event in pygame.event.get():
            checkQuit(event)
            backActive = checkBackButton(event, backButton)

        backButton.draw(screen)

        for idx in range(len(constants.HELPS)):
            displayText(constants.HELPS[idx], 48, (700, 300 + (72 * idx)), centre=True)
        displayText("Create by Jay Lee", 48, (700, 750), centre=True)

        displayUpdate()
    # buttonSound.play()


def simulateScreen():
    # Pop up setting
    optionBox = Button(550, 300, 300, 200, "", colour=constants.BLACK)
    settingButton = Button(600, 360, 200, 32, "Settings")
    quitButton = Button(600, 408, 200, 32, "Quit")
    optionActive = False
    quitGame = False

    timeImages = loadImages(constants.TIME_TEXTS)

    speed = 1

    while not quitGame:
        screen.fill(constants.GREY)

        # event check
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                manager.setSpeed(1 if optionActive else 0)
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
                            speed = (speed * idx) if idx == 2 and speed < 8 else idx
                            manager.setSpeed(speed)  # max time speed: x8

        manager.movePerson(screen)
        manager.checkInfected()
        manager.checkDeath()

        displayInfo()

        for index in range(len(timeImages)):
            screen.blit(timeImages[index], (4 + (32 * index), 84))

        if optionActive:
            optionBox.draw(screen)
            settingButton.draw(screen)
            quitButton.draw(screen)

        displayUpdate()


def displayText(strText, fontSize, position, colour=constants.WHITE, centre=False):
    font = getFont(fontSize)
    text = font.render(strText, True, colour)
    if centre:
        screen.blit(text, text.get_rect(center=position))
    else:
        screen.blit(text, position)


def checkQuit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def checkBackButton(event, backButton):
    if event.type == pygame.MOUSEBUTTONUP:
        return checkButtonClick(backButton)
    else:
        return False


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


def setTextAndLine():
    # Setting text
    displayText("Setting", 50, (20, 100))
    displayText("Sound:", 40, (40, 200))
    for idx in range(len(constants.SETTING_TEXTS)):
        displayText(constants.SETTING_TEXTS[idx], 40, (40, 320 + (140 * idx)))

    # Variable text
    displayText("Variables", 50, (720, 100))
    displayText("Covid mode", 40, (1150, 120))
    for idx in range(len(constants.VARIABLE_TEXTS)):
        displayText(constants.VARIABLE_TEXTS[idx], 40, (740, (2 + idx) * 100))

    drawLine((10, 140), (210, 140))
    drawLine((710, 140), (910, 140))
    drawLine((700, 150), (700, 750))


def genBackButton():
    return Button(10, 10, 150, 50, "Back"), False


def displayInfo():
    health = manager.getNumberOfHealthPeople()
    infectious = manager.getNumberOfInfectedPeople()
    death = manager.getNumberOfDeadPeople()
    displayText("Healthy: " + str(health), 30, (5, 5), colour=constants.GREEN)
    displayText("Infectious: " + str(infectious), 30, (5, 35), colour=constants.RED)
    displayText("Death: " + str(death), 30, (5, 65), colour=constants.BLACK)


def drawSlider(startPos, length, defaultValue, width=2):
    endPos = (list(startPos)[0], list(startPos)[1] + length)
    pointPos = (list(startPos)[0], list(startPos)[1] + defaultValue)
    drawLine(startPos, endPos, width=width)
    pygame.draw.circle(screen, constants.WHITE, pointPos, 10)
    return


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

    manager = Manager()

    # buttonSound = pygame.mixer.Sound(getFilePath("sounds\\button_click_sound.mp3"))
    pygame.mixer.music.load(getFilePath("sounds\\background_music.mp3"))
    pygame.mixer.music.play(-1)

    menuScreen()
