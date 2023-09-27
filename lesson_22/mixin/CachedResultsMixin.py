class CachedResultsMixin:
    def __init__(self):
        self._cache = {}

    @staticmethod
    def cache(func):
        def wrapper(self, *args, **kwargs):
            key = (func, args, frozenset(kwargs.items()))

            if key not in self._cache:
                self._cache[key] = func(self, *args, **kwargs)

            return self._cache[key]
        return wrapper
    

class Operations(CachedResultsMixin):
    def __init__(self):
        super().__init__()

    @CachedResultsMixin.cache
    def fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)


operations = Operations()
print(operations.fibonacci(5))
