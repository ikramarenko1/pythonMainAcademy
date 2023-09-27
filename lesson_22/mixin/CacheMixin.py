# Реалізація кешування запитів до веб-сервісу:
# Розробіть мікс, який дозволить кешувати результати запитів до веб-сервісу,
# щоб зменшити навантаження на сервер та покращити швидкість відповідей.
import hashlib
import json
import time


class CacheMixin:
    def __init__(self):
        self._cache = {}
        self._cache_expiration = 60

    def cache_request(self, func):
        def wrapper(*args, **kwargs):
            key_data = {
                "args": args,
                "kwargs": kwargs
            }
            key = hashlib.sha256(json.dumps(key_data, sort_keys=True).encode()).hexdigest()

            # Перевірка наявності результату у кеші
            if key in self._cache:
                timestamp, result = self._cache[key]
                # Перевірка актуальності кешу
                if time.time() - timestamp < self._cache_expiration:
                    return result

                else:
                    print("Термін дії кешу закінчився")

            result = func(*args, **kwargs)
            self._cache[key] = (time.time(), result)

            return result

        return wrapper


class WebServiceClient(CacheMixin):
    def __init__(self):
        super().__init__()

    @CacheMixin.cache_request
    def make_request(self, endpoint, params):
        print("Робимо запрос до", endpoint, "з параметрами", params)

        # Тут виконується запит до веб-сервісу
        time.sleep(2)

        return {"data": "response"}


client = WebServiceClient()

response = client.make_request("/api/data", {"param": "value"})
print(response)
