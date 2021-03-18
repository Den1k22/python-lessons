# To create empty field 10 x 10 and with chaotic way fill it with symbol "*"
# Program should be clsoed when whole field is filled with symbols "*"

# Steps:
# Create empty field (use two-dimensional array)
# in the while-loop:
#   generate random number for row and column
#   set "*" in the cell which has coordinates with generated numbers
#   check that all cell are filled with "*"
#   when all cells are filled with "*" -> exit

import random

def print_field(field):
  for row in field:
    for column in row:
      print(column, end="")
    print()
  print()

def is_field_filled(field):
  is_filled = True
  for row in field:
    for column in row:
      if (column != "*"):
        is_filled = False
        break
  return is_filled

def main():
  size = 10

  field = [["." for x in range(size)] for y in range(size)]

  print_field(field)

  while(True):
    random_row = random.randint(0, size - 1)
    random_column = random.randint(0, size - 1)

    field[random_row][random_column] = "*"

    print_field(field)

    if (is_field_filled(field)):
      break

main()
