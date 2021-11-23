

import random

class Circle:
  def __str__(self) -> str:
    return "this is circle with number " + str(self.number)

  def __init__(self):
    self.number = random.randint(1, 1000)
    print("hello", self.number)

  def do_something(self):
    print("working", self.number)

object_circle = Circle()

print(object_circle)

circle_text = str(object_circle)

object_circle.do_something()
object_circle.do_something()
object_circle.do_something()

object_circle.__init__()
object_circle.do_something()
object_circle.do_something()


class Square:
  square_variable = 5

  def show_variable(self):
    print(self.square_variable)

object_square = Square()

print(object_square)

object_square.show_variable()
