# Перейменувати файл
# Опис: Напишіть програму, яка перейменовує файл.
# Користувач вводить початкову назву файлу та нову назву, і програма перейменовує файл.
import os

print('Список доступних файлiв для перейменування.\n')

for file in os.listdir():
    if 'txt' in file:
        print(file)

file_to_rename = str(input('\nВведiть файл для перейменування: '))
new_filename = str(input('Введiть нову назву файлу: '))

os.rename(file_to_rename, new_filename)
