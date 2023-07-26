# Завдання: Об'єднати вміст декількох файлів
# Опис: Напишіть програму, яка об'єднує вміст трьох файлів "file1.txt",
# "file2.txt" і "file3.txt" і записує його в новий файл "merged.txt".
import os

files = 0

for file in os.listdir():
    if file[:4] == "file":
        files += 1

with open('merged.txt', 'w') as merged:
    for i in range(1, files + 1):
        with open(f'file{i}.txt', 'r') as file:
            merged.write(file.read())
            merged.write('\n')