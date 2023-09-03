# Логування виключень: Напишіть декоратор, який буде логувати виключення, якщо воно виникає в процесі виконання функції.
def logging_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Виникла помилка при виконаннi "{func.__name__}": {e}.')
            return None

    return wrapper


@logging_exceptions
def division(a, b):
    return a / b


print(division(4, 2))
print(division(4, 0))
print(division(4, '2'))
