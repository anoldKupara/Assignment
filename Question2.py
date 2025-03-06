import math

class Shape:
    def CalculateArea(self):
        pass  # Abstract method, to be implemented by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def CalculateArea(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def CalculateArea(self):
        return self.width * self.height

def TotalArea(shapes):
    return sum(shape.CalculateArea() for shape in shapes)

# Creating a list of shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 8)
]

print(f"Total Area: {TotalArea(shapes):.2f}")
