# Створіть список об'єктів різних типів (наприклад, екземпляри Circle, Rectangle та Triangle).
# Використовуйте цей список для обчислення площі кожного об'єкта і друку результату.
import math


class Shape:
    def area(self):
        raise NotImplementedError("Метод area() повинен бути реалiзованим у пiдкласах.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Rectangle(10, 20),
    Triangle(10, 15)
]

area_results = []
for shape in shapes:
    area_results.append(f'Площа {type(shape).__name__} - {shape.area()}')

for area in area_results:
    print(area)
