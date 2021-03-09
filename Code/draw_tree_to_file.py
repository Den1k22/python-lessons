
user_input = input("Enter maximum number: ")
number = int(user_input)

spaces_amount = number // 2

f = open("my_tree.txt", "w")

while (spaces_amount >= 0):
  if (spaces_amount*2 == number):
    spaces_amount -= 1
    continue

  for j in range(spaces_amount):
    f.write(" ")
    # print(" ", sep="", end="")

  for j in range((number - (spaces_amount * 2))):
    f.write("*")
    # print("*", sep="", end="")

  spaces_amount -= 1
  f.write("\n")
  # print()

f.close()
