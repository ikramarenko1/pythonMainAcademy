# Знайти середню довжину рядків у файлі
# Опис: Напишіть програму, яка зчитує файл і знаходить середню довжину рядків
# у ньому. Програма виводить на екран середню довжину рядків.
import os


def average_len(filename):
    filename = filename.lower().strip()

    with open(filename, 'r') as file:
        data = file.readlines()
        sum_of_chars = 0

        for line in data:
            sum_of_chars += len(line)

        return round(sum_of_chars / len(data))


print('Список доступних файлiв для того, щоб знайти середню довжину рядків.\n')

for file in os.listdir():
    if 'txt' in file:
        print(file)

file_to_count = str(input('\nВведiть назву файла: '))

print(average_len(file_to_count))