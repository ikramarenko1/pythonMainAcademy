# Реалізуйте рекурсивну функцію для обчислення числа степені.

def power(num, exponent):
    if exponent == 0:
        return 1

    return num * power(num, exponent - 1)


user_num = int(input('Введiть число для обчислення числа степені: '))
user_exponent = int(input('Введiть степінь для обчислення числа степені: '))

print(power(user_num, user_exponent))
