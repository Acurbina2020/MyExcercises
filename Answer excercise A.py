def inputFunction():
  user_input = int(input("Please define a range.\n"))
  # int must be used so the user_input can be interpreted as integer. Integer is a number without decimal point.
    for i in range(user_input):
      print(i)
