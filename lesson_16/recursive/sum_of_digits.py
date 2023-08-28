# Реалізуйте рекурсивну функцію для обчислення суми цифр у заданому числі.
def get_sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return num % 10 + get_sum_of_digits(num // 10)


user_input = int(input('Введiть число для обчислення суми його цифр: '))

print(f'Сума цифр в числi {user_input}: {get_sum_of_digits(user_input)}.')