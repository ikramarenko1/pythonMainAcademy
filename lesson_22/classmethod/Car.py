# Контроль доступу до даних об'єкту: Створіть клас для представлення об'єкта, такого як автомобіль.
# Використовуйте властивість для контролю доступу до конфіденційної інформації, такої як номер двигуна.
class Car:
    def __init__(self, name, year, engine_number):
        self.name = name
        self.year = year
        self._engine_number = engine_number

    def __str__(self):
        return f'Iнформацiя про автомобiль:\n' \
               f'  - Назва: {self.name}\n' \
               f'  - Рiк випуску: {self.year}\n' \
               f'  - Двигун: {self.engine_number}'

    @property
    def engine_number(self):
        return 'Ця iнформацiя є конфiденцiйною.'

    @engine_number.setter
    def engine_number(self, value):
        self._engine_number = value

    def check_engine_number(self, value):
        return value == self._engine_number


audi = Car('Audi RS5 Coupe', '2022', 'CFSA')
print(audi)

print(audi.check_engine_number('CFSA'))
print(audi.check_engine_number('CFSA123'))
