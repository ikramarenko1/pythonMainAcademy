# Завдання: Пошук відмінних ознак у списку словників
# Дано список словників, кожен з яких представляє товар із назвою, ціною та вагою.
# Знайдіть товари, де ціна вища за середню ціну, а вага нижча за середню вагу.

products = [
    {"name": "apple", "price": 13, "weight": 4},
    {"name": "banana", "price": 14, "weight": 7},
    {"name": "orange", "price": 20, "weight": 2},
    {"name": "milk", "price": 25, "weight": 3}
]

total_price = sum(product['price'] for product in products)
average_price = total_price // len(products)

total_weight = sum(product['weight'] for product in products)
average_weight = total_weight // len(products)

result_products = [
    product for product in products
    if product['price'] > average_price and product['weight'] < average_weight
]

print(f'Середня цiна: {average_price}')
print(f'Середня вага: {average_weight}')
print(result_products)
