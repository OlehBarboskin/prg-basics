car_speed = int(input("Enter the speed of the car in km/h: "))

speed_exceeded = False

while car_speed >= 40 and car_speed <= 140:
    print("Speed is within the allowed range.")
    break
else:
    print("Speed is outside the allowed range.")