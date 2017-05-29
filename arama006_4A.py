# CSci 1133-20 HW 4
# Haron Arama
# HW 4, Problem 4A

import turtle

def drawTriangle(edgeLength):
    turtle.left(30)
    turtle.forward(edgeLength)
    turtle.right(300)
    turtle.back(edgeLength)
    turtle.left(60)
    turtle.forward(edgeLength)

def drawStemAndTriangle(stemLength, edgeLength):
    turtle.forward(stemLength)
    drawTriangle(edgeLength)
    turtle.home()


stemAndTriangles = int(input("Input quantity of stems and triangles: "))
stemLength      = int(input("Input long stem length: "))
edgeLength      = stemLength / 5
shortStemLength = stemLength / 2

if (stemAndTriangles % 2) == 0:
    j = 0
else:
    j = 1

stemAndTriangle = int(stemAndTriangles / 2)

i = 1
while i <= (stemAndTriangle + j):
    theta = 360 / (stemAndTriangle + j)
    drawStemAndTriangle(stemLength, edgeLength)
    turtle.left((theta * i) + (theta / 2))

    if (stemAndTriangles % 2) != 0 and i == stemAndTriangle + j:
        break

    drawStemAndTriangle(shortStemLength, edgeLength)
    turtle.left(theta * i)
    i += 1

turtle.exitonclick()