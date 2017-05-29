import turtle

def drawSquare(xCenter, yCenter, edgeLength, depthLeft):
    if depthLeft >= 1:
        turtle.penup()
        turtle.goto(xCenter, yCenter)
        turtle.forward(edgeLength / 2)
        turtle.right(90)
        turtle.forward(edgeLength / 2)
        turtle.pendown()
        turtle.right(90)
        for i in range(4):
            turtle.forward(edgeLength)
            turtle.right(90)
        return drawSquare(xCenter - (edgeLength / 4), yCenter  + (edgeLength / 4), edgeLength / 4, depthLeft - 1), drawSquare(xCenter + (edgeLength / 4), yCenter + (edgeLength / 4), edgeLength / 4, depthLeft - 1), drawSquare(xCenter + (edgeLength / 4), yCenter  - (edgeLength / 4), edgeLength / 4, depthLeft - 1), drawSquare(xCenter - (edgeLength / 4), yCenter  - (edgeLength / 4), edgeLength / 4, depthLeft - 1)


maxDepth    = int(input("Input depth: "))
xCenter     = int(input("Input xCenter: "))
yCenter     = int(input("Input yCenter: "))
edgeLength  = int(input("Input edgeLength: "))

turtle.speed(0)
drawSquare(xCenter, yCenter, edgeLength, maxDepth)
turtle.exitonclick()