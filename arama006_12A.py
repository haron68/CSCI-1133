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

class WalkerGroup(Field, RandomWalker):
    def __init__(self, fieldObj = Field, walkers = [], stepCount = 0):
        self.__walkers = walkers
        self.__fieldObj = fieldObj
        self.__stepCount = stepCount

    def getStepCount(self):
        stepCount = self.__stepCount
        return stepCount

    def allTakeOneStep(self):
        walkers = self.__walkers

        for walker in walkers:
            walker.randomStep()

        self.__stepCount += 1

    def countMeetings(self):
        walkers = self.__walkers
        meetingCount = 0

        for walker1 in walkers:
            for walker2 in walkers:
                if walker1.getX() == walker2.getX() and walker1.getY() == walker2.getY():
                    meetingCount += 1

        meetingCount -= len(walkers)
        return meetingCount

    def numberOut(self):
        walkers = self.__walkers
        field = self.__fieldObj
        outCount = 0

        for walker in walkers:
            if field.isInField(walker.getX(), walker.getY()):
                outCount += 0
            else:
                outCount += 1

        return outCount

    def __str__(self):
        walkers = self.__walkers
        field = self.__fieldObj

        walkerGroupString = ""
        walkerGroupString += "Field:\n{}\n".format(field.__str__())

        walkers.sort()
        for walker in walkers:
            walkerGroupString += "{} \n".format(walker.__str__())

        walkerGroupString += "Number of Steps: \t{}\n\n".format(self.__stepCount)
        walkerGroupString += "Number of Meetings: \t{}".format(self.countMeetings())

        return walkerGroupString

myField = Field(-5, -5, 5, 5)

Walker1 = RandomWalker("One", 0, 0)
Walker2 = RandomWalker("Two", 0, 0)
Walker3 = BiasedRandomWalker([[1, 0, .24], [0, 1, .24], [-1, 0, .24], [0, -1, .24], [1, 1, .04]], "Three", 0, 0)
Walker4 = BiasedRandomWalker([[1, 0, .23], [0, 1, .23], [-1, 0, .23], [0, -1, .31]], "Four", 0, 0)

walkerGroup = WalkerGroup(myField, [Walker1, Walker2, Walker3, Walker4], 0)

while walkerGroup.numberOut() <= 0:
    walkerGroup.allTakeOneStep()
    walkerGroup.countMeetings()

print(walkerGroup)