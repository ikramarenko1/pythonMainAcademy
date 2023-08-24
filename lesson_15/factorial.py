# Задача з функціями: Створіть функцію для обчислення факторіала заданого числа.
def factorial(n):
    if n == 1:
        return n

    return n * factorial(n - 1)


user_input = int(input('Введiть число для обчислення факторiалу: '))
print(factorial(user_input))
