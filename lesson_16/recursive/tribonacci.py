# Створіть рекурсивну функцію для знаходження n-го числа з послідовності Трібоначчі.
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


user_input = int(input('Введiть n-ий член послідовності Трібоначчі: '))

print(tribonacci(user_input))
