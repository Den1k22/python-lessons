


FIRST_PLAYER = "X"
SECOND_PLAYER = "O"
EMPTY = "."


def check_coordinates(coordinates):
  if (len(coordinates) < 2): # check that there are more than 1 number
    return False
  elif (not coordinates[0].isnumeric() or not coordinates[1].isnumeric()): # check that they are numbers
    return False
  else:
    return True


def set_symbol_to_field(field, x, y, symbol):
  turn_made = False
  if (field[x][y] == EMPTY):
    field[x][y] = symbol
    turn_made = True

  return turn_made


def check_field(field, symbol):
  result = False

  if (field[0][0] == field[0][1] and field[0][1] == field[0][2] and field[0][2] == symbol):
    result = True
  elif (field[1][0] == field[1][1] and field[1][1] == field[1][2] and field[1][2] == symbol):
    result = True
  elif (field[2][0] == field[2][1] and field[2][1] == field[2][2] and field[2][2] == symbol):
    result = True
  elif (field[0][0] == field[1][0] and field[1][0] == field[2][0] and field[2][0] == symbol):
    result = True
  elif (field[0][1] == field[1][1] and field[1][1] == field[2][1] and field[2][1] == symbol):
    result = True
  elif (field[0][2] == field[1][2] and field[1][2] == field[2][2] and field[2][2] == symbol):
    result = True
  elif (field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[2][2] == symbol):
    result = True
  elif (field[0][2] == field[1][1] and field[1][1] == field[2][0] and field[2][0] == symbol):
    result = True

  return result

def is_field_filled(field, empty_symbol):
  is_filled = True
  for row in field:
    for column in row:
      if (column == empty_symbol):
        is_filled = False
        break
  return is_filled


def draw_field(field):
  for line in field:
    for symbol in line:
      print(symbol, end=" ")
    print()
  print()


def main():
  field = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
  player_turn = True # true = x, false = o

  print("This is tic tac toe game")
  print("Coordinates for field:\n [1,1][1,2],[1,3]\n [2,1][2,2],[2,3]\n [3,1][3,2],[3,3]")
  while True:
    draw_field(field)
    if (player_turn):
      print("X turn")
    else:
      print("O turn")

    user_input = input("Enter coordinates(divide with space):")

    coordinates = user_input.split(" ")

    correct_input = check_coordinates(coordinates)

    if (not correct_input):
      print("Incorrect coordinates")
      continue

    x = int(coordinates[0])
    y = int(coordinates[1])

    if (x < 1 or x > 3 or y < 1 or y > 3):
      print("Incorrect coordinates")
      continue

    if (player_turn):
      turn_made = set_symbol_to_field(field, x-1, y-1, FIRST_PLAYER)
    else:
      turn_made = set_symbol_to_field(field, x-1, y-1, SECOND_PLAYER)

    if (not turn_made):
      continue

    if check_field(field, FIRST_PLAYER):
      print("X won")
      break

    if check_field(field, SECOND_PLAYER):
      print("O won")
      break

    if is_field_filled(field, EMPTY):
      print("Draw")
      break

    player_turn = not player_turn

  draw_field(field)

main()
