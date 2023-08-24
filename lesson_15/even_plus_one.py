# Задача зі списками: Реалізуйте функцію, яка приймає список чисел і повертає новий
# список, в якому всі парні числа збільшені на 1.
def get_list_even_plus_one(*args):
    return [num + 1 for num in args if num % 2 == 0]


user_input = map(int, input('Введiть список чисел через пробiл для тесту: ').split())

# "*" для розпаковування map обʼєкта
print(get_list_even_plus_one(*user_input))
