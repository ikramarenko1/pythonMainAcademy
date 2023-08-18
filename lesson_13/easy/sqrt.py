# Обчислення кореня: Реалізуйте обчислення квадратного кореня числа, яке вводить
# користувач. Обробте можливі помилки, такі як введення від'ємного числа.
import math

num = input('Введiть число для обчислення квадратного кореня: ')

try:
    num = float(num)

    if num < 0:
        raise ValueError

    result = math.sqrt(num)

    print(result)
except ValueError:
    print('Введене число не коректне.')
