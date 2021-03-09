

user_input = input("Enter maximum number: ")
number = int(user_input)

spaces_amount = number // 2
counter = 0
while (spaces_amount >= counter):
  if (counter*2 == number):
    counter += 1
    continue

  for j in range(counter):
    print(" ", sep="", end="")

  for j in range((number - (counter * 2))):
    print("*", sep="", end="")

  counter += 1
  print()


print("======")
#  Christmas tree
#    *
#   ***
#  *****
# *******

spaces_amount = number // 2

while (spaces_amount >= 0):
  if (spaces_amount*2 == number):
    spaces_amount -= 1
    continue

  for j in range(spaces_amount):
    print(" ", sep="", end="")

  for j in range((number - (spaces_amount * 2))):
    print("*", sep="", end="")

  spaces_amount -= 1
  print()


# increasing tree (opposite)
#   *
#  **
# ***
#****
for i in range(number):
  temp = i + 1

  for j in range(number-temp):  # number - i - 1 <=> number - (i+1)
    print(" ",sep="",end="")

  for j in range(temp):
    print("*", sep="", end="")

  print()


# decreasing tree
#****
#***
#**
#*
for i in range(number):
  for j in range(number - i):
    print("*",sep="",end="")
  print()


# increasing tree
# *
# **
# ***
# ****
for i in range(number):
  for j in range(i+1):
    print("*",sep="",end="")
  print()
