#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This class is button class


# import constants
import pygame


class Button:
    def __init__(self, x, y, width, height, colour, text, textColour):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__rect = pygame.Rect(x, y, width, height)
        self.__colour = colour
        self.__font = pygame.font.SysFont("notosanscjkkrblack", height)
        self.__text = self.__font.render(text, True, textColour)

    def draw(self, screen):
        pygame.draw.rect(screen, self.__colour, self.__rect)
        screen.blit(self.__text, self.__text.get_rect(center = self.__rect.center))

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

    def getText(self):
        return self.__text

    def getColour(self):
        return self.__colour

    def setColour(self, colour):
        self.__colour = colour


# class SelectionBox(Button):
#     def __init__(self, x, y, width, height, colour, textColour, optionList, selectedColour, selected=0):
#         super().__init__(x, y, width, height, colour, optionList[0], textColour)
#         self.optionList = optionList
#         self.selectedColour = selectedColour
#         self.selected = selected
#         self.draw_menu = False
#         self.menu_active = False

#     def update(self):
#         pass

#     def getOptionList(self):
#         return self.optionList

#     def getSelectedColour(self):
#         return self.selectedColour

#     def getSelected(self):
#         return self.selected
