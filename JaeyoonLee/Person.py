#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This class is person class


import math
import random

import pygame


class Person:
    def __init__(self, x, y, velocity, direction, colour, radius):
        self.__x = x
        self.__y = y
        self.__velocity = velocity
        self.__direction = direction
        self.__colour = colour
        self.__radius = radius

    def move(self):
        vx = math.cos(self.getDirection()) * self.getVelocity()
        vy = math.sin(self.getDirection()) * self.getVelocity()
        self.__x += vx
        self.__y += vy

    def draw(self, screen):
        pygame.draw.circle(
            screen, self.__colour, [int(self.__x), int(self.__y)], self.__radius
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

    def setVelocity(self, velocity):
        self.__velocity = velocity

    def setDirection(self, direction):
        self.__direction = direction

    def setColour(self, colour):
        self.__colour = colour


class Infectious(Person):
    def __init__(
        self, x, y, velocity, direction, colour, radius, infectionRate, deathRate
    ):
        super().__init__(x, y, velocity, direction, colour, radius)
        self.__infectionRate = infectionRate
        self.__deathRate = deathRate
        self.__deathCount = 0

    def mutate(self):
        if random.randint(0, 1) == 0:
            self.__infectionRate = random.randint(0, 100)
        else:
            self.__deathRate = random.randint(0, 100)

    def getInfectionRate(self):
        return self.__infectionRate

    def getDeathRate(self):
        return self.__deathRate

    def getDeathCount(self):
        return self.__deathCount

    def setDeathCount(self, deathCount):
        self.__deathCount = deathCount
