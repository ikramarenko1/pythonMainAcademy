# Створіть базовий клас Animal з методом move().
# Створіть підкласи Bird, Fish, та Dog, які успадковують Animal та реалізовують свої методи move().
# Створіть список з різних типів тварин та викличте метод move() для кожного.
class Animal:
    def move(self):
        raise NotImplementedError("Метод move() повинен бути реалiзованим у пiдкласах.")


class Bird(Animal):
    def move(self):
        print(f'{type(self).__name__.upper()}: Пирх-пирх, пирх-пирх!')


class Fish(Animal):
    def move(self):
        print(f'{type(self).__name__.upper()}: Буль-буль-буль!')


class Dog(Animal):
    def move(self):
        print(f'{type(self).__name__.upper()}: Пх-пх-пх-пх-пх!')


animals = [
    Bird(),
    Fish(),
    Dog()
]

actions = [(type(animal).__name__, animal.move()) for animal in animals]
