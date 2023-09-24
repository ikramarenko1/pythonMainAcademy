# Створення замовлення: Реалізуйте клас Order і класовий метод для створення нового замовлення в інтернет-магазині.
# item_name: TEST, price: 10000, quantity: 1
class Order:
    id = 1

    def __init__(self, customer, items):
        self.id = Order.id
        self.customer = customer
        self.items = items
        self.total = sum(item['price'] * item['quantity'] for item in items)

    def __str__(self):
        return f'Замовлення #{self.id}:\n' \
               f'  - Замовник: {self.customer}\n' \
               f'  - Товари: ' + ", ".join(f'{item["name"]} - {item["quantity"]} шт.' for item in self.items) + '\n' \
               f'  - Загальна вартiсть = {self.total} у.о.'

    @classmethod
    def create(cls, customer, items):
        return cls(customer, items)


my_order = Order.create('Ilya', [
    {'name': 'Macbook Pro M1', 'price': 60000, 'quantity': 1},
    {'name': 'Airpods Max', 'price': 20000, 'quantity': 2},
    {'name': 'Hator Keyboard', 'price': 2499, 'quantity': 1}
])

print(my_order)
