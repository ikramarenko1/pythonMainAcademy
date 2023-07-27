# Видалити файл
# Опис: Напишіть програму, яка видаляє файл. Користувач вводить назву файлу, і програма видаляє цей файл.
import os

print('Список доступних файлiв для видалення.\n')

for file in os.listdir():
    if 'txt' in file:
        print(file)

file_to_del = str(input('\nВведiть файл для видалення: '))

os.remove(file_to_del)