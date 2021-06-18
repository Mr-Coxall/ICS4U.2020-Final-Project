#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This file provides functions for the program.

import os
import sys

import constants
import pygame
from Button import Button, SelectionBox
from Setting import Slider

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)
fps = pygame.time.Clock()


def displayText(
    screen, strText, fontSize, position, colour=constants.WHITE, centre=False
):
    font = getFont(fontSize)
    text = font.render(strText, True, colour)
    if centre:
        screen.blit(text, text.get_rect(center=position))
    else:
        screen.blit(text, position)


def checkQuit(event, specific=False):
    if event.type == pygame.QUIT or specific:
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


def update():
    pygame.display.update()
    fps.tick(constants.FPS)


def backgroundImageBlit(screen, strPath):
    path = getFilePath(strPath)
    background = resizeImage(
        pygame.image.load(path), (constants.WIDTH, constants.HEIGHT)
    )
    screen.blit(background, (0, 0))


def titleText(screen, size, title=constants.TITLE, adjustment=100):
    displayText(
        screen,
        title,
        size,
        (constants.CENTER_X, constants.CENTER_Y - adjustment),
        centre=True,
    )


def genMenuButtons():
    buttonText = constants.MENU_TEXTS
    return [
        Button(600, 400 + (60 * index), 200, 50, buttonText[index])
        for index in range(len(buttonText))
    ]


def genSelectoionBox(options):
    return [
        SelectionBox(
            450,
            320 + (170 * idx),
            200,
            40,
            constants.OPTION_BOX,
            constants.PEOPLE_OPTIONS[idx],
            [options[idx]] + constants.PEOPLE_COLOURS[idx][1:],
        )
        for idx in range(len(options))
    ]


def calculateDefault(variable, idx):
    sliderLength = constants.SLIDER_LENGTH
    varRange = constants.MIN_MAX_VAR
    return variable * sliderLength / (varRange[idx][1] - varRange[idx][0])


def genSliders(variables):
    return [
        Slider(
            (740, (2 + idx) * 100 + 40),
            constants.SLIDER_LENGTH,
            calculateDefault(variables[idx], idx),
        )
        for idx in range(len(variables))
    ]


def drawSliders(screen, variables, varSettings, checkBox):
    for idx, varSlider in enumerate(varSettings):
        varSlider.draw(screen)
        if checkBox.getChecked():
            variables[idx] = constants.DEFAULT_VAR[idx]
            varSlider.setDefault(calculateDefault(variables[idx], idx))
    return variables


def settingText(screen):
    displayText(screen, "Setting", 50, (20, 100))
    displayText(screen, "Sound:", 40, (40, 200))
    for idx in range(len(constants.SETTING_TEXTS)):
        displayText(screen, constants.SETTING_TEXTS[idx], 40, (40, 320 + (170 * idx)))
    displayText(screen, "Variables", 50, (720, 100))
    displayText(screen, "Covid mode", 40, (1150, 120))
    for idx in range(len(constants.VARIABLE_TEXTS)):
        displayText(screen, constants.VARIABLE_TEXTS[idx], 40, (740, (2 + idx) * 100))
    drawLine(screen, (10, 140), (210, 140))
    drawLine(screen, (710, 140), (910, 140))
    drawLine(screen, (700, 150), (700, 750))


def displayVariables(screen, variables):
    sound = pygame.mixer.music.get_volume()
    displayText(screen, str(int(sound * 100)), 40, (560, 230))
    for idx, variable in enumerate(variables):
        unit = ""
        if idx in [0, 3]:
            variable = int(variable)
        else:
            unit = "%"
        displayText(screen, str(variable) + unit, 40, (1250, (2 + idx) * 100 + 30))


def sliderCollide(slider, pos):
    pos_x = list(pos)[0]
    pos_y = list(pos)[1]
    return (
        0 < pos_x - slider.getX() < slider.getLength()
        and 0 < pos_y - slider.getY() + 10 < 24
    )


def checkSlider(defaultModelCheckBox, mousePosition, varSettings, variables):
    sliderLength = constants.SLIDER_LENGTH
    varRange = constants.MIN_MAX_VAR
    if defaultModelCheckBox.getBoxRect().collidepoint(mousePosition):
        defaultModelCheckBox.update()
    for idx, varSlider in enumerate(varSettings):
        if sliderCollide(varSlider, mousePosition):
            variables[idx] = (
                varRange[idx][0]
                + varSlider.updatePoint(mousePosition)
                * (varRange[idx][1] - varRange[idx][0])
                / sliderLength
            )
            if variables != constants.DEFAULT_VAR and defaultModelCheckBox.getChecked():
                defaultModelCheckBox.update()
    return variables


def checkVolumeSlider(soundSlider, mousePosition, buttonSound):
    if soundSlider.getRect().collidepoint(mousePosition):
        sliderLength = constants.SLIDER_LENGTH
        sound = soundSlider.updatePoint(mousePosition) / sliderLength
        pygame.mixer.music.set_volume(sound)
        buttonSound.set_volume(sound)


def genPopUP(btnText1="Setting", btnText2="Quit"):
    btnY = 360 if btnText1 == "Setting" else 380
    optionBox = Button(550, 300, 300, 200, "", colour=constants.BLACK)
    settingButton = Button(600, btnY, 200, 32, btnText1)
    quitButton = Button(600, btnY + 48, 200, 32, btnText2)
    return optionBox, settingButton, quitButton


def timeSetting(manager, timeImages, speed):
    mousePosition = pygame.mouse.get_pos()
    for idx in range(3):
        image = timeImages[idx].get_rect(center=(16 + (32 * idx), 108))
        if image.collidepoint(mousePosition):
            speed = (speed * idx) if idx == 2 and speed < 8 else idx
            manager.setSpeed(speed)  # max time speed: x8
    return speed


def simText(screen, health, infectious, death):
    displayText(screen, "Healthy: " + str(health), 30, (5, 5), colour=constants.GREEN)
    displayText(
        screen, "Infectious: " + str(infectious), 30, (5, 35), colour=constants.RED
    )
    displayText(screen, "Death: " + str(death), 30, (5, 65), colour=constants.BLACK)


def TimeText(screen, timeImages, speed):
    for index in range(3):
        screen.blit(timeImages[index], (4 + (32 * index), 84))
    displayText(screen, "x" + str(speed), 50, (110, 90), colour=constants.BLACK)


def popUp(screen, optionBox, settingButton, quitButton):
    optionBox.draw(screen)
    settingButton.draw(screen)
    quitButton.draw(screen)


def simEndPopUP(screen, simEndBox, quitSimButton, creditButton, infectious):
    text1 = (
        constants.VIRUS_END_TEXT[0] if infectious == 0 else constants.HUMAN_END_TEXT[0]
    )
    text2 = (
        constants.VIRUS_END_TEXT[1] if infectious == 0 else constants.HUMAN_END_TEXT[1]
    )
    simEndBox.draw(screen)
    displayText(screen, text1, 32, (700, 330), colour=constants.RED, centre=True)
    displayText(screen, text2, 32, (700, 360), colour=constants.RED, centre=True)
    quitSimButton.draw(screen)
    creditButton.draw(screen)


def musicInit():
    pygame.mixer.music.load(getFilePath(constants.BGM_PATH))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    return pygame.mixer.Sound(getFilePath(constants.BTN_SOUND))


def getFilePath(filePath):
    return os.path.join(sourceFileDir, filePath)


def getFont(fontSize):
    return pygame.font.SysFont(constants.FONT, fontSize)


def getBackgroundColour(colours):
    return (
        constants.GREY if colours[-1] == constants.BLACK else constants.BACKGROUND_BLACK
    )


def drawLine(screen, startPos, endPos, colour=constants.WHITE, lineWidth=2):
    pygame.draw.line(screen, colour, startPos, endPos, lineWidth)


def checkButtonClick(button):
    return button.getRect().collidepoint(pygame.mouse.get_pos())


def genBackButton(text="Back"):
    return Button(10, 10, 150, 50, text), False


def checkBackButton(screen, backButton):
    backActive = False
    for event in pygame.event.get():
        checkQuit(event)
        if event.type == pygame.MOUSEBUTTONUP:
            backActive = checkButtonClick(backButton)

    backButton.draw(screen)

    return backActive


def genInputBox():
    inputBox = Button(
        580,
        400,
        240,
        40,
        constants.VIRUS_NAME,
        colour=constants.DARK_GREY,
        # textColour=constants.WHITE,
    )
    inputBack = Button(520, 360, 360, 180, "", colour=constants.BACKGROUND_BLACK)
    startButton = Button(580, 465, 240, 40, "Start")
    return inputBox, startButton, inputBack


def checkVirusName(event, virus_name, buttonSound):
    if event.key == pygame.K_BACKSPACE:
        virus_name = virus_name[:-1]
    elif len(virus_name) < 15:
        virus_name += event.unicode
    buttonSound.play()
    return virus_name


def drawInputBox(screen, virus_name, inputBoxes, active):
    # inputBoxes = [inputBox, startButton, inputBack]
    inputBoxes[2].draw(screen)
    displayText(
        screen, "Virus Name:", 36, (700, 380), colour=constants.RED, centre=True
    )
    inputBoxes[0].setText(virus_name)
    if active:
        inputBoxes[0].setColour(constants.GREY)
    else:
        inputBoxes[0].setColour(constants.DARK_GREY)
    inputBoxes[0].draw(screen)
    inputBoxes[1].draw(screen)


def drawBackground(screen):
    backgroundImageBlit(screen, constants.MENU_IMG)
    titleText(screen, 100)


def drawBar(screen, pos, size, progress):
    pos = list(pos)
    size = list(size)
    pygame.draw.rect(screen, constants.WHITE, (pos, size), 2)
    innerPos = (pos[0] + 4, pos[1] + 4)
    innerSize = ((size[0] - 7) * progress, size[1] - 7)
    pygame.draw.rect(screen, constants.GREEN, (innerPos, innerSize))
