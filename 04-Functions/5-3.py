def triange_area(a,b,c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

print(f'The area of ​​a triangle with sides 3, 4, and 5 is {triange_area(3, 4, 5)}')