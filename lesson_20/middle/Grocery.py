# Магазин продуктів: Створіть клас "Товар", який має атрибути назва, ціна та кількість.
# Напишіть метод, який обчислює загальну вартість товару (ціна * кількість).
class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f'Продукт "{self.name}":\n' \
               f'    Цiна: {self.price} у.о.\n' \
               f'    Кiлькiсть: {self.count} шт.'

    def get_total_cost(self):
        return f'Загальна вартiсть продукту {self.name} = {self.price * self.count} у.о.'


apples = Product('Яблука', 2, 325)
milk = Product('Молоко', 7, 39)

print(apples)
print(apples.get_total_cost())

print(milk)
print(milk.get_total_cost())
