# Завдання: Фільтрація списку чисел за парність
# Дано список чисел. Створіть список, що містить тільки парні числа з вихідного списку, за допомогою List Comprehension.
import random

nums = [random.randint(1, 21) for _ in range(10)]
paired_nums = [num for num in nums if num % 2 == 0]

print(f'Початковий список: {nums}')
print(f'Список лише з парними числами: {paired_nums}')
