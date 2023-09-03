# Перевірка прав доступу: Створіть декоратор для перевірки прав доступу користувача до функції.
def check_access_rights(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # За замовчуванням 'guest'
            user_role = kwargs.get('user_role', 'guest')

            if user_role != role:
                print(f'Доступ відхилено за правами доступу.')
                return None

            result = func(*args, **kwargs)

            return result
        return wrapper
    return decorator


@check_access_rights('admin')
def get_sum(*args, user_role='guest'):
    return sum(args)


sum1 = get_sum(1, 2, user_role='admin')
print(sum1)

sum2 = get_sum(1, 3, user_role='user')
print(sum2)
