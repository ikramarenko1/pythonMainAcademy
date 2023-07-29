# Обчислення: Напишіть функцію, яка знаходить факторіал заданого числа N рекурсивно.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 120
print(factorial(6))  # 720
