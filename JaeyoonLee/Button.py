#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This class is button class


import constants
import pygame


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        colour=constants.WHITE,
        textColour=constants.RED,
    ):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__rect = pygame.Rect(x, y, width, height)
        self.__colour = colour
        self.__font = pygame.font.SysFont(constants.FONT, height)
        self.__text = self.__font.render(text, True, textColour)

    def draw(self, screen):
        pygame.draw.rect(screen, self.__colour, self.__rect)
        screen.blit(self.__text, self.__text.get_rect(center=self.__rect.center))

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getRect(self):
        return self.__rect

    def getFont(self):
        return self.__font

    def getText(self):
        return self.__text

    def getColour(self):
        return self.__colour

    def setColour(self, colour):
        self.__colour = colour


class SelectionBox(Button):
    def __init__(
        self,
        x,
        y,
        width,
        height,
        colour,
        optionList,
        textColour,
        selected=0,
    ):
        super().__init__(
            x, y, width, height, optionList[0], colour=colour, textColour=textColour[0]
        )
        self.__optionList = optionList
        self.__textColour = textColour
        self.__selected = selected
        self.__menuActive = False
        self.__optionRects = [
            pygame.Rect(x, y + (height * idx + 1), width, height)
            for idx in range(len(optionList))
        ]

    def draw(self, screen):
        rectColour = (0, 0, 0)
        rectScreen = screen.copy()
        rectScreen.fill(rectColour)
        for idx in range(len(self.__optionList)):
            if self.__menuActive:
                rectColour = self.getColour()
            else:
                super().draw(screen)
            rectScreen.set_alpha(0)
            text = self.getFont().render(
                self.__optionList[idx], True, self.__textColour[idx]
            )
            rect = self.__optionRects[idx]
            pygame.draw.rect(rectScreen, self.getColour(), rect)
            rectScreen.blit(text, text.get_rect(center=rect.center))

    def update(self):
        mousePosition = pygame.mouse.get_pos()
        if self.getRect().collidepoint(mousePosition):
            self.__menuActive = not self.__menuActive

    def getOptionList(self):
        return self.__optionList

    def getSelected(self):
        return self.__selected

    def setMenuActive(self, menuActive):
        self.__menuActive = menuActive

    def setSelected(self, selected):
        self.__selected = selected
