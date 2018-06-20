MyList1 = ["Polaris", "Aldebaran", "Sirio", "Rigel"]
MyList2 = ["Class A", "Class B", "Class C", "Class D"]

def MyFunction():
    for a, b in zip(MyList1, MyList2):
        user_input = input("Find out what class is your star. Write a name here:\n")
        if user_input in MyList1:
            print (b)
        else:
            print ("Please write name of a star")
            MyFunction()
