
import random

# print("Raw random number: ", random.random()) # this line does not affect future code

while True: # menu loop
  print("Try to guess the number")
  random_number = random.randint(0, 100)

  while True: # game loop
    user_input = input("Enter number: ")

    if (not user_input.isnumeric()):
      continue

    user_number = int(user_input)

    if (user_number == random_number):
      print("Cool, you guessed the number!")
      break

    if (random_number > user_number):
      print("Number should be bigger")
    else:
      print("Number should be smaller")

  user_input = input("Do you want to play again? (yes - y, no - everything else): ")
  if (user_input != "y"):
    break

print("EXIT")
