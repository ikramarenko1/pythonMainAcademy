# Інтернет-магазин: Реалізуйте структуру для інтернет-магазину з можливістю додавання товарів до корзини,
# обчислення загальної вартості та оформлення замовлення.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Товар "{self.name}", {self.price} у.о.'


class Cart:
    def __init__(self):
        self.products = {}

    def __str__(self):
        return f'В корзинi:\n' + '\n'.join([f"{product.name}: {count} шт." for product, count in self.products.items()])

    def add(self, product, count=1):
        if product in self.products:
            self.products[product] += count
            print(f'Товар "{product.name}" додано до кошика! Загальна кiлькiсть: {self.products[product]} шт.')
        else:
            self.products[product] = count
            print(f'Товар "{product.name}" додано до кошика у кiлькостi {self.products[product]} шт!')

    def remove(self, product):
        if product in self.products:
            del self.products[product]
            print(f'Товар "{product.name}" видалено з кошика!')
        else:
            print(f'Товару "{product.name}" не було знайдено в кошику.')

    def get_total_cost(self):
        return sum(product.price * count for product, count in self.products.items())


class Order:
    def __init__(self, cart):
        self.cart = cart

    def make_order(self):
        total = self.cart.get_total_cost()
        print(f'Дякуємо! Замовлення на суму {total} у.о. було успiшно оформлене!')


apples = Product('Яблуко', 24)
bananas = Product('Банан', 49)
bread = Product('Хлiб', 23)
milk = Product('Молоко', 33)
rice = Product('Рис', 43)
water = Product('Вода', 19)

cart = Cart()

cart.add(apples, 4)
cart.add(bananas, 2)
cart.add(bread)
cart.add(water, 6)

print(cart)

cart.remove(bananas)

print(cart)

order = Order(cart)

order.make_order()
