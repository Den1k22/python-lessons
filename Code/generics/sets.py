
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
  This file contains different words which can repeat, this
  """

# Let's find uniq words:
uniq_words = set()
for word in text.split(" "):
  uniq_words.add(word)

print(uniq_words)
# {'', 'which', 'repeat\n', 'repeat', 'This', 'contains', 'words', 'can', 'or', 'not\n', 'repeat,', 'different', 'file', 'this\n', '\n'}

# we need uniq words, that means that we need to remove empty string and special characters
pure_uniq_words = set()

for word in uniq_words:
  # here we use list comprehension to create list of only letters and numbers
  word_as_list = [letter for letter in word if letter.isalnum()]

  # word_as_list as example: different => ['d', 'i', 'f', 'f', 'e', 'r', 'e', 'n', 't']

  pure_word = "".join(word_as_list)

  if pure_word != "":
    pure_uniq_words.add(pure_word)

print(pure_uniq_words)
# {'not', 'which', 'repeat', 'This', 'contains', 'words', 'can', 'this', 'or', 'different', 'file'}
