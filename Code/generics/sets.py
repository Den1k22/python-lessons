
my_set = { "apple", "banana", "tomato" }

print(my_set)
# {'apple', 'banana', 'tomato'}

my_set.add("hammer")

print(my_set)
# {'apple', 'banana', 'hammer', 'tomato'}

my_set.add("hammer")

print(my_set)
# {'apple', 'banana', 'hammer', 'tomato'}


text = """
  This file contains different words which can repeat
  This file contains different words which can repeat or not
  This file contains different words which can repeat
  """

# Let's find uniq words:
uniq_words = set()
for word in text.split(" "):
  uniq_words.add(word)

print(uniq_words)
# {'', 'different', 'This', 'contains', 'words', 'or', 'which', 'repeat', 'can', 'repeat\n', '\n', 'not\n', 'file'}

# we need uniq words, that means that we need to remove empty string and special characters
pure_uniq_words = set()

for word in uniq_words:
  # here we use list comprehension to create list of only letters and numbers
  word_as_list = [letter for letter in word if letter.isalnum()]

  pure_word = ''.join(word_as_list)

  if pure_word != "":
    pure_uniq_words.add(pure_word)

print(pure_uniq_words)
# {'which', 'or', 'different', 'not', 'repeat', 'This', 'can', 'contains', 'file', 'words'}
