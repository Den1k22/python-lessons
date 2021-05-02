
number = None

while True:
  user_input = input("Enter number(press enter to exit)")
  if (user_input == ""):
    break
  elif(user_input.isnumeric()):
    user_number = int(user_input)
    if number != None:
      if (number < user_number):
        number = user_number
    else:
      number = user_number
  else:
    print("wrong input")

print("The biggest number is:", number)
