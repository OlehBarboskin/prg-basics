user_input = int(input("Enter a number: "))
for i in range(user_input, 0, -1):
    if i > 5:
        print(i)
for i in range(user_input, 0, -1):
    if i == 5:
        print("Five")
        continue
    if i == 4:
        print("Four")
        continue
    if i == 3:
        print("Three")
        continue
    if i == 2:
        print("Two")
        continue
    if i == 1:
        print("One")
        continue

