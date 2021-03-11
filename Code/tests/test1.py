# Create variable "number" and assign number 5 to it
number = 5

# Create variable "user_input" and assign raw user input to it
users_input = input("Enter a number: ")

# Create variable "user_number" and assign converted "user_input" to number (int)
user_number = int(users_input)

# Create if-elif-else statement: if "user_number" is less than "number", else if "user_number" is more than "number" and else "user_number" is equals "number"
if(user_number == number):
  print("user_number equals number")
elif(user_number < number):
  print("user_number less than number")
else:
 print("user_number bigger than number")

# Create while loop which starts from 0 and finish when it will do "number"'s amount of loops. Each loop should display loop's index number and power of 2 it (number, number^2)
counter = 0
while(counter < number):
  print(counter, counter*counter)
  counter += 1
