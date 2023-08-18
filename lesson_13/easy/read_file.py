# Читання файлу: Напишіть програму, яка читає вміст файлу, назва якого
# вводиться користувачем. Обробте випадок, коли файл не існує.
import os

print('Файли в поточнiй директорії:')
for file in os.listdir():
    if file.endswith('.txt'):
        print(f' - {file}')

filename = str(input('\nВведiть назву файлу для зчитування інформації: '))

try:
    with open(filename, 'r') as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print(f'Файл не знайдено.')
