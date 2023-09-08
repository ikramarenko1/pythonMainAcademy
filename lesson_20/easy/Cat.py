# Створіть клас Кот, який має атрибути ім'я і вік. Додайте метод привітатися,
# який виводить рядок з привітанням, використовуючи ім'я кота.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Котик з iм`ям {self.name}. {self.age} рокiв.'

    def say_hello(self):
        print(f'З Вами вітається котик за ім`ям {self.name}: "Мяяяяуууу! Мррррр мяяяяууу!"')


ryzhik = Cat('Рижик', 2)

print(ryzhik)
ryzhik.say_hello()
