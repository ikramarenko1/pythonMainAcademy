# Знайти кількість символів у файлі
# Опис: Напишіть програму, яка зчитує файл і підраховує кількість символів у ньому.
# Програма виводить на екран кількість символів.
import os


def count_symbols(filename):
    filename = filename.lower().strip()

    with open(filename, 'r') as file:
        data = file.readlines()
        cnt = 0

        for line in data:
            cnt += len(line)

        return cnt


print('Список доступних файлiв для зчитування кiлькостi символiв.\n')

for file in os.listdir():
    if 'txt' in file:
        print(file)

file_to_count = str(input('\nВведiть назву файла: '))

print(count_symbols(file_to_count))
