# Завдання: Злиття двох списків з унікальними значеннями
# Дано два списки чисел. Створіть список, що містить усі унікальні значення з обох списків.
import random

nums1 = [random.randint(1, 11) for _ in range(5)]
nums2 = [random.randint(1, 11) for _ in range(5)]

print(f'Список 1 - {nums1}')
print(f'Список 2 - {nums2}')
print(f'Список з унiкальними числами - {set(nums1 + nums2)}')