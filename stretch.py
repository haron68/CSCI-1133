import math

def shortestDist(list):

    lengthList = len(list)
    z = []
    distance = []
    a = 0
    i = 0
    while i < (lengthList / 2):
        x = list[a + 1][0] - list[a][0]
        y = list[a + 1][1] - list[a][1]
        z.append(math.pow(x, 2) + math.pow(y, 2))
        distance.append(math.sqrt(z[i]))
        if (a < lengthList - 2):
            a += 2
        else:
            a = 0
        i += 1

    minimum = min(distance)
    print("Minimum: ", minimum, "List: ", list, "Distances: ", distance)

shortestDist([[45, -99], [24, 83], [-48, -68], [-97, 99], \
              [-8, -77], [-2, 50], [44, 41], [-48, -58], \
              [-1, 53], [14, 86], [31, 94], [12, -91], \
              [33, 50], [82, 72], [83, -90], [10, 78], \
              [7, -22], [90, -88], [-21, 5], [6, 23]] )