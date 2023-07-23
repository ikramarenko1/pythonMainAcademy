# Завдання 15: Перевірити, чи є словник пустим
# Опис: Напишіть програму, яка приймає словник (dictionary) і перевіряє, чи є він пустим
# (не містить жодного елемента). Використайте цю програму, щоб перевірити, чи є словник пустим.

def if_empty(dictionary):
    return len(dictionary) == 0


fruits = {"apple": "red", "banana": "yellow", "orange": "orange", "grapes": "purple"}
empty_fruits = {}

print(if_empty(fruits))  # False
print(if_empty(empty_fruits))  # True
