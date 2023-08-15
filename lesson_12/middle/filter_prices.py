# Завдання: Фільтрація словника за значенням
# Дано словник з цінами товарів. Створіть словник, який містить лише ті товари,
# ціна на які перевищує середню ціну всіх товарів.

goods = {
    'apple': 2,
    'banana': 3,
    'strawberry': 8,
    'cucumber': 4,
    'tomato': 4,
    'milk': 10,
    'water': 1,
    'juice': 5,
    'sausage': 7,
    'cheese': 10
}
average_price = sum(goods.values()) // len(goods)
goods_over_average = {name: price for name, price in goods.items() if price > average_price}

print(f'Середня цiна товарiв: {average_price}')
print(f'Новий словник: {goods_over_average}')
