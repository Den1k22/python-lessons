

line_with_text = "text1 text2 text3"
print(line_with_text)
print("========")

"""
.split() method
"""
divided_lines = line_with_text.split(" ")

for line in divided_lines:
  print(line)
print("========")

"""
.replace() method
"""
line_after_replace = line_with_text.replace(" ", "\n")

print(line_after_replace)
print("========")


"""
users input problem
"""
users_input = input("Enter two numbers(separated with space): ")

numbers = users_input.split(" ")

if (len(numbers) < 2): # check that there are more than 1 number
  print("There are not enough numbers")
elif (numbers[0].isnumeric() and numbers[1].isnumeric()): # check that they are numbers
  print("First number: ", int(numbers[0]))
  print("Second number: ", int(numbers[1]))
else:
  print("Incorrect numbers")
print("========")

"""
Change case of letters
"""
line_with_letters = "LiNeWiThLetTeRs"
print(line_with_letters)

"""
change to lower case
"""
print(line_with_letters.lower())

"""
change to upper case
"""
print(line_with_letters.upper())
