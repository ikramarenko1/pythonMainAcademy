# Завдання 1: Додавання елементу до словника
# Опис: Напишіть програму, яка приймає словник (dictionary) і додає новий елемент до нього.
# Новий елемент складається з ключа (key) і значення (value). Використайте цю програму, щоб
# додати новий елемент до словника.

def add_key_value(dictionary, key, value):
    dictionary[key] = value


fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}

add_key_value(fruits, 'grapes', 'purple')

print(fruits)
