
letter_side_a = input("Enter one side of letter: ")
letter_side_b = input("Enter second side of letter: ")

envelope_side_a = input("Enter one side of envelope: ")
envelope_side_b = input("Enter second side of envelope: ")

if (letter_side_a < letter_side_b):
  temp = letter_side_b
  letter_side_b = letter_side_a
  letter_side_a = temp

if (envelope_side_a < envelope_side_b):
  temp = envelope_side_b
  envelope_side_b = envelope_side_a
  envelope_side_a = temp

if (letter_side_a < envelope_side_a and letter_side_b < envelope_side_b):
  print("Letter can fit to the envelope")
else:
  print("Does not fit")
