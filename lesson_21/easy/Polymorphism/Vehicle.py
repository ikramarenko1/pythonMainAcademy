# Створіть базовий клас Vehicle з методом drive().
# Створіть підкласи Car та Bike, які успадковують Vehicle та реалізовують свої методи drive().
# Створіть список з об'єктами обох типів транспорту та викличте метод drive() для кожного.
class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError(f'Метод drive() повинен бути реалiзований в пiдкласах')


class Car(Vehicle):
    def drive(self):
        print(f'{self.name.upper()}: Брррр... брум брум брум брум!')


class Bike(Vehicle):
    def drive(self):
        print(f'{self.name.upper()}: *звук педалей*')


vehicles = [
    Car('Audi RS5 Coupe'),
    Bike('Bike')
]

for vehicle in vehicles:
    vehicle.drive()
