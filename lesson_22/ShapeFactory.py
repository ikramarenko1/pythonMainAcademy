class Shape:
    def draw(self):
        raise NotImplementedError('Підкласи повинні реалізовувати цей метод')


class Circle(Shape):
    def draw(self):
        return 'Малюємо коло'


class Rectangle(Shape):
    def draw(self):
        return 'Малюємо прямокутник'


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == 'Circle':
            return Circle()
        elif shape_type == 'Rectangle':
            return Rectangle()
        else:
            raise ValueError(f'Тип фігури {shape_type} не розпізнано')


user_choice = input('Введіть тип фігури (Коло/Прямокутник): ')
shape = ShapeFactory.create_shape(user_choice)

print(shape.draw())
