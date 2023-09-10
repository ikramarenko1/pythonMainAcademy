# Кошик: Створіть клас "Кошик", який може містити товари (об'єкти класу Товар).
# Додайте метод для обчислення загальної вартості всіх товарів у кошику.
class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f'Товар {self.name}:\n   Цiна: {self.price} у.о.\n   Кiлькiсть: {self.count}'

    def get_total_cost(self):
        return f'Загальна вартiсть продукту {self.name} = {self.price * self.count} у.о.'


class Cart:
    def __init__(self):
        self.products = []

    def __str__(self):
        return 'Товари в кошику: ' + ', '.join([str(product) for product in self.products])

    def add(self, product):
        print(f'Товар {product.name} успiшно додано до кошику!')
        self.products.append(product)

    def remove(self, product):
        print(f'Товар {product.name} успiшно видалено з кошика!')
        self.products.remove(product)

    def get_total_cost(self):
        return f'Загальна вартiсть товарiв у кошику = {sum([product.price * product.count for product in self.products])} у.о.'


apples = Product('Яблуко', 4, 3)
water = Product('Пляшка води', 6, 6)
rice = Product('Пачка рису', 1, 4)

cart = Cart()

print('----' * 3)
cart.add(apples)
print(cart)
print('----' * 3)

cart.add(water)
print(cart)
print('----' * 3)

cart.remove(water)
print(cart)
print('----' * 3)

cart.add(rice)
print(cart.get_total_cost())
print('----' * 3)