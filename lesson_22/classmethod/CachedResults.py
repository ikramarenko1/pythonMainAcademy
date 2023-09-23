# Робота з кешем: Реалізуйте класовий метод для кешування результатів дорогообчислюваних функцій.
class CachedResults:
    cache_dict = {}

    @classmethod
    def cache(cls, func):
        def wrapper(*args, **kwargs):
            key = (func, args, frozenset(kwargs.items()))

            if key not in cls.cache_dict:
                cls.cache_dict[key] = func(*args, **kwargs)

            return cls.cache_dict[key]
        return wrapper


@CachedResults.cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(5))
