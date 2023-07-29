# Читання з файлу: Створіть функцію, яка зчитує числа з текстового
# файлу "numbers.txt", сортує їх у порядку спадання та записує в інший файл "sorted_numbers.txt".
import random

with open('numbers.txt', 'w') as file:
    for _ in range(20):
        file.write(f'{str(random.randint(1, 50))}\n')

with open('sorted_numbers.txt', 'w') as file_s:
    with open('numbers.txt', 'r') as file:
        data = file.read().split()

        data = sorted([int(num) for num in data], reverse=True)

        for i in range(len(data)):
            file_s.write(f'{str(data[i])}\n')

    print('Готово!')