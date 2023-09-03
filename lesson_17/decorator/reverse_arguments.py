# Зміна порядку аргументів: Напишіть декоратор, який буде змінювати порядок аргументів функції.
def reverse_arguments(func):
    def wrapper(*args, **kwargs):
        return func(*reversed(args), **kwargs)

    return wrapper


@reverse_arguments
def print_arguments(a, b, c):
    print(f"1: {a}, 2: {b}, 3: {c}")


print_arguments(1, 2, 3)
