prices = {"pizza": 12, "burger": 8, "fries": 4, "soda": 2} 

try:
    item = input("Enter food you'd like to buy: ")
    print(prices[item])
except KeyError:
    print("Sorry. That is not on the menu.")