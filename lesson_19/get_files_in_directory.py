# Виведіть всі файлові розширення у поточному каталозі.
import os


def get_files_in_directory(directory=".", tab=0):
    extensions = set()

    for item in os.listdir(directory):
        path = os.path.join(directory, item)

        if os.path.isdir(path):
            print('---' * tab + ('>' if tab > 0 else '') + f'Папка: {item}:')
            get_files_in_directory(path, tab + 1)

        else:
            item = item.split('.')
            name = item[0]
            extension = item[1]

            if extension:
                print('---' * tab + ('>' if tab > 0 else '') + f'Файл {name} з розширенням .{extension}')
                extensions.add(extension)
            else:
                print('---' * tab + ('>' if tab > 0 else '') + f'Файл {name}')


get_files_in_directory()
