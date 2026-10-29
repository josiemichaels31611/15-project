animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"]
try:
    userin = int(input("Enter an index: "))
    print(animals[userin])
except IndexError:
    print("That's not a valid index")
except ValueError:
    print("Please enter an integer")