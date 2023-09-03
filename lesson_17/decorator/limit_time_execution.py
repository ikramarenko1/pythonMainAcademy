# Вимірювання виконання з обмеженням часу: Створіть декоратор, який вимірює час виконання
# функції, але при цьому обмежує час виконання.
import time


def limit_time_execution(max_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            elapsed_time = end_time - start_time

            if elapsed_time > max_time:
                print(f'Виконання функції {func.__name__} перевищує лiмiт допустимого часу.')
                return None

            print(f'Виконання функції {func.__name__} заняло {elapsed_time} секунд.')

            return result
        return wrapper
    return decorator


@limit_time_execution(1)
def more_sleep():
    time.sleep(2)
    return 'Я виспався!'


@limit_time_execution(1)
def less_sleep():
    time.sleep(0.5)
    return 'Хочу ще 5 хвилиночок..'


print(more_sleep())
print(less_sleep())
