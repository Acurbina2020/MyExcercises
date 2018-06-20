def inputFunction():
    user_input = input("Please define a range.\n")
    if user_input.isdigit():
            user_input = int(user_input) #The machine expects a digit (integer) as input.
            for i in range(user_input):
                    print(i)
    else:
            print("This is not a number, you moron")
            inputFunction() #Writing this makes the machine ask again to input a number. Otherwise, the function will end and it has to be restarted to input a number. For Python 2, write raw_input().
