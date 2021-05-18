

import turtle
import math

turtle.showturtle()

turtle.speed(5)

side = 500
height = side * math.sqrt(3) / 2

turtle.penup()
turtle.goto(0,300)
turtle.pendown()

turtle.dot()
turtle.right(60)
turtle.forward(side)
turtle.right(120)
turtle.forward(side)
turtle.right(120)
turtle.forward(side)
turtle.right(150)
turtle.forward(height)
turtle.left(90)
turtle.circle(height/3)

a = input("Press enter to exit")
