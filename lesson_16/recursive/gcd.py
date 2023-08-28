# Напишіть рекурсивну функцію для обчислення найбільшого спільного дільника двох чисел.

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


num1 = int(input('Введiть число 1: '))
num2 = int(input('Введiть число 2: '))

print(gcd(num1, num2))
