# Задача зі списками: Напишіть функцію, яка приймає список чисел і повертає
# новий список, де елементи впорядковані за зростанням.
def get_new_list(*args):
    return sorted(args)


user_input = map(int, input('Введiть список чисел через пробiл для тесту: ').split())

print(f'Результат: {get_new_list(*user_input)}')
