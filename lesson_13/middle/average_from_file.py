# Обчислення середнього: Напишіть програму, яка обчислює середнє арифметичне чисел з файлу
# "numbers.txt". Обробте випадок, коли файл не знайдено, і виведіть повідомлення "Файл не існує".
import random

with open('numbers.txt', 'w') as file:
    file.write(f'{random.randint(1, 21)}')

    for _ in range(9):
        file.write(f'\n{random.randint(1, 21)}')

try:
    with open('numbers.txt', 'r') as file:
        data = file.read()
        numbers = list(map(int, data.split('\n')))
        average = sum(numbers) / len(numbers)

        print(f'Числа з файлу: {numbers}')
        print(f'Середнє арифметичне чисел - {average}')

except FileNotFoundError:
    print('Файл не існує')
except Exception as e:
    print(e)
