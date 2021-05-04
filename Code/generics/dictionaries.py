

phone_book = {
  "Bob": "123",
  "Patrick": "345"
}

print("1:", phone_book)
# 1: {'Bob': '123', 'Patrick': '345'}

phone_book["New_name"] = "678"
print("2:", phone_book)
# 2: {'Bob': '123', 'Patrick': '345', 'New_name': '678'}

removed_record = phone_book.pop("Bob")
print("3:", phone_book)
# 3: {'Patrick': '345', 'New_name': '678'}

print("4:", removed_record)
# 4: 123
