
import random
import time


ALIVE = 'o'
DEAD = ' '
# LIST_OF_NEIGHBORS = [[-1,-1], [-1,0], [-1,+1], [0,-1], [0,+1], [+1,-1], [+1,0], [+1,+1]]


def create_empty_field(field_size, empty_cell_symbol='.'):
  # return [[symbol for x in range(field_size)] for y in range(field_size)]
  new_list = []
  for row in range(field_size):
    row_list = []
    for column in range(field_size):
      row_list.append(empty_cell_symbol)
    new_list.append(row_list)
  return new_list


def randomizeField(field, field_size):
  for field_cell_y in range(1, field_size + 1):
    for field_cell_x in range(1, field_size + 1):
      if random.random() > 0.5:
        field[field_cell_y][field_cell_x] = ALIVE


def loadFile(field, field_size):
  f = open("glider_gun.txt", "r")
  file_text = f.readlines()
  f.close()

  table = []
  for line in file_text:
    splited_line = line.split(sep=',')
    table.append(splited_line)

  table_max_width = len(file_text[0].split(sep=','))
  table_max_height = len(file_text)

  for field_cell_y in range(1, field_size + 1):
    for field_cell_x in range(1, field_size + 1):
      if (field_cell_y > table_max_height) or (field_cell_x > table_max_width):
        field[field_cell_y][field_cell_x] = DEAD
        continue

      if table[field_cell_y - 1][field_cell_x - 1] == '*':
        field[field_cell_y][field_cell_x] = ALIVE
      else:
        field[field_cell_y][field_cell_x] = DEAD


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

  # for neighbor in LIST_OF_NEIGHBORS:
  #   if (field[field_cell_y + neighbor[0]][field_cell_x + neighbor[1]] == ALIVE):
  #     neighbors += 1

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

  # field = new_field # this does not work,
  # because here we change where points function's field variable not main loop's field variable
  field.clear()
  field.extend(new_field)


def main():
  field_size = 40

  field = create_empty_field(field_size+2, DEAD)

  loadFile(field, field_size)

  while True:
    clear_screen()
    print_field(field, field_size)
    updateField(field, field_size)
    time.sleep(0.1)

main()
