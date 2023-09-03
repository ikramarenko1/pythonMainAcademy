# Обробка реініціалізації: Створіть декоратор, який буде обробляти реініціалізацію функції в певних умовах.
import time


def reinitialization(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                print('Роблю реініціалізацію функції..')
                print('Якісь дії..')

                time.sleep(1)

                func.__init__(*args, **kwargs)

            return func(*args, **kwargs)
        return wrapper
    return decorator


def condition(x):
    return x == 1


@reinitialization(condition)
def initialize(x):
    print(f'Роблю ініціалізацію з x = {x}')


initialize(1)
initialize(0)