# Завантажте зображення з Інтернету за допомогою бібліотеки requests та збережіть його на диск.
import requests


def download_image_from_url(url, img_name):
    response = requests.get(url)

    try:
        response.raise_for_status()

        with open(img_name, 'wb') as file:
            file.write(response.content)

    except Exception as e:
        print(f'Виникла помилка при завантаженнi зображення: {e}')


photo_url = input('Введiть url для завантаження зображення: ')
img_name = input('Як назвати файл? ')

download_image_from_url(photo_url, img_name)
