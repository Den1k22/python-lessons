

my_list = [element * element for element in range(5)]

my_list_2 = []
for element in range(5):
  my_list_2.append(element)

print(my_list)
print(my_list_2)


field = [["." for x in range(10)] for y in range(10)]
[print( "".join(row) ) for row in field]


my_list = [[element, element * element] for element in range(6)]
print(my_list)
[print(number, power_of_two) for number, power_of_two in my_list]
