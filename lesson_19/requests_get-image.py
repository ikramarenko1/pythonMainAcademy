# Завантажте зображення з Інтернету за допомогою бібліотеки requests та відобразіть його на екрані.
import requests
import io
from PIL import Image


def get_image_from_url(url):
    try:
        response = requests.get(url)

        data = io.BytesIO(response.content)
        image = Image.open(data)

        image.show()
    except Exception as e:
        print(f'Виникла помилка при вiдображеннi зображення: {e}')


photo_url = input('Введiть url для зображення: ')

get_image_from_url(photo_url)
