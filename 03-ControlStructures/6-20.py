decimal_number = int(input("Enter a decimal number: "))

binary_number = (decimal_number % 2)/2

print(f"The binary representation (first digit after decimal point) is: {int(binary_number * 10)}")