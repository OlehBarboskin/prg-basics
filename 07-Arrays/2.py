categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

biggest_number = max(expenses)
index_of_biggest = expenses.index(biggest_number)

print(f"The biggest expense is for {categories[index_of_biggest]} $ {biggest_number}")