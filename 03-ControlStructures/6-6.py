parking_input = int(input("Enter parking duration in hours: "))

if parking_input >= 1 and parking_input <= 2:
    parking_fee = 5
elif parking_input >= 3 and parking_input <= 6:
    parking_fee = 15
elif parking_input >= 6:
    parking_fee = 20

print(f"The fee: {parking_fee}")