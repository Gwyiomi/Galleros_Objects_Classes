import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = math.pi * self.radius ** 2
        print(f"The area of a circle is{circle_area: .2f}")

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of a circle is{circle_perimeter: .2f}")


radius_value = int(input("Enter a value for radius: "))
compute_circle = Circle(radius_value)

compute_circle.area()
compute_circle.perimeter()
