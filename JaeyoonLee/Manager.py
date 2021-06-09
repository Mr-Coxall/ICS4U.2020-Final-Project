#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Jun 2021
# This class managing simulator.


import math
import random

import constants
from Person import Infectious, Person


class Manager:
    def __init__(self):
        self.healthPeople = self.generatePeople(
            constants.N_PEOPLE - 1, [100, 1300], [100, 700], constants.WHITE
        )
        self.infectedPeople = self.generatePeople(
            1, [650, 750], [350, 450], constants.RED, infected=True
        )
        self.deadPeople = []

    def movePerson(self, screen):
        for personIndex in range(self.getNumberOfLivingPeople()):
            person = self.separatePeople(personIndex)
            person.draw(screen)
            if person.getVelocity() != 0:
                person.move()
                if random.randint(1, constants.FPS) == constants.FPS:
                    person.setDirection(random.uniform(0, 2 * math.pi))
                if self.hitWall(person.getX(), person.getY(), person.getDirection(), constants.RADIUS):
                    person.setDirection(person.getDirection() + math.pi)

    def checkInfected(self):
        for infectious in self.infectedPeople:
            healthCount = 0
            for health in self.healthPeople:
                distance = math.sqrt(
                    (infectious.getX() - health.getX()) ** 2
                    + (infectious.getY() - health.getY()) ** 2
                )
                if distance < constants.RADIUS * 2:
                    # Collide
                    newInfectious = Infectious(
                        health.getX(),
                        health.getY(),
                        health.getVelocity(),
                        health.getDirection(),
                        constants.RED,
                        infectious.getInfectionRate(),
                        infectious.getDeathRate(),
                    )
                    self.infectedPeople.append(newInfectious)
                    del self.healthPeople[healthCount]

                healthCount += 1

    def checkDeath(self):
        pass

    def mutateVirus(self):
        pass

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
            velocity = 1
            if not infected:
                person = Person(
                    x, y, velocity, random.uniform(-math.pi, math.pi), colour
                )
            else:
                person = Infectious(
                    x, y, velocity, random.uniform(-math.pi, math.pi), colour, 10, 10
                )
            people.append(person)
        return people

    def separatePeople(self, personIndex):
        if personIndex < len(self.healthPeople):
            return self.healthPeople[personIndex]
        else:
            return self.infectedPeople[personIndex - len(self.healthPeople)]
    
    def neg_or_pos(self, n):
        if random.randint(0, 1) == 0:
            n *= -1
        return n

    def hitWall(self, pos_x, pos_y, direction, radius):
        if pos_x - radius < 0:
            if math.cos(direction) < 0:
                return True
        elif pos_x + radius > constants.MAX_WIDTH:
            if math.cos(direction) > 0:
                return True
        if pos_y - radius < 0:
            if math.sin(direction) < 0:
                return True
        elif pos_y + radius > constants.MAX_HEIGHT:
            if math.sin(direction) > 0:
                return True
        return False

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
        return constants.N_PEOPLE - len(self.deadPeople)
