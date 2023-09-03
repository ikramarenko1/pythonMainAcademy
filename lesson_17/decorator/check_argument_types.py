# Перевірка типів аргументів: Створіть декоратор, який буде перевіряти, чи відповідають типи аргументів певному шаблону.
def check_argument_types(required_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if type(arg) != required_type:
                    print(f'Аргумент {arg} функції {func.__name__} повинен бути типу {required_type}, '
                          f'а функцiя отримала {type(arg)}.')
                    return None

            return func(*args, **kwargs)
        return wrapper
    return decorator


@check_argument_types(int)
def get_sum(*args):
    return sum(args)


print(get_sum(1, 2, 3))
print(get_sum(1, '2', 3))
print(get_sum(1, 2, 'hello'))

