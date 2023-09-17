# Створіть клас Animal з методом speak().
# Створіть підкласи Dog та Cat, які успадковують Animal та реалізовують свої власні методи speak().
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


dog = Dog('Белла')
cat = Cat('Персиваль')

dog.speak()
cat.speak()
