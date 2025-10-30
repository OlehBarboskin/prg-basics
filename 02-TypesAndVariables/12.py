side_a = int(input("Side A:"))
side_b = int(input("Side B:"))
side_c = int(input("Side C:"))

volume = side_a * side_b * side_c

surface_area = 2*(side_a*side_b) + 2*(side_b*side_c) + 2*(side_a*side_c)

print(f"{volume}")
print(f"{surface_area}")