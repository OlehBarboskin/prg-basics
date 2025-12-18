price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key, value in price_list.items():
    print(f"{key}: ${value}")



sum_of = sum(price_list.values())
print(f"Total inventory value: ${sum_of:.2f}")

for key, value in price_list.items():
    price_list[key] *= 0.9
print("Prices after 10% discount:")
for key, value in price_list.items():
    print(f"{key}: ${value:.2f}")

sum_after_discount = sum(price_list.values())
print(f"Total inventory value after discount: ${sum_after_discount:.2f}")