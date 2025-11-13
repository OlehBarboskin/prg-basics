number_of_products = int(input("Enter the number of products: "))
product_price = int(input("Enter the price per product: "))

amount_to_pay = number_of_products * product_price

if number_of_products > 2:
    amount_to_pay = (product_price * 2) + ((number_of_products - 2) * product_price * 0.75)
    print(f"Total amount to pay after 25% discount is: {amount_to_pay}")
else: 
    print(f"Total amount to pay is: {amount_to_pay}")