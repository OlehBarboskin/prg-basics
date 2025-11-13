age_group = int(input("Enter your age: "))

if age_group < 13:
    print("Child")
elif age_group >= 13 and age_group < 20:
    print("Teen")
elif age_group >= 20 and age_group < 65:
    print("Adult")
else:
    print("Senior")