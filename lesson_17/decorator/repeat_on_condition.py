# Повторне виконання функції: Напишіть декоратор, який дозволить автоматично повторювати
# виконання функції при певних умовах.
import random


def repeat_on_condition(condition, retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retries):
                result = func(*args, **kwargs)

                print(f'Спроба № {i + 1}/{retries}: {result}')

                if condition(result):
                    break

            return result
        return wrapper
    return decorator


def condition(result):
    return result < 5


@repeat_on_condition(condition, 5)
def guess_num():
    return random.randint(1, 10)


print(guess_num())
