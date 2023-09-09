# Парковка автомобілів: Створіть клас для керування парковкою автомобілів з можливістю
# додавання, видалення та пошуку автомобілів.
class Parking:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def __str__(self):
        return f'============\n' \
               f'Паркiнг "{self.name}":\n' \
               f'Автомобiлi:\n' + '\n'.join([car.model for car in self.cars]) + '\n============'

    def add(self, car):
        self.cars.append(car)
        print(f'Авто {car.model} успiшно додано до парковки "{self.name}"!')

    def remove(self, car):
        self.cars.remove(car)
        print(f'Авто {car.model} успiшно видалено з парковки "{self.name}"!')

    def search(self, car):
        if car in self.cars:
            print(f'Авто {car.model} успiшно знайдено на парковцi!')
        else:
            print(f'Авто {car.model} не знайдено на парковцi!')


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'Інформація про автомобіль:\n   Модель: {self.model}\n   Рiк випуску: {self.year}\n   Колiр: {self.color}'


audi = Car('Audi RS5 Coupe', '2022', 'Space Grey')
mercedes = Car('Mercedes-Benz c63', '2021', 'White')
parking = Parking('Парковка №231')

parking.add(audi)
parking.add(mercedes)

print(parking)

parking.remove(mercedes)

print('----' * 3)

parking.search(audi)
parking.search(mercedes)