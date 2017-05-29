import math

def centroid(pointList):
    x = []
    y = []
    z = []
    for n in range(len(pointList)):
        x.append(float(pointList[n][0]))
        y.append(float(pointList[n][1]))
        z.append(float(pointList[n][2]))

    averagePoint = [(sum(x) / (n + 1)), (sum(y) / (n + 1)), (sum(z) / (n + 1))]

    return averagePoint

def distance(pt1, pt2):
    x = float(pt1[0])
    y = float(pt1[1])
    z = float(pt1[2])

    px = float(pt2[0])
    py = float(pt2[1])
    pz = float(pt2[2])

    averageDistance = math.sqrt(math.pow(x - px, 2) + math.pow(y - py, 2) + math.pow(z - pz, 2))

    return averageDistance

def main():
    points = int(input("Number of points: "))
    pointList = []
    for i in range(0, points):
        point = input("Input next point's x y z: ")
        pointList.append(point)

    point = []
    i = 0
    while i < len(pointList):
        point = pointList[i].split(' ')
        pointList[i] = point
        point = []
        i += 1

    averages = []
    n = 0
    while n < len(pointList):
        averages.append(distance(pointList[n], centroid(pointList)))
        n += 1

    print("Average distance from center: ", round(sum(averages) / n, 6))

    cont = input("Enter another point list (y/n)? ")
    if cont == 'y':
        main()

main()