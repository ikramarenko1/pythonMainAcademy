# Задача зі списками: Реалізуйте функцію, яка приймає список чисел і повертає список,
# де кожне число підняте до квадрату.

def list_to_square(*args):
    return [num ** 2 for num in args]


user_input = map(int, input('Введiть список чисел через пробiл для тесту: ').split())

print(f'Результат: {list_to_square(*user_input)}')
