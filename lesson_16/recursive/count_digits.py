# Напишіть рекурсивну функцію для обчислення числа цифр у заданому числі.

def count_digits(num):
    if num == 0:
        return 0

    return 1 + count_digits(num // 10)


user_input = int(input('Введiть число для обчислення числа його цифр: '))

print(f'В числi {user_input}: {count_digits(user_input)} цифр.')
