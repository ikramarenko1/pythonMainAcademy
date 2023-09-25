# Інтерфейс для роботи з зовнішніми службами: Створіть клас для взаємодії з
# зовнішніми веб-сервісами. Використовуйте властивості для створення зручного
# інтерфейсу для відправки та отримання даних через API.
import requests


class ExternalService:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {}

    def _request(self, method, endpoint, data=None):
        url = '{}/{}'.format(self.base_url, endpoint)
        response = requests.request(method, url, headers=self.headers, data=data)
        response.raise_for_status()

        return response.json()

    @property
    def data(self):
        return self._request('GET', 'data')

    @data.setter
    def data(self, data):
        self._request('POST', 'data', data=data)


service = ExternalService('https://example.com')
print(service.data)

service.data = {'key': 'value'}
print(service.data)
