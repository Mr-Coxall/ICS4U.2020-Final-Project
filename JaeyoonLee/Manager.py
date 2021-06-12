#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This class managing simulator.


import math
import random

import constants
from Person import Infectious, Person


class Manager:
    def __init__(self, variables):
        self.N_people = int(variables[0])
        if variables[0] < 75:
            self.radius = 10
        else:
            self.radius = 5
        self.infectionRate = variables[1]
        self.deathRate = variables[2]
        self.activity = int(variables[3])
        self.healthPeople = self.generatePeople(
            self.N_people - 1, [100, 1300], [100, 700], constants.WHITE
        )
        self.infectedPeople = self.generatePeople(
            1, [650, 750], [350, 450], constants.RED, infected=True
        )
        self.deadPeople = []

    def movePerson(self, screen):
        for personIndex in range(self.N_people):
            person = self.separatePeople(personIndex, death=True)
            person.draw(screen)
            if person.getVelocity() != 0:
                person.move()
                if (
                    random.randint(0, 360 // (self.activity * person.getVelocity()))
                    == 0
                ):
                    person.setDirection(random.uniform(0, 2 * math.pi))
                if self.hitWall(
                    person.getX(),
                    person.getY(),
                    person.getDirection(),
                    self.radius,
                ):
                    person.setDirection(person.getDirection() + math.pi)

    def checkInfected(self):
        for infectious in self.infectedPeople:
            for healthCount, health in enumerate(self.healthPeople):
                healthPos = [health.getX(), health.getY()]
                infectiousPos = [infectious.getX(), infectious.getY()]
                distance = self.getDistance(healthPos, infectiousPos)
                chance = (
                    random.randint(1, 100) <= infectious.getInfectionRate()
                    and distance < self.radius * 2 + 4
                )
                if distance < self.radius * 2 or chance:
                    # infection
                    newInfectious = Infectious(
                        health.getX(),
                        health.getY(),
                        health.getVelocity(),
                        health.getDirection(),
                        constants.RED,
                        self.radius,
                        infectious.getInfectionRate(),
                        infectious.getDeathRate(),
                    )
                    self.infectedPeople.append(newInfectious)
                    del self.healthPeople[healthCount]

    def checkDeath(self):
        for infectionIdx, infectious in enumerate(self.infectedPeople):
            if (
                infectious.getVelocity() != 0
                and infectious.getDeathCount()
                == random.randint(2, 4) * constants.FPS // infectious.getVelocity()
            ):
                if random.randint(1, 100) <= infectious.getDeathRate():
                    newDeath = Person(
                        infectious.getX(),
                        infectious.getY(),
                        0,
                        0,
                        constants.BLACK,
                        self.radius,
                    )
                    self.deadPeople.append(newDeath)
                    del self.infectedPeople[infectionIdx]
            infectious.setDeathCount(infectious.getDeathCount() + 1)

    def mutateVirus(self):
        for infectious in self.infectedPeople:
            if random.randint(0, constants.MUTATE) == 0:
                infectious.mutate()

    def setSpeed(self, speed):
        for personIndex in range(self.getNumberOfLivingPeople()):
            person = self.separatePeople(personIndex)
            person.setVelocity(abs(int(speed)))

    def generatePeople(
        self, N_People, creationDomain, creationRange, colour, infected=False
    ):
        people = []
        for _ in range(N_People):
            x = random.randint(creationDomain[0], creationDomain[1])
            y = random.randint(creationRange[0], creationRange[1])
            velocity = self.radius // 5
            if not infected:
                person = Person(
                    x,
                    y,
                    velocity,
                    random.uniform(-math.pi, math.pi),
                    colour,
                    self.radius,
                )
            else:
                person = Infectious(
                    x,
                    y,
                    velocity,
                    random.uniform(-math.pi, math.pi),
                    colour,
                    self.radius,
                    self.infectionRate,
                    self.deathRate,
                )
            people.append(person)
        return people

    def separatePeople(self, personIndex, death=False):
        if personIndex < len(self.healthPeople):
            return self.healthPeople[personIndex]
        elif death and (personIndex >= self.getNumberOfLivingPeople()):
            return self.deadPeople[personIndex - self.getNumberOfLivingPeople()]
        return self.infectedPeople[personIndex - len(self.healthPeople)]

    def getDistance(self, pos1, pos2):
        return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

    def hitWall(self, pos_x, pos_y, direction, radius):
        if (
            pos_x - radius < 0
            and math.cos(direction) < 0
            or pos_x - radius >= 0
            and pos_x + radius > constants.WIDTH
            and math.cos(direction) > 0
        ):
            return True
        return (
            pos_y - radius < 0
            and math.sin(direction) < 0
            or pos_y - radius >= 0
            and pos_y + radius > constants.HEIGHT
            and math.sin(direction) > 0
        )

    def getHealthPeople(self):
        return self.healthPeople

    def getInfectedPeople(self):
        return self.infectedPeople

    def getDeadPeople(self):
        return self.deadPeople

    def getNumberOfHealthPeople(self):
        return len(self.healthPeople)

    def getNumberOfInfectedPeople(self):
        return len(self.infectedPeople)

    def getNumberOfDeadPeople(self):
        return len(self.deadPeople)

    def getNumberOfLivingPeople(self):
        return self.N_people - len(self.deadPeople)
