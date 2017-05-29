import random

class RandomWalker:
    
    def __init__(self, name = "", xInit = 0, yInit = 0):
        self.__name     = name
        self.__xInit    = xInit
        self.__yInit    = yInit
        
    def getX(self):
        return self.__xInit
    
    def getY(self):
        return self.__yInit
    
    def randomStep(self):
        orientation = random.choice(['x','y'])
        magnitude   = random.choice([-1, 1])
        
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
        self.__xMinInit     = xMinInit
        self.__yMinInit     = yMinInit
        self.__xMaxInit     = xMaxInit
        self.__yMaxInit     = yMaxInit

    def isInField(self, x, y):
        if x <= self.__xMaxInit and x >= self.__xMinInit:
            if y <= self.__yMaxInit and y >= self.__yMinInit:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return 'x min: {} x max: {}'.format(self.__xMinInit, self.__xMaxInit) + '\n' + 'y min: {} y max: {}'.format(self.__yMinInit, self.__yMaxInit)

FieldOne = Field(-1, -1, 1, 1)

print("For boundaries: -1 and 1")

HaronWalker = RandomWalker("Haron", 0, 0)

stepCount = []

for x in range(0, 100):
    i = 0
    j = 1
    while i < j:
        HaronWalker.randomStep()
        
        if FieldOne.isInField(HaronWalker.getX(), HaronWalker.getY()):
            j += 1
            i += 1
        else:
            stepCount.append(i)
            HaronWalker.reset()
            break

minCount    = min(stepCount)
maxCount    = max(stepCount)
average     = sum(stepCount)/len(stepCount)

print("  Minimum steps:   {}".format(minCount), "\n", " Maximum steps:   {}".format(maxCount), "\n", " Average steps:   {:0.2f}".format(average))

FieldTwo = Field(-4, -4, 4, 4)

print("For boundaries: -4 and 4")

HaronWalker = RandomWalker("Haron", 0, 0)

stepCount = []

for x in range(0, 100):
    i = 0
    j = 1
    while i < j:
        HaronWalker.randomStep()
        
        if FieldTwo.isInField(HaronWalker.getX(), HaronWalker.getY()):
            j += 1
            i += 1
        else:
            stepCount.append(i)
            HaronWalker.reset()
            break

minCount    = min(stepCount)
maxCount    = max(stepCount)
average     = sum(stepCount)/len(stepCount)

print("  Minimum steps:   {}".format(minCount), "\n", " Maximum steps:   {}".format(maxCount), "\n", " Average steps:   {:0.2f}".format(average))

FieldThree = Field(-13, -13, 13, 13)

print("For boundaries: -13 and 13")

HaronWalker = RandomWalker("Haron", 0, 0)

stepCount = []

for x in range(0, 100):
    i = 0
    j = 1
    while i < j:
        HaronWalker.randomStep()
        
        if FieldThree.isInField(HaronWalker.getX(), HaronWalker.getY()):
            j += 1
            i += 1
        else:
            stepCount.append(i)
            HaronWalker.reset()
            break

minCount    = min(stepCount)
maxCount    = max(stepCount)
average     = sum(stepCount)/len(stepCount)

print("  Minimum steps:   {}".format(minCount), "\n", " Maximum steps:   {}".format(maxCount), "\n", " Average steps:   {:0.2f}".format(average))


