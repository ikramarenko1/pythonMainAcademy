# Створення екземпляру з іменованими параметрами: Реалізуйте класовий метод для створення
# екземпляру класу з іменованими параметрами.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f'{self.name}, {self.age} рокiв, {self.city}'

    @classmethod
    def create(cls, **kwargs):
        return cls(
            name=kwargs.get('name', 'Unknown?'),
            age=kwargs.get('age', 1),
            city=kwargs.get('city', 'Unknown?')
        )


ilya = Person.create(name='Ilya', age='20', city='Kyiv')
person = Person.create(age=18)

print(repr(ilya))
print(repr(person))
