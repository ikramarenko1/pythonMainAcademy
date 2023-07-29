# Читання та обробка файлу: Створіть текстовий файл "data.txt", де кожен рядок містить число.
# Зчитайте ці числа з файлу, обчисліть їх середнє значення та виведіть на екран.
import random

with open('data.txt', 'w') as file:
    for _ in range(10):
        file.write(f'{str(random.randint(1, 25))}\n')

with open('data.txt', 'r') as file:
    data = file.read().splitlines()
    nums = []

    for i in range(len(data)):
        nums.append(int(data[i]))

    print(f'Середнє значення - {sum(nums) / len(nums)}')
