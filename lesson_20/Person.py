# Створіть клас Person, який має атрибути ім'я та вік, і метод вивести_інформацію,
# який виводить інформацію про цю особу.

# Розширте клас Person, додавши метод привітатися, який виводить рядок з привітанням, використовуючи ім'я особи.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def about(self):
        print(f'Ім`я: {self.name}, вiк: {self.age} рiк/рокiв')

    def say_hello(self):
        print(f'Привiт, {self.name}!')


person1 = Person('Михайло', 25)

person1.about()
person1.say_hello()
