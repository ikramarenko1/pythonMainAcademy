# Напишіть рекурсивну функцію для обчислення добутку елементів списку.

def get_multiplication_of_elements(lst):
    if len(lst) == 0:
        return 1

    return lst[0] * get_multiplication_of_elements(lst[1:])


user_input = list(map(int, input('Введiть список чисел через пробiл: ').split()))

print(get_multiplication_of_elements(user_input))
