# Завдання: Об'єднати значення словника в один рядок
# Опис: Напишіть програму, яка приймає словник (dictionary) з рядковими значеннями і
# об'єднує їх у один рядок без використання розгалужень або циклів.'
# Приклад вхідних даних: {"name": "John", "age": "25", "city": "New York"}
# Приклад вихідних даних: "John 25 New York"

user = {"name": "John", "age": "25", "city": "New York"}
print(' '.join(user.values()))
