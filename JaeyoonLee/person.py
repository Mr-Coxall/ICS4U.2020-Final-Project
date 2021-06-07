#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This class is person class


import math

import constants
import pygame


class Person:
    def __init__(self, x, y, velocity, direction, colour):
        self.__x = x
        self.__y = y
        self.__velocity = velocity
        self.__direction = direction
        self.__colour = colour

    def move(self):
        vx = math.cos(self.getDirection()) * self.getVelocity()
        vy = math.sin(self.getDirection()) * self.getVelocity()
        self.__x += vx
        self.__y += vy

    def draw(self, screen):
        pygame.draw.circle(
            screen, self.__colour, [int(self.__x), int(self.__y)],
            constants.RADIUS
        )

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getVelocity(self):
        return self.__velocity

    def getDirection(self):
        return self.__direction

    def getColour(self):
        return self.__colour

    def setDirection(self, direction):
        self.__direction = direction

    def setColour(self, colour):
        self.__colour = colour


class Infectious(Person):
    def __init__(self, x, y, velocity, direction, colour, infectionRate,
                 deathRate):
        self.infectionRate = infectionRate
        self.deathRate = deathRate
        super().__init__(x, y, velocity, direction, colour)

    def mutate(self):
        pass

    def getInfectionRate(self):
        return self.infectionRate

    def getDeathRate(self):
        return self.deathRate
