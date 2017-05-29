import random
import math

class RandomWalker:
    def __init__(self, name="", xInit=0, yInit=0):
        self.__name = name
        self.__xInit = xInit
        self.__yInit = yInit

    def getX(self):
        return self.__xInit

    def getY(self):
        return self.__yInit

    def setX(self, newX):
        self.__xInit = newX

    def setY(self, newY):
        self.__yInit = newY

    def getName(self):
        return self.__name

    def randomStep(self):
        orientation = random.choice(['x', 'y'])
        magnitude = random.choice([-1, 1])

        if orientation == 'x':
            self.__xInit += magnitude
        elif orientation == 'y':
            self.__yInit += magnitude

    def reset(self):
        self.__xInit = 0
        self.__yInit = 0

    def __str__(self):
        return "{} ({}, {})".format(self.__name, str(self.__xInit), str(self.__yInit))

    def __eq__(self, walker2):
        if self.getX() == walker2.getX() and self.getY() == walker2.getY():
            return True
        else:
            return False

    def __lt__(self, walker2):
        dSelf       = math.sqrt(math.pow(self.getX(), 2) + math.pow(self.getY(), 2))
        dWalker2    = math.sqrt(math.pow(walker2.getX(), 2) + math.pow(walker2.getY(), 2))

        if dSelf < dWalker2:
            return True
        else:
            return False

class BiasedRandomWalker(RandomWalker):
    def __init__(self, stepProbabilities, name = "", xInit = 0, yInit = 0):
        self.__stepProbabilities = stepProbabilities
        RandomWalker.__init__(self, name, xInit, yInit)

    def getProbabilities(self):
        stepProbabilities = self.__stepProbabilities
        return stepProbabilities

    def randomStep(self):
        randNum = random.uniform(0, 1)

        probList = []
        count = 0
        while count < 4:
            probList.append(self.__stepProbabilities[count][2])
            if randNum <= self.__stepProbabilities[count][2]:
                if count == 0 or count == 2:
                    self.xInit += self.__stepProbabilities[count][0]
                elif count == 1 or count == 3:
                    self.yInit += self.__selfProbabilities[count][1]
            print(randNum)
            print(count)
            count += 1

class Field:
    def __init__(self, xMinInit, yMinInit, xMaxInit, yMaxInit):
        self.__xMinInit = xMinInit
        self.__yMinInit = yMinInit
        self.__xMaxInit = xMaxInit
        self.__yMaxInit = yMaxInit

    def isInField(self, x, y):
        if x <= self.__xMaxInit and x >= self.__xMinInit:
            if y <= self.__yMaxInit and y >= self.__yMinInit:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return 'x min: {} x max: {}'.format(self.__xMinInit, self.__xMaxInit) + '\n' + 'y min: {} y max: {}'.format(
            self.__yMinInit, self.__yMaxInit)


Field = Field(-5, -5, 5, 5)

Walker1 = RandomWalker("Walker1", 0, 0)
Walker2 = RandomWalker("Walker2", 0, 0)
Walker3 = RandomWalker("Walker3", 0, 0)
Biased  = BiasedRandomWalker([[ 1, 0, .4], [ 0, 1, .2], [-1, 0, .2], [ 0, -1, .2]], "Biased")

print(Biased)
Biased.randomStep()
print(Biased)

meetCount = 0
stepCount = 0
i = 0
while i < 1:
    Walker1.randomStep()
    Walker2.randomStep()
    Walker3.randomStep()

    if Field.isInField(Walker1.getX(), Walker1.getY()) and Field.isInField(Walker2.getX(), Walker2.getY()) and Field.isInField(Walker3.getX(), Walker3.getY()):
        if Walker1.__eq__(Walker2) or Walker1.__eq__(Walker3) or Walker2.__eq__(Walker3):
            meetCount += 1

        stepCount += 1
    else:
        if Walker1.__lt__(Walker2) and Walker2.__lt__(Walker3):
            print(Walker1)
            print(Walker2)
            print(Walker3)
        elif Walker1.__lt__(Walker3) and Walker3.__lt__(Walker2):
            print(Walker1)
            print(Walker3)
            print(Walker2)
        elif Walker2.__lt__(Walker1) and Walker1.__lt__(Walker3):
            print(Walker2)
            print(Walker1)
            print(Walker3)
        elif Walker2.__lt__(Walker3) and Walker3.__lt__(Walker1):
            print(Walker2)
            print(Walker3)
            print(Walker1)
        elif Walker3.__lt__(Walker1) and Walker3.__lt__(Walker2):
            print(Walker3)
            print(Walker1)
            print(Walker2)
        else:
            print(Walker3)
            print(Walker2)
            print(Walker1)
        print()
        print("Number of Steps: ", stepCount)
        print("Number of Meetings: ", meetCount)
        break