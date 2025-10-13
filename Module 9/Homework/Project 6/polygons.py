import math

class Polygon:
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 / 7) * (self.radius ** 2)

if __name__ == "__main__":
    t = Triangle(int(input("\nEnter base of triangle: ")), int(input("Enter height of triangle: ")))
    print("Area of Triangle:", t.area())

    r = Rectangle(int(input("\nEnter length of rectangle: ")), int(input("Enter width of rectangle: ")))
    print("Area of Rectangle:", r.area())

    s = Square(int(input("\nEnter side of square: ")))
    print("Area of Square:", s.area())

    c = Circle(int(input("\nEnter radius of circle: ")))
    print("Area of Circle:", c.area())