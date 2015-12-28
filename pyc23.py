# completing the monte carlo approximation of pi

import math

def showMontePi(numDarts):
    wn = turtle.Screen()
    wn.bgcolor("light pink")
    drawingT = turtle.Turtle()

    wn.setworldcoordinates(-2,-2,2,2)

    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)
    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)

    circle = 0
    drawingT.up()

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        d = math.sqrt(x**2 + y**2)

        drawingT.goto(x,y)

        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
        else:
            drawingT.color("red")

        drawingT.dot()

    pi = circle/numDarts * 4

    wn.exitonclick()

    return pi


showMontePi(50)