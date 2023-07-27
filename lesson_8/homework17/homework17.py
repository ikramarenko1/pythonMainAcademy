# Знайти найкоротший рядок у файлі
# Опис: Напишіть програму, яка зчитує файл і знаходить
# найкоротший рядок у ньому. Програма виводить на екран цей найкоротший рядок.
import os


def find_shortest_line(filename):
    filename = filename.lower().strip()

    with open(filename, 'r') as file:
        data = file.readlines()
        min_str = data[0]
        min_length = len(data[0])

        for line in data:
            if len(line) < min_length:
                min_str = line.strip()
                min_length = len(line)

        return min_str


print('Список доступних файлiв для знаходження найкоротшого рядка.\n')

for file in os.listdir():
    if 'txt' in file:
        print(file)

user_file = str(input('\nВведіть назву файлу в якому знайти найкоротший рядок: '))

print(find_shortest_line(user_file))