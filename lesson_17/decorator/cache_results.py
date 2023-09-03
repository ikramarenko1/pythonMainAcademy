# Кешування результатів функції: Створіть декоратор, який буде кешувати результати функції для певних аргументів.
def cache_result(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print(f'Беру результат з кешу для функції {func.__name__} з аргументами {args}, {kwargs}')
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result

        print(f'Записую в кеш результат функції {func.__name__} з аргументами {args}, {kwargs}')

        return result

    return wrapper


@cache_result
def get_sum(*args):
    return sum(args)


sum1 = get_sum(1, 2, 3)
print(sum1)

sum2 = get_sum(1, 2, 3)
print(sum2)

sum3 = get_sum(2, 3, 8)
print(sum3)
