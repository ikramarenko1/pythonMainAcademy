# Створіть функцію animal_speak(animal), яка приймає об'єкт типу Animal та викликає метод speak().
# Використовуйте цю функцію для різних об'єктів Animal.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Метод speak() повинен бути реалiзованим у пiдкласах.")


class Dog(Animal):
    def speak(self):
        print(f'{self.name.upper()}: Wooof!')


class Cat(Animal):
    def speak(self):
        print(f'{self.name.upper()}: Meeeooow!')


def animal_speak(animal):
    if isinstance(animal, Animal):
        animal.speak()
    else:
        print(f'{animal} не тварина!')


dog = Dog('Белла')
cat = Cat('Персиваль')

dog.speak()
cat.speak()

print('----' * 3)

animal_speak(dog)
animal_speak(cat)
