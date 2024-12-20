class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perim(self):
    return self.a * 4

square1 = Square(4)
square2 = Square(6)

print(f'Square with side 4:{square1}')
print(f'Area is {square1.area()} Perimeter is {square1.perim()}')
print (f'Square with side 6: Area is {square2.area()}, perim {square2.perim()} ')