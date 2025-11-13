input_temperature = int(input("Enter the temperature in Celsius: "))

if input_temperature > 35:
    print("It's extremely hot")
elif input_temperature > 30:
    print("It's hot")
elif input_temperature > 15:
    print("It's warm")
elif input_temperature >= 0:
    print("It's cold")
else:
    print("It's freezing cold")