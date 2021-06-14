#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This program simulates a virus spreading.


import constants
import displayFunctions as display
import pygame
from Manager import Manager
from Setting import CheckBox, Slider


def splashScreen():
    # background image
    display.backgroundImageBlit(screen, constants.SPLASH_IMG)

    # splash screen title
    display.titleText(screen, 60, adjustment=0)

    pygame.display.update()

    pygame.time.wait(1000)


def menuScreen():
    # background image
    display.backgroundImageBlit(screen, constants.MENU_IMG)

    # main menu screen title
    display.titleText(screen, 100)

    buttons = display.genMenuButtons()

    while True:
        buttonActive = [False for _ in range(4)]
        clicked = False

        # event check
        for event in pygame.event.get():
            display.checkQuit(event)
            if event.type == pygame.MOUSEBUTTONUP:
                for idx in range(4):
                    buttonActive[idx] = display.checkButtonClick(buttons[idx])
                    if buttonActive[idx]:
                        clicked = True
                if buttonActive[3]:
                    display.checkQuit(event, specific=True)

        # button active
        if clicked:
            buttonSound.play()
            if buttonActive[0]:
                simulateScreen()
            elif buttonActive[1]:
                optionScreen()
            elif buttonActive[2]:
                helpScreen()
            display.backgroundImageBlit(screen, constants.MENU_IMG)
            display.titleText(screen, 100)

        for button in buttons:
            button.draw(screen)

        display.displayUpdate()


def optionScreen(variableAccess=True):
    global variables, colours
    # background image
    display.backgroundImageBlit(screen, constants.OPTION_IMG)

    backButton, backActive = display.genBackButton()

    colourSettings = display.genSelectoionBox(colours)

    sliderLength = constants.SLIDER_LENGTH
    sound = pygame.mixer.music.get_volume()
    soundSlider = Slider((40, 240), sliderLength, sound * sliderLength)
    varSettings = display.genSliders(variables)

    defaultModelCheckBox = CheckBox((1320, 120), 40)

    while not backActive:
        display.backgroundImageBlit(screen, constants.OPTION_IMG)
        for event in pygame.event.get():
            display.checkQuit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttonSound.play()
            elif event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                backActive = display.checkButtonClick(backButton)
                display.checkVolumeSlider(soundSlider, mousePosition, buttonSound)
                if variableAccess:
                    variables = display.checkSlider(
                        defaultModelCheckBox, mousePosition, varSettings, variables
                    )
                    for idx, colourSetting in enumerate(colourSettings):
                        colours[idx] = colourSetting.update(mousePosition)

        backButton.draw(screen)

        for colourSetting in colourSettings:
            colourSetting.draw(screen)

        soundSlider.draw(screen)
        defaultModelCheckBox.draw(screen)
        variables = display.drawSliders(
            screen, variables, varSettings, defaultModelCheckBox
        )

        # set texts and lines on screen
        display.displaySettingText(screen)

        display.displayVariables(screen, variables)

        display.displayUpdate()


def helpScreen():
    # background image
    display.backgroundImageBlit(screen, constants.OPTION_IMG)

    backButton, backActive = display.genBackButton()

    # help screen title
    display.titleText(screen, 80, title="About Virus Simulator", adjustment=250)

    while not backActive:
        for event in pygame.event.get():
            display.checkQuit(event)
            backActive = display.checkBackButton(event, backButton)

        backButton.draw(screen)

        for idx in range(len(constants.HELPS)):
            display.displayText(
                screen, constants.HELPS[idx], 48, (700, 300 + (72 * idx)), centre=True
            )
        display.displayText(screen, "Create by Jay Lee", 48, (700, 750), centre=True)

        display.displayUpdate()
    buttonSound.play()


def simulateScreen():
    manager = Manager(variables, colours)

    optionBox, settingButton, quitButton = display.genPopUP()
    simEndBox, quitSimButton, creditButton = display.genPopUP(
        btnText1="Menu", btnText2="Credits"
    )
    optionActive = False
    quitGame = False
    credit = False

    timeImages = display.loadImages(constants.TIME_TEXTS)

    speed = 1

    while not (quitGame or credit):
        backgroundColour = (
            constants.GREY
            if colours[-1] == constants.BLACK
            else constants.BACKGROUND_BLACK
        )
        screen.fill(backgroundColour)

        health = manager.getNumberOfHealthPeople()
        infectious = manager.getNumberOfInfectedPeople()
        death = manager.getNumberOfDeadPeople()

        simEnd = health == 0 or infectious == 0

        # event check
        for event in pygame.event.get():
            display.checkQuit(event)
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                manager.setSpeed(1 if optionActive else 0)
                optionActive = not optionActive
            elif event.type == pygame.MOUSEBUTTONDOWN:
                buttonSound.play()
            elif event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if optionActive:
                    if display.checkButtonClick(settingButton):
                        optionScreen(variableAccess=False)
                    quitGame = display.checkButtonClick(quitButton)
                elif simEnd:
                    quitGame = display.checkButtonClick(quitSimButton)
                    credit = display.checkButtonClick(creditButton)
                else:
                    speed = display.timeSetting(
                        manager, timeImages, mousePosition, speed
                    )

        manager.movePerson(screen)
        manager.checkInfected()
        manager.checkDeath()

        display.displaySimText(screen, health, infectious, death)
        display.displayTimeText(screen, timeImages, speed)

        if optionActive:
            display.displayPopUp(screen, optionBox, settingButton, quitButton)
        elif simEnd:
            display.simEndPopUP(
                screen, simEndBox, quitSimButton, creditButton, infectious
            )

        display.displayUpdate()
    if simEnd and credit:
        creditScreen()


def creditScreen():
    # background image
    display.backgroundImageBlit(screen, constants.OPTION_IMG)

    backButton, backActive = display.genBackButton(text="Menu")

    # help screen title
    display.titleText(screen, 80, title="Credits", adjustment=250)

    while not backActive:
        for event in pygame.event.get():
            display.checkQuit(event)
            backActive = display.checkBackButton(event, backButton)

        backButton.draw(screen)

        for idx in range(len(constants.CREDITS_TEXT)):
            display.displayText(
                screen, constants.CREDITS_TEXT[idx], 48, (180, 300 + (120 * idx))
            )
        display.displayText(screen, "Since June 2021", 32, (180, 750), centre=True)
        display.displayText(
            screen, "Thank you for using Virus Simulator", 32, (700, 750), centre=True
        )

        display.displayUpdate()
    buttonSound.play()


if __name__ == "__main__":
    # initialize pygame
    pygame.init()
    pygame.display.set_caption(constants.TITLE)
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    buttonSound = display.musicInit()
    variables: list = [100, 25, 4, 6]
    colours: list = [constants.WHITE, constants.RED, constants.BLACK]

    splashScreen()
    menuScreen()
