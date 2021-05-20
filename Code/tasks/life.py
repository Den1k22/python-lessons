
import random
import time


ALIVE = 'o'
DEAD = ' '


def create_empty_field(field_size, symbol='.'):
  # return [[symbol for x in range(field_size)] for y in range(field_size)]
  new_list = []
  for row in range(field_size):
    row_list = []
    for column in range(field_size):
      row_list.append(symbol)
    new_list.append(row_list)
  return new_list


def randomizeField(field, field_size):
  for field_cell_y in range(1, field_size + 1):
    for field_cell_x in range(1, field_size + 1):
      if random.random() > 0.5:
        field[field_cell_y][field_cell_x] = ALIVE


def clear_screen():
  print(chr(27) + "[2J")


def print_field(field, field_size):
  for field_cell_y in range(1, field_size + 1):
    for field_cell_x in range(1, field_size + 1):
      print(field[field_cell_y][field_cell_x], end="")
    print()
  print()


def countNeighbors(field, field_cell_x, field_cell_y):
  neighbors = 0
  if (field[field_cell_y - 1][field_cell_x - 1] == ALIVE):
    neighbors += 1
  if (field[field_cell_y - 1][field_cell_x    ] == ALIVE):
    neighbors += 1
  if (field[field_cell_y - 1][field_cell_x + 1] == ALIVE):
    neighbors += 1
  if (field[field_cell_y    ][field_cell_x - 1] == ALIVE):
    neighbors += 1
  if (field[field_cell_y    ][field_cell_x + 1] == ALIVE):
    neighbors += 1
  if (field[field_cell_y + 1][field_cell_x - 1] == ALIVE):
    neighbors += 1
  if (field[field_cell_y + 1][field_cell_x    ] == ALIVE):
    neighbors += 1
  if (field[field_cell_y + 1][field_cell_x + 1] == ALIVE):
    neighbors += 1
  return neighbors


def updateField(field, field_size):
  new_field = create_empty_field(field_size+2, DEAD)
  for field_cell_y in range(1, field_size + 1):
    for field_cell_x in range(1, field_size + 1):
      neighbors = countNeighbors(field, field_cell_x, field_cell_y)

      if field[field_cell_y][field_cell_x] == ALIVE:
        if (neighbors < 2) or (neighbors > 3):
          new_field[field_cell_y][field_cell_x] = DEAD
        else:
          new_field[field_cell_y][field_cell_x] = ALIVE
      else:
        if neighbors == 3:
          new_field[field_cell_y][field_cell_x] = ALIVE
        else:
          new_field[field_cell_y][field_cell_x] = DEAD
  return new_field


def main():
  field_size = 30

  field = create_empty_field(field_size+2, DEAD)

  randomizeField(field, field_size)

  while True:
    clear_screen()
    print_field(field, field_size)
    field = list(updateField(field, field_size))
    time.sleep(0.5)

main()
