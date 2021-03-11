

list_table = []

for i in range(1,11):
  table_line = []
  for j in range(1,11):
    table_line.append(i*j)
  list_table.append(table_line)

for row in range(10):
  for column in range(10):
    print(list_table[row][column], end=" ")

  print()
