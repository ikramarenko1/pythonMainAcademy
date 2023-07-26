# Завдання: Знайти найбільший файл у директорії
# Опис: Напишіть програму, яка знаходить найбільший файл у поточній директорії та виводить його назву та розмір.
import os


def get_filesize(filename):
    return os.path.getsize(filename)


largest_size = 0
largest_filename = ''

for file in os.listdir():
    if os.path.isfile(file):
        if get_filesize(file) > largest_size:
            largest_size = get_filesize(file)
            largest_filename = file

print("Найбільший файл:", largest_filename)
print("Розмір:", largest_size, "байт")
