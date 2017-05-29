# CSci 1133-20 HW 2
# Haron Arama
# HW 2, Problem 2B

import turtle

turtle.showturtle()

sideLength = int(input("Input the side length(s) of the star: "))

def drawStar(sideLength):
    i = 1
    angle = 75
    turtle.setheading(angle)
    turtle.forward(sideLength)
    while (i <= 7):
        if (i == 1) and (angle == 75):
            angle = 15
            i = 2
            turtle.setheading(angle)
            turtle.forward(sideLength)
        elif (i == 2) and (angle == 15):
            angle = 165
            i = 3
            turtle.setheading(angle)
            turtle.forward(sideLength)
        elif (i == 3) and (angle == 165):
            angle = 105
            i = 4
            turtle.setheading(angle)
            turtle.forward(sideLength)
        elif (i == 4) and (angle == 105):
            angle = 255
            i = 5
            turtle.setheading(angle)
            turtle.forward(sideLength)
        elif (i == 5) and (angle == 255):
            angle = 195
            i = 6
            turtle.setheading(angle)
            turtle.forward(sideLength)
        elif (i == 6) and (angle == 195):
            angle = 345
            i = 7
            turtle.setheading(angle)
            turtle.forward(sideLength)
        elif (i == 7) and (angle == 345):
            angle = 285
            i = 8
            turtle.setheading(angle)
            turtle.forward(sideLength)

drawStar(sideLength)

turtle.exitonclick()