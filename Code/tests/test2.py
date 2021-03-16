# Create variables "lenght" and assign number 10 to it
length = 10

# Create for loop which works in range from 0 to "lenght"("lenght" excluded)
# Each loop should print loop! number
for number in range(0, length):
    print("loop number: ", number + 1)

# Create for loop which works in range from 1 to "lenght"("lenght" included)
# Each loop should print loop! number
for number in range(1, length + 1):
    print("loop!", number)

# set 0 to "lenght" variable
length = 0

# Create while loop where each loop increases lenght by one, but before that it should print next messages:
# "Less than 5" if lenght is less than 5
# "Less than 10" if lenght is less than 10
# "Stop the loop" if lenght is 10 or more!
while True:
  print("Length is now =", length)
  if length < 5:
      print("Less than 5")
  elif length < 10:
      print("Less than 10")
  else:
      print("The loop is now going to stop. It's more than 10")
      break
  length = length + 1

# create two variables:
# variable "number" and set 5 as Integer
# variable "text" and set "10" as String
number = 5
text = "10"

# open file for writing with name "numbers.txt"
f = open("numbers.txt", "w")

# write to file variables: "number" and "text"
number = str(number)
f.write(number + "\n" + text)

# close file
f.close()

# open file for reading with name "numbers.txt"
f = open("numbers.txt", "r")

# read all text from file and print it
print(f.read())

# close file
f.close()
