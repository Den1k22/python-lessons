
import random


MAX_AMOUNT_OF_NUMBERS = 100  # constant


numbers = []  # here we create empty array for random numbers

for i in range(MAX_AMOUNT_OF_NUMBERS):  # range(MAX_AMOUNT_OF_NUMBERS) => [0,1,2,3,4,5,6,7,8,9]
  numbers.append(random.randint(1, 100))  # here we fill numbers array with random numbers


f = open("file_with_numbers.txt", "w")  # open file for writing

for number in numbers:  # in this loop we save array with numbers to the file
  f.write(str(number) + "\n")

f.close
