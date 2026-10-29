item_prices = []
total = 0 
while True:
    try:
        price = input("Enter the price of an item (press q to quit): ")
        if price.lower() == "q":
            break
        price = float(price)   
        if price < 0:
            print("Price cannot be negative") 
        else:
            total += price
            item_prices.append(price)
            print("Item added!")
    except ValueError:
        print("Invalid price")
    finally:
        print("Entry proccessed")
print(f"Items purchased: {len(item_prices)}")
print(f"Total: {total}")