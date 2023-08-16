# Завдання: Групування товарів за ціновими діапазонами
# Дано словник з товарами та їх цінами. Створіть словник, де ключами будуть діапазони цін
# (наприклад, 0-10, 11-20, тощо), а значеннями - список товарів, що відповідають цим діапазонам.

products = {
    'apple': 9,
    'banana': 13,
    'orange': 11,
    'watermelon': 29,
    'strawberry': 23,
    'milk': 10,
    'bread': 3,
    'eggs': 6,
    'cheese': 32,
    'chicken': 47,
    'pasta': 31,
    'rice': 24,
    'sugar': 4,
    'salt': 1,
    'coffee': 20,
    'tea': 15,
}
ranges = ['0-10', '11-20', '21-30', '31-40', '41-50']
products_by_ranges = {range: [] for range in ranges}

for product, price in products.items():
    for range_str in ranges:
        min_price, max_price = map(int, range_str.split('-'))

        if min_price <= price <= max_price:
            products_by_ranges[range_str].append(product)

print(products_by_ranges)
