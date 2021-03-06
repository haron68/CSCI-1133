import random


class RandomWalker:
    def __init__(self, name="", xInit=0, yInit=0):
        self.__name = name
        self.__xInit = xInit
        self.__yInit = yInit

    def getX(self):
        return self.__xInit

    def getY(self):
        return self.__yInit

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


Field = Field(-3, -3, 3, 3)

print(Field)

HaronWalker = RandomWalker("Haron", 0, 0)

for i in range(1, 21):
    HaronWalker.randomStep()

    if Field.isInField(HaronWalker.getX(), HaronWalker.getY()):
        print("Step ", i, ": ", HaronWalker.__str__())
    else:
        print("Step ", i, ": ", HaronWalker.__str__())
        break