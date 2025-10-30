price_entered = float(input("Enter the price: "))
discount_applied = int(input("The discount: "))

reduction = price_entered*(discount_applied/100)
new_price = price_entered - reduction

print(f"{round(new_price,2)}")
print(f"{round(reduction,2)}")
