

multiplication_table = []

for row in range(1,11):
  table_line = []
  for column in range(1,11):
    table_line.append(row*column)
  multiplication_table.append(table_line)

for row in range(10):
  for column in range(10):
    print(multiplication_table[row][column], end=" ")

  print()
