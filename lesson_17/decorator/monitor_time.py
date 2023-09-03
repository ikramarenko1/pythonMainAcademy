# Моніторинг часу виконання: Напишіть декоратор, який буде вимірювати час виконання функції і виводити його.
import time


def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f'Час виконання функції {func.__name__} - {end_time - start_time} секунд')

        return result

    return wrapper


@get_time
def sleep(n):
    time.sleep(n)
    print('Я виспався!')


sleep(3)
