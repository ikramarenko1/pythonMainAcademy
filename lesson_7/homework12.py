# Завдання 12: Перевірити наявність певного значення у словнику
# Опис: Напишіть програму, яка приймає словник (dictionary) і перевіряє, чи міститься певне значення
# (value) у цьому словнику. Використайте цю програму, щоб перевірити наявність певного значення у словнику.

def check_for_value(dictionary, value):
    return value in dictionary.values()


fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}

print(check_for_value(fruits, 'red'))  # True
print(check_for_value(fruits, 'purple'))  # False
