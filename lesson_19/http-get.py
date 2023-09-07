# Виконайте HTTP-GET-запит до віддаленого сервера та виведіть заголовок відповіді на екран.
import requests


url = 'https://httpbin.org/get'

response = requests.get(url)

try:
    response.raise_for_status()
    print(f'Запит виконано успiшно! Результат:\n')
    print(response.headers)

except requests.exceptions.HTTPError as e:
    print(f'Виникла помилка: {e}')
