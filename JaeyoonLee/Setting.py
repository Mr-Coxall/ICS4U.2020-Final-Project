#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This class is slider class


import constants
import pygame


class Slider:
    def __init__(self, startPos, length, default, colour=constants.WHITE):
        self.__startPos = startPos
        self.__length = length
        self.__default = int(default)
        self.__colour = colour
        self.__pointPos = (self.getX() + self.__default, self.getY())
        self.__rect = pygame.Rect(startPos, (length, 4))

    def draw(self, screen):
        pygame.draw.rect(screen, self.__colour, self.__rect)
        pygame.draw.circle(screen, constants.GREY, self.__pointPos, 10)

    def updatePoint(self, pos):
        xPos = list(pos)[0]
        self.setPoint(xPos)
        return xPos - self.getX()

    def getStartPos(self):
        return self.__startPos

    def getX(self):
        return list(self.__startPos)[0]

    def getY(self):
        return list(self.__startPos)[1]

    def getLength(self):
        return self.__length

    def getColour(self):
        return self.__colour

    def getRect(self):
        return self.__rect

    def setDefault(self, default):
        self.__default = int(default)
        self.__pointPos = (self.getX() + self.__default, self.getY())

    def setPoint(self, xPos):
        self.__pointPos = (xPos, self.getY())


class CheckBox:
    def __init__(
        self,
        pos,
        size,
        border=4,
        checked=True,
        boxColour=constants.WHITE,
        checkBtnColour=constants.RED,
    ):
        self.__boxPos = pos
        self.__boxSize = size
        self.__checkBtnSize = size - (2 * border)
        self.__checked = checked
        self.__boxColour = boxColour
        self.__checkBtnColour = checkBtnColour
        self.__checkBtnPos = (self.getX() + border, self.getY() + border)
        self.__box = pygame.Rect(pos, (size, size))
        self.__checkBtn = pygame.Rect(
            self.__checkBtnPos, (self.__checkBtnSize, self.__checkBtnSize)
        )

    def draw(self, screen):
        # screen = screen.copy()
        pygame.draw.rect(screen, self.__boxColour, self.__box)
        if self.__checked:
            pygame.draw.rect(screen, self.__checkBtnColour, self.__checkBtn)

    def update(self):
        self.__checked = not self.__checked
        return self.__checked

    def getStartPos(self):
        return self.__boxPos

    def getX(self):
        return list(self.__boxPos)[0]

    def getY(self):
        return list(self.__boxPos)[1]

    def getChecked(self):
        return self.__checked

    def getBoxSize(self):
        return self.__boxSize

    def getBtnSize(self):
        return self.__checkBtnSize

    def getBoxColour(self):
        return self.__boxColour

    def getCheckColour(self):
        return self.__checkBtnColour

    def getBoxRect(self):
        return self.__box

    def getBtnRect(self):
        return self.__checkBtn
