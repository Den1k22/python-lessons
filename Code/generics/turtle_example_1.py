

import turtle

turtle.showturtle()

turtle.speed(5)

for i in range(8):
  turtle.dot()
  turtle.forward(50)
  turtle.circle(50)
  turtle.circle(20)
  turtle.forward(50)
  turtle.left(45)

a = input("Press enter to exit")
