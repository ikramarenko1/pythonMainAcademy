# Використовуючи бібліотеку requests, виведіть на екран вміст сторінки "https://www.example.com".
import requests


response = requests.get('https://www.example.com')

if response.status_code == 200:
    print(response.text)
else:
    print('Виникла помилка при вiдправцi запросу на сайт.')
