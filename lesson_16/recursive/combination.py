# Створіть рекурсивну функцію для обчислення числа комбінацій C(n, k).
def combination(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return combination(n - 1, k - 1) + combination(n - 1, k)


num1 = int(input('Введiть число 1: '))
num2 = int(input('Введiть число 2: '))

print(combination(num1, num2))
