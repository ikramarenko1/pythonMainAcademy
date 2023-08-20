# Пошук файлів: Створіть програму, яка шукає всі файли з розширенням ".txt" у вказаній директорії.
# Виведіть на екран список знайдених файлів. Обробте випадок, коли директорія не існує, і виведіть
# повідомлення "Директорія не знайдена".
import os


def find_files_in_directory(directory):
    try:
        for file in os.listdir(directory):
            if file.endswith('.txt'):
                print(f' - {file}')

    except FileNotFoundError:
        print(f'Директорія {directory} не знайдена.')
    except IsADirectoryError:
        print(f'{directory} не є директорією.')
    except Exception as e:
        print(f'Виникла помилка: {e}')


user_input = input('Введiть назву директорії: ')
find_files_in_directory(user_input)
