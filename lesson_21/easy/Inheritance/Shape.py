# Створіть базовий клас Shape, з методом area().
# Створіть підкласи Circle та Rectangle, які успадковують Shape та реалізовують власні методи area().
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


circle = Circle(5)
print(f'Площа кола: {circle.area()}')

rectangle = Rectangle(10, 5)
print(f'Площа прямокутника: {rectangle.area()}')
