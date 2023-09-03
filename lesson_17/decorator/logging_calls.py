# Логування викликів функцій: Створіть декоратор, який буде логувати виклики функцій разом з аргументами.
import time


def logging_calls(func):
    def wrapper(*args, **kwargs):
        print(f'Виклик функції {func.__name__} з параметрами {args}, {kwargs}.')
        result = func(*args, **kwargs)
        print(f'Функція {func.__name__} з параметрами {args}, {kwargs} завершила виконання.')

        return result

    return wrapper


@logging_calls
def sleep(n, string):
    time.sleep(n)
    print(string)


sleep(2, 'hello!')
