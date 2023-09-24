# Обробка HTTP-запитів: Створіть клас для роботи з HTTP-запитами і класовий метод для виконання GET-запитів.
import requests


class HttpRequest:
    @classmethod
    def execute_get_request(cls, url, params=None):
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


url = 'https://api.example.com/data'
params = {'param1': 'value1', 'param2': 'value2'}

response_data = HttpRequest.execute_get_request(url, params=params)
print(response_data)
