# Завдання: Видалення дублікатів зі списку
# Дано список чисел. Створіть список, де видалено всі дублікати чисел, за допомогою List Comprehension.
import random

nums = [random.randint(1, 21) for _ in range(10)]
unique_nums = list(set(nums))

print(f'Початковий список: {nums}')
print(f'Список з унiкальними числами: {unique_nums}')
