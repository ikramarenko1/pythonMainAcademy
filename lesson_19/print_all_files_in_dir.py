# Виведіть всі файлові розширення у поточному каталозі.
import os


def get_files_in_dir(path):
    extensions = []

    if os.listdir(path):
        print(path)
        for name in os.listdir(path):
            print(name)
            if os.path.isdir(name):

                print(f'Папка {name}:')
                print(f'{path}/{name}/')
                get_files_in_dir(f'{path}/{name}/')

            if os.path.isfile(name):
                # name = name.split('.')
                # extensions.append(f'.{name[1]}')
                extensions.append(name)

        # print(set(extensions))
        print(extensions)


get_files_in_dir(os.path.curdir)

