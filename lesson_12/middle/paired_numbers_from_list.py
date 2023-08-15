# Завдання: Генерація пар чисел зі списку
# Дано список чисел. Створіть список, який містить всі можливі пари чисел з початкового списку,
# де перше число менше другого.

nums = [12, 36, 2, 6]
pairs = [(num1, num2) for i, num1 in enumerate(nums) for num2 in nums[i + 1:] if num1 < num2]

print(pairs)
