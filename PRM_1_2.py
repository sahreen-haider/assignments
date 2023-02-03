class Shape:
    def __init__(self, sides):
        self.sides = sides


class Triangle(Shape):
    def __init__(self, sides):
        Shape.__init__(self, sides)

    def validate_triangle(self):
        a, b, c = self.sides
        if a + b > c and b + c > a and a + c > b:
            return "Valid Triangle"
        else:
            return "Invalid Triangle"


class Rectangle(Shape):
    def __init__(self, sides):
        Shape.__init__(self, sides)

    def validate_rectangle(self):
        a, b, c, d = self.sides
        if a == c and b == d:
            return "Valid Rectangle"
        else:
            return "Invalid Rectangle"


rex = input("enter the 3 sides of the triangle(side side side): ").split()
rex = [int(x) for x in rex]
tr = Triangle(rex)
print(tr.validate_triangle())



rex_1 = input("enter the 4 sides of the rectangle(l b l b): ").split()
rex_1 = [int(x) for x in rex_1]
rect = Rectangle(rex_1)
print(rect.validate_rectangle())
