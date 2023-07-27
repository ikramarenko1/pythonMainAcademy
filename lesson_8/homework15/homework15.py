# Вивести перші N рядків з файлу
# Опис: Напишіть програму, яка відкриває файл і виводить на екран перші N рядків.
# Користувач вводить N, і програма виводить перші N рядків з файлу.

def print_n_lines(filename, lines):
    with open(filename, 'r') as file:
        data = file.readlines()

        for i in range(lines):
            print(data[i].strip())


print_n_lines('merged.txt', 5)
