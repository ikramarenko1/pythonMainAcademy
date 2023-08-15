# Завдання: Видалення найменших значень зі списку
# Дано список чисел. Створіть список, з якого видалено найменші значення, за допомогою List Comprehension.

nums = [2, 4, 7, 2, 23, 43, 97, 6]
nums_without_min = [num for num in nums if num != min(nums)]

print(nums_without_min)
