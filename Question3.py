class Shape:
    def __init__(self, color):
        self.color = color
        print(f"Shape initialized with color: {self.color}")

    def calculate_area(self):
        print("Calculating area in Shape class (default implementation)")
        return 0

class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        super().calculate_area()
        print("Calculating area in Rectangle class")
        return self.width * self.height
rectangle = Rectangle(5, 10, "blue")
print(f"Rectangle area: {rectangle.calculate_area()}")