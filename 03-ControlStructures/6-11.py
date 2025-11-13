current_price = int(input("Enter the current price of the item: "))
previous_price = int(input("Enter the previous price of the item: "))

if current_price <= previous_price*0.90:
    print("Buy the product!")
    print(f"Product price reduced by {(previous_price/current_price-1)*(100):.2f}")
else:
    print("Don't buy the product!")