# Перевірка аргументів функції: Напишіть декоратор, який буде перевіряти, чи всі аргументи функції є числами.
def check_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                print(f'Аргумент {arg} повинен бути числом!')
                return None

        result = func(*args, **kwargs)

        return result

    return wrapper


@check_arguments
def get_sum(*args):
    return sum(args)


sum1 = get_sum(1, 2, 3)
print(sum1)

sum2 = get_sum(1, 'hello', 3)
print(sum2)
