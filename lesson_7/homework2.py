# Завдання 2: Видалення елементу зі словника
# Опис: Напишіть програму, яка приймає словник (dictionary) і видаляє елемент за певним ключем (key).
# Використайте цю програму, щоб видалити елемент зі словника.

def del_element(dictionary, key):
    del dictionary[key]


fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}

del_element(fruits, 'banana')

print(fruits)
