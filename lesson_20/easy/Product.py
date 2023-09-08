# Створіть клас Товар, який має атрибути назва, ціна і кількість. Виведіть інформацію про товар.

# Розширте клас Товар, додавши метод загальна_вартість, який обчислює загальну вартість товару (ціна * кількість).
class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f'Товар {self.name}:\n   Цiна: {self.price} у.о.\n   Кiлькiсть: {self.count}'

    def get_total_cost(self):
        return f'Загальна вартiсть продукту {self.name} = {self.price * self.count} у.о.'


apples = Product('Яблука', 2, 325)
milk = Product('Молоко', 7, 39)

print(apples)
print(apples.get_total_cost())

print(milk)
print(milk.get_total_cost())