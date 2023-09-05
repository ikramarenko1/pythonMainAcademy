# Організація імпортів:
# Створіть кілька модулів у папці modules, кожен з яких містить функції для виконання певної операції
# (наприклад, math_operations.py, string_operations.py). Потім створіть головний файл main.py, де імпортується функції
# з цих модулів та використовується для обчислень.
from modules import math_operations
from modules import string_operations

print(math_operations.add(1, 2))
print(math_operations.subtract(43, 1))
print(math_operations.multiply(2, 4))
print(math_operations.divide(4, 2))

print('=====' * 3)

print(string_operations.reverse('hello!'))
print(string_operations.to_lowercase('hello!'))
print(string_operations.to_uppercase('hello!'))
