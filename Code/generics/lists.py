

# example of the list
my_list = ["pen", "pencil", "paper", "rock"]
for item in my_list:
  print(item)


# in the next example user enters items and when he will finish the entered items will be displayed
users_inventory = []
while (True):
  users_input = input("Enter item: ")

  if (users_input == ""):
    break
  else:
    users_inventory.append(users_input) # append == add item to end of the list

print("User's inventory: ", end="")
# symbol * tells python to take each element from the list individualy
print(*users_inventory, sep=", ")


# remove element from list with .pop
item_list = [1, 2, 3, 4]
# when use .pop you tell index of the element which should be removed
item_list.pop(2)
print(item_list)

item_list = [1, 2, 3, 4]
# .pop returns removed element and it is possible to store it
removed_element = item_list.pop(2)
print(item_list, "<>", removed_element)

# [1, 2, 4]
# [1, 2, 4] <> 3

# remove element from list with .remove
item_list = [1, 2, 3, 4]
# for .remove you need to define exact item which should be removed
item_list.remove(3)

# [1, 2, 4]
