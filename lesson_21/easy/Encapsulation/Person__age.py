# Створіть клас Person, у якому інкапсульовано приватну змінну age.
# Напишіть методи get_age() та set_age(), які дозволяють отримувати та встановлювати вік об'єкта.
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__age = value
                print(f'Вiк {self.name} змiнено на {value} рокiв.')
            else:
                print('Кiлькiсть повинна бути бiльше 0.')
        else:
            print(f'{value} повинно бути числом.')


ilya = Person('Ilya')

ilya.set_age(20)
print(f'Вiк {ilya.name} - {ilya.get_age()} рокiв.')
