# Обробка спеціальних станів: Створіть декоратор, який буде обробляти спеціальні стани під час виконання функції.
def handle_special_states(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            if result is None:
                print(f"УВАГА: Функція {func.__name__} повернула None.")
            elif isinstance(result, (int, float)) and result < 0:
                print(f"УВАГА: Функція {func.__name__} повернула негативне значення.")

            return result

        except ZeroDivisionError:
            print(f"ПОМИЛКА: Функція {func.__name__} повернула помилку: на 0 ділити не можна!")
            return None
        except Exception as e:
            print(f"ПОМИЛКА: Функція {func.__name__} повернула помилку:: {e}")
            return None

    return wrapper


@handle_special_states
def division(a, b):
    return a / b


@handle_special_states
def return_none():
    return None


print(division(4, 2))
print(division(4, 0))
print(return_none())


