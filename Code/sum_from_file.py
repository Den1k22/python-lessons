

f = open("file_with_numbers.txt", "r")  # open file for reading

numbers = f.readlines()

f.close


sum_of_numbers = 0  # here we initialize empty sum_of_numbers

for number in numbers:
  number_temp = number.replace("\n", "")

  if (not number_temp.isnumeric()):  # here we check that number is valid
    continue

  sum_of_numbers += int(number_temp)  # here we add to sum converted number


f = open("file_with_numbers_answer.txt", "w")  # open file for writing

f.write(str(sum_of_numbers))

f.close
