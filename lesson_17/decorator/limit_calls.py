# Обмеження кількості викликів: Напишіть декоратор, який буде обмежувати кількість викликів функції.
def limit_calls(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        limit = 3

        if calls >= limit:
            print(f'Виконання функції {func.__name__} з параметрами {args}, {kwargs} неможливе. '
                  f'Перевищенно лiмiт в використаннi')

            return None

        result = func(*args, **kwargs)
        calls += 1

        print(f'Виконання функції {func.__name__} з параметрами {args}, {kwargs}.')

        return result

    return wrapper


@limit_calls
def get_sum(*args):
    return sum(args)


sum1 = get_sum(1, 2, 3)
print(sum1)

sum2 = get_sum(1, 2, 3)
print(sum2)

sum3 = get_sum(2, 3, 8)
print(sum3)

sum4 = get_sum(1, 2, 3)
print(sum4)
