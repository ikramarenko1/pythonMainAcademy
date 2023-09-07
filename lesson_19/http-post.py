# Виконайте HTTP-POST-запит до віддаленого сервера та виведіть відповідь на екран.
import requests


url = 'https://httpbin.org/post'
data = {
    'test_key1': 'test_value1',
    'test_key2': 'test_value2'
}

response = requests.post(url, data)

try:
    response.raise_for_status()
    print(f'Запит виконано успiшно! Результат:\n')
    print(response.text)

except requests.exceptions.HTTPError as e:
    print(f'Виникла помилка: {e}')
