# Створіть клас Автомобіль, який має атрибути модель, рік і колір. Виведіть інформацію про автомобіль.

# Розширте клас Автомобіль, додавши метод запустити, який виводить рядок про те, що автомобіль був запущений.
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'Інформація про автомобіль:\n   Модель: {self.model}\n   Рiк випуску: {self.year}\n   Колiр: {self.color}'

    def start_engine(self):
        print(f'Двигун автомобiля {self.model} був успiшно запущений!')


audi = Car('Audi RS5 Coupe', '2022', 'Space Grey')
mercedes = Car('Mercedes-Benz c63', '2021', 'White')

print(audi)
audi.start_engine()

print(mercedes)
mercedes.start_engine()
