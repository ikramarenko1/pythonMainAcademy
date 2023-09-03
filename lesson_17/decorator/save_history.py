# Збереження історії викликів: Напишіть декоратор, який буде зберігати історію викликів функції разом з аргументами.
def save_history(func):
    history = {}

    def wrapper(*args, **kwargs):
        func_info = {
            'name': func.__name__,
            'args': args,
            'kwargs': kwargs
        }

        history[func.__name__] = func_info

        try:
            result = func(*args, **kwargs)
            history[func.__name__]['result'] = 'success'

            return result, history

        except Exception as e:
            print(f'Виникла помилка при виконаннi функції "{func.__name__}": {e}')
            history[func.__name__]['result'] = 'mistake'
            result = None

            return result, history

    return wrapper


@save_history
def get_sum(*args):
    return sum(args)


print(get_sum(1, 2, 3, 4))
print(get_sum(1, 2, '3', 4))
