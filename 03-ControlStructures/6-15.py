input_number = input("Enter a 13 symbol number: ")

if len(input_number) == 13 and input_number.startswith("590"):
    print("Valid")
else:
    print("Invalid")