# Перевірка правильності реалізації функції: Напишіть декоратор, який буде перевіряти,
# чи функція повертає правильний результат.
def check_correctness(expected):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if result == expected:
                print(f'УСПIХ: Функцiя {func.__name__} повернула очiкуваний результат!')
            else:
                print(f'ПОМИЛКА: Функцiя {func.__name__} повернула неочiкуваний результат!')

            return result
        return wrapper
    return decorator


@check_correctness(5)
def get_sum(a, b):
    return a + b


print(get_sum(3, 2))
print(get_sum(3, 3))
