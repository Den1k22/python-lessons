
import turtle

turtle.showturtle()

turtle.speed(1)  # speed can be from 0 - 10

turtle.forward(100)
turtle.dot()

turtle.right(90)
turtle.forward(100)
turtle.dot()

turtle.left(120)
turtle.forward(100)
print(turtle.heading())
turtle.dot()

turtle.setheading(180)
turtle.forward(200)
turtle.dot()

turtle.setheading(0)
turtle.circle(100)


# turtle.pencsize(5)
# turtle.pencolor('red')
# turtle.bgcolor('gray')
# turtle.goto(0, 100)

turtle.goto(0, 0)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.goto(-200, -200)
turtle.goto(200, -200)
turtle.goto(200, 200)

# turtle.pos()
# turtle.xcor()
# turtle.ycor()
