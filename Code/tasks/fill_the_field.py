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


def ask_number():
  while(True):
    user_input = input("Enter size of the field: ")
    if (user_input.isnumeric()):
      break
  return int(user_input)


def create_empty_field(size, symbol="."):
  return [[symbol for x in range(size)] for y in range(size)]


def print_field(field):
  for row in field:
    for column in row:
      print(column, end="")
    print()
  print()


def is_in_field(field, row, column, symbol):
  return (field[row][column] == symbol) # true if it is in the field, false if it is not in the field


def put_to_field(field, row, column, symbol):
  field[row][column] = symbol


def is_field_filled(field, symbol):
  is_filled = True
  for row in field:
    for column in row:
      if (column != symbol):
        is_filled = False
        break
  return is_filled


def main():
  star = "*"
  empty = "."

  field_size = ask_number()

  field = create_empty_field(field_size, empty)

  print_field(field)

  while(True):
    random_row = random.randint(0, field_size - 1)
    random_column = random.randint(0, field_size - 1)

    if (is_in_field(field, random_row, random_column, star)):
      continue

    put_to_field(field, random_row, random_column, star)

    print_field(field)

    if (is_field_filled(field, star)):
      break


main()
