# This program is a simple calculator

num1 = int(input("Enter first number, please "))
num2 = int(input("Enter second number, please "))

# This function adds(sum) two numbers
add = num1 + num2

# this function multiplies(product) two numbers
multiply = num1 * num2

# this function subtracts(difference) two numbers
subtract = num1 - num2

# This function divides(quotient) two numbers
divides = num1 / num2

print(num1, "+", num2, "=", sum)

print(num1, "-", num2, "=", subtract)

print(num1, "*", num2, "=", multiply)

# Add check for division to zero

print(num1, "/", num2, "=", divides)
