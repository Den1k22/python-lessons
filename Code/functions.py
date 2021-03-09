

sums = []

def enter_and_save_two_numbers(order_number):
  print("This is", order_number, "call")
  first_number = input("Enter first number: ")
  second_number = input("Enter second number: ")
  sum_of_numbers = int(first_number) + int(second_number)
  return sum_of_numbers

sums.append(enter_and_save_two_numbers(1))
sums.append(enter_and_save_two_numbers(2))
sums.append(enter_and_save_two_numbers(3))
sums.append(enter_and_save_two_numbers(4))
sums.append(enter_and_save_two_numbers(5))

print(sums)
