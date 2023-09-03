# Автоматичне виведення документації: Створіть декоратор, який буде автоматично додавати документацію з іншої функції.
from functools import wraps


def add_documentation(func_from):
    def decorator(func):
        if func_from.__doc__:
            func.__doc__ = func_from.__doc__

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


def default_doc():
    """Стандартна документацiя для створення нової функції."""


@add_documentation(default_doc)
def get_sum(*args):
    return sum(args)


print(get_sum(1, 2, 3))
print(get_sum.__doc__)
