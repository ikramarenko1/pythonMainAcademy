# Створіть клас Car, у якому зінкапсульовано приватну змінну fuel_level. Напишіть методи
# get_fuel_level() та add_fuel(), які дозволяють отримувати і змінювати це значення.
class Car:
    def __init__(self, name, fuel=0):
        self.name = name
        self.__fuel = fuel

    def get_fuel_level(self):
        return self.__fuel

    def add_fuel(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__fuel += value
                print(f'До автомобiля {self.name} додано бензина в розмiрi {value} л.')
            else:
                print('Кiлькiсть повинна перевищувати 0')
        else:
            print(f'{value} повинно бути числом!')


audi = Car('Audi RS5 Coupe')

audi.add_fuel(40)
print(f'Кiлькiсть бензина в {audi.name} - {audi.get_fuel_level()} л.')
