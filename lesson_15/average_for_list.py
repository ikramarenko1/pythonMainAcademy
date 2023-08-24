# Задача зі списками: Створіть програму, яка обчислює середнє арифметичне значення списку чисел.

def get_average(*args):
    return sum(args) / len(args)


user_input = map(int, input('Введiть список чисел через пробiл для обчислення середнього арифметичного: ').split())

# "*" для розпаковування map обʼєкта
print(get_average(*user_input))
