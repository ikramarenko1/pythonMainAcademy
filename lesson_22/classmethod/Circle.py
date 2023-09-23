# Створення круга з радіусом: Створіть клас Circle з параметром радіусу
# та класовим методом для створення круга з цим радіусом.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def create(cls, radius):
        return cls(radius)

    def area(self):
        return f'Площа круга з радiусом {self.radius} = {3.14 * self.radius * self.radius}'


circle = Circle.create(5)

print(circle.area())
