

import turtle

turtle.showturtle()

side_amount = 16
side_size = 25

angle = 360 / side_amount

turtle.speed(0)

for i in range(side_amount):
  turtle.dot()
  turtle.forward(side_size/2)
  turtle.right(180)
  turtle.circle(side_size/2)
  turtle.right(180)
  turtle.forward(side_size/2)
  turtle.left(angle)

a = input("Press enter to exit")
