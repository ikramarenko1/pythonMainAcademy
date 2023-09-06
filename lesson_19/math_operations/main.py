# Напишіть програму, яка приймає від користувача два числа та вибір операції (додавання, віднімання, множення, ділення).
# Виконайте вибрану операцію та виведіть результат.
import math_operations as my_math


def get_result(a, b, action):
    if action == '+':
        return my_math.add(a, b)

    elif action == '-':
        return my_math.subtract(a, b)

    elif action == '*':
        return my_math.multiply(a, b)

    elif action == '/':
        return my_math.divide(a, b)

    else:
        return 'Невiдома функцiя, повторiть введення.'


a = float(input('Введiть перше число: '))
b = float(input('Введiть друге число: '))
action = input('Введiть дiю мiж числами: ')

try:
    result = get_result(a, b, action)
    print(f'Результат виконання {a} {action} {b} = {result}')

except Exception as e:
    print(f'Виникла помилка при виконаннi функції get_result: {e}')
