

import turtle
import math

turtle.showturtle()

turtle.speed(5)

for i in range(5):
  turtle.dot()
  turtle.forward(200)
  turtle.right(144)

turtle.right(108)
turtle.circle(100/ math.cos(math.radians(18)))

a = input("Press enter to exit")
