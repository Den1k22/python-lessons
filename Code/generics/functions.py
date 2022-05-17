

def add_numbers(number1, number2):
  return number1 + number2

def subtract_numbers(number1, number2):
  return number1 - number2

print(add_numbers(7,2))
print(add_numbers(9,9))

print(subtract_numbers(7,2))
print(subtract_numbers(9,9))


def return_two_values():
  return 5, 4

values = return_two_values()
print(values)

a, b = return_two_values()
print(a)
print(b)
