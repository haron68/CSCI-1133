# Homework 11 - B
# TA Julia Garbuz

import random


class RandomWalker():
    def __init__(self, name="", xInit=0, yInit=0):
        self.__name = name
        self.__x = xInit
        self.__y = yInit

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def getName(self):
        return self.__name

    def randomStep(self):
        r = random.randint(1, 4)
        if r == 1:
            self.__x += 1
        elif r == 2:
            self.__x -= 1
        elif r == 3:
            self.__y += 1
        else:
            self.__y -= 1

    def reset(self):
        self.__x = 0
        self.__y = 0

    def distToOrigin(self):
        return ((self.__x) ** 2 + (self.__y) ** 2) ** 0.5

    def __eq__(self, walker2):
        return (self.__x == walker2.getX() and self.__y == walker2.getY())

    def __lt__(self, walker2):
        return self.distToOrigin() < walker2.distToOrigin()

    def __str__(self):
        return self.__name + "  (" + str(self.__x) + ", " + str(self.__y) + ")"


class BiasedRandomWalker(RandomWalker):
    def __init__(self, stepProbabilities, nameInit="", xInit=0, yInit=0):
        RandomWalker.__init__(self, nameInit, xInit, yInit)
        self.__stepProbabilities = stepProbabilities

    def getProbabilities(self):
        return self.__stepProbabilities

    def randomStep(self):
        r = random.random()
        sumProb = 0
        keepChecking = True
        i = 0
        while keepChecking and i < len(self.__stepProbabilities):
            sumProb += self.__stepProbabilities[i][2]
            if r <= sumProb:
                move = self.__stepProbabilities[i]
                keepChecking = False
            i += 1
        self.setX(self.getX() + move[0])
        self.setY(self.getY() + move[1])


class Field():
    def __init__(self, xMinInit, yMinInit, xMaxInit, yMaxInit):
        self.__xMin = xMinInit
        self.__yMin = yMinInit
        self.__xMax = xMaxInit
        self.__yMax = yMaxInit

    def isInField(self, x, y):
        if (self.__xMin <= x <= self.__xMax) and (self.__yMin <= y <= self.__yMax):
            return True
        else:
            return False

    def __str__(self):
        return ("x min:\t" + str(self.__xMin) + "\tx max:\t" + str(self.__xMax) + "\n") + \
               ("y min:\t" + str(self.__yMin) + "\ty max:\t" + str(self.__yMax))

class OriginWalker(BiasedRandomWalker):
    def __init__(self, stepProbabilities, nameInit = "", xInit = 0, yInit = 0, originRevisits = 0):
        BiasedRandomWalker.__init__(self, stepProbabilities, nameInit, xInit, yInit)
        self.__originRevisits = originRevisits

    def getOriginRevisits(self):
        originRevisits = self.__originRevisits
        return originRevisits

    def reset(self):
        BiasedRandomWalker.reset(self)
        self.__originRevisits = 0

    def randomStep(self):
        BiasedRandomWalker.randomStep(self)

        if BiasedRandomWalker.getX(self) == 0 and BiasedRandomWalker.getY(self) == 0:
            self.__originRevisits += 1

    def __str__(self):
        originRevisits = self.__originRevisits
        return "{}\nOrigin Revisits: {}".format(BiasedRandomWalker.__str__(self), originRevisits)

myField = Field(-4, -4, 4, 4)

Walker1 = OriginWalker([[ 1, 0,.25], [ 0, 1,.25], [-1, 0,.25], [ 0, -1,.25]], "One")
Walker2 = OriginWalker([[ 1, 0, .3], [ 0, 1, .2], [-1, 0, .3], [ 0, -1, .2]], "Two")
Walker3 = OriginWalker([[ 1, 0, .4], [ 0, 1, .4], [-1, 0, .1], [ 0, -1, .1]], "Three")

originVisits = []

for i in range(0, 100):
    while myField.isInField(Walker1.getX(), Walker1.getY()):
        Walker1.randomStep()

    originVisits.append(Walker1.getOriginRevisits())
    Walker1.reset()
average = sum(originVisits) / 100
print("For Walker ", Walker1.getName())
print("\tMinimum origin revisits: \t", min(originVisits))
print("\tMaximum origin revisits: \t", max(originVisits))
print("\tAverage origin revisits: \t", average)

originVisits = []

for i in range(0, 100):
    while myField.isInField(Walker2.getX(), Walker2.getY()):
        Walker2.randomStep()

    originVisits.append(Walker2.getOriginRevisits())
    Walker2.reset()
average = sum(originVisits) / 100
print("For Walker", Walker2.getName())
print("\tMinimum origin revisits: \t", min(originVisits))
print("\tMaximum origin revisits: \t", max(originVisits))
print("\tAverage origin revisits: \t", average)

originVisits = []

for i in range(0, 100):
    while myField.isInField(Walker3.getX(), Walker3.getY()):
        Walker3.randomStep()

    originVisits.append(Walker3.getOriginRevisits())
    Walker3.reset()
average = sum(originVisits) / 100
print("For Walker ", Walker3.getName())
print("\tMinimum origin revisits: \t", min(originVisits))
print("\tMaximum origin revisits: \t", max(originVisits))
print("\tAverage origin revisits: \t", average)