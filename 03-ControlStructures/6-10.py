enter_age = int(input("Enter your dog age: "))

human_years = 0

if enter_age >= 2:
    human_years = 21 + (enter_age - 2) * 4
    print(f"Dog age in human years is: {human_years}")
elif enter_age == 1:
    human_years = 10.5
    print(f"Dog age in human years is: {human_years}")
else:
    print("Error")
