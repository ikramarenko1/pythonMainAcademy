# Завдання: Генерація послідовності чисел
# Створіть список чисел від 1 до 20, пропустивши парні числа, за допомогою List Comprehension.

nums = [_ for _ in range(1, 21) if _ % 2 != 0]

print(nums)
