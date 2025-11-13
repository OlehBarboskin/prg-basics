coord_x = int(input("Enter the x coordinate: "))
coord_y = int(input("Enter the y coordinate: "))

if coord_x == 0 and coord_y == 0:
    quadrant = "the origin"
elif coord_x > 0 and coord_y > 0:
    quadrant = "Quadrant 1"
elif coord_x < 0 and coord_y > 0:
    quadrant = "Quadrant 2"
elif coord_x < 0 and coord_y < 0:
    quadrant = "Quadrant 3"
else:
    quadrant = "Quadrant 4"

print(f"The point ({coord_x}, {coord_y} is in {quadrant})")