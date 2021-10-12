

import random

class Circle:
  def __str__(self) -> str:
    return "this is circle with number " + str(self.number)

  def __init__(self):
    self.number = random.randint(1, 1000)
    print("hello", self.number)

  def do_something(self):
    print("working", self.number)

circle = Circle()

print(circle)


circle_text = str(circle)

circle.do_something()
circle.do_something()
circle.do_something()

circle.__init__()
circle.do_something()
circle.do_something()
