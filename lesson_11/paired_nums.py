# Підрахунок парних чисел: Знайти і вивести всі парні числа в заданому діапазоні.
import random

nums = []

for _ in range(10):
    nums.append(random.randint(1, 30))

paired_nums = [[num for num in nums if num % 2 == 0]]

print('Парнi числа: ', paired_nums)
