
def main():
  user_mode_input = input("Choose mode: a(km/h - > m/s), b(m/s -> km/h): ")
  user_speed_input = input("Enter speed value: ")

  if (not user_speed_input.isnumeric()):
    print("Incorrect number")
    return

  speed = int(user_speed_input)

  if (user_mode_input == "a"):
    print(speed * 1000 / 3600)
  elif (user_mode_input == "b"):
    print(speed * 3600 / 1000)
  else:
    print("Incorrect mode")

main()
