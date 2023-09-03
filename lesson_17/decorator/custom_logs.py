# Кастомні логи: Створіть декоратор, який дозволить користувачу задавати кастомні повідомлення для логування.
def custom_logs(func):
    logs = {}

    def wrapper(*args, **kwargs):
        user_input = input('Введiть повідомлення для логування: ')

        func_log = {
            'name': func.__name__,
            'msg': user_input,
        }

        logs[func.__name__] = func_log

        try:
            result = func(*args, **kwargs)
            logs[func.__name__]['result'] = 'success'

            return result, logs

        except Exception as e:
            print(f'Функцiя {func.__name__} повернула помилку: {e}')
            result = None
            logs[func.__name__]['result'] = 'mistake'
            logs[func.__name__]['mistake'] = e

            return result, logs

    return wrapper


@custom_logs
def get_sum(*args):
    return sum(args)


print(get_sum(1, 2, 3))
print(get_sum(1, '2'))
