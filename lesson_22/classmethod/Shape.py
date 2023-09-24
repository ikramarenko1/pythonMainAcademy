# Фабрика об'єктів: Створіть клас Shape з класовим методом для створення
# об'єктів різних геометричних фігур (круг, прямокутник, трикутник).
class Shape:
    def __init__(self, name, **characteristics):
        self.name = name
        self.characteristics = characteristics

    @property
    def documentation(self):
        doc = f'Назва: {self.name}\n'
        doc += 'Характеристики:\n'
        for key, value in self.characteristics.items():
            doc += f'  - {key}: {value}\n'

        return doc

    @classmethod
    def create_shape(cls, shape_type, *args):
        shapes = {
            'circle': Circle,
            'rectangle': Rectangle,
            'triangle': Triangle
        }
        return shapes[shape_type](*args)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


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


# Використання класу Shape для створення об'єктів різних фігур
circle = Shape.create_shape('circle', 5)
print(f'- Площа круга: {circle.area()}')

rectangle = Shape.create_shape('rectangle', 10, 5)
print(f'- Площа прямокутника: {rectangle.area()}')

triangle = Shape.create_shape('triangle', 10, 5)
print(f'- Площа трикутника {triangle.area()}')

circle_doc = Shape('Circle', radius=25)
rectangle_doc = Shape('Rectangle', width=10, height=5)

print(circle_doc.documentation)
print(rectangle_doc.documentation)
