# Реалізуйте рекурсивну функцію для обчислення чисел Фібоначчі.
def fibonacci(n):
    if n < 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


user_input = int(input('Введiть кiлькiсть чисел Фібоначчі: '))

print(fibonacci(user_input))
