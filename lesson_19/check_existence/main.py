# Створіть програму, яка перевіряє, чи існує файл або каталог з вказаним ім'ям у поточному каталозі.
import os
import time


def check_existence(name):
    print(f'Починаю пошук {name} в поточній директорії..')
    time.sleep(1)

    if os.path.exists(name):
        if os.path.isfile(name):
            print(f'Файл {name} існує в поточній директорії!')

        elif os.path.isdir(name):
            print(f'Каталог {name} існує в поточній директорії!')

    else:
        print('Вказаний файл/каталог не знайдений в поточній директорії.')


check_existence('file1.txt')
check_existence('dir1')
check_existence('file2.txt')
