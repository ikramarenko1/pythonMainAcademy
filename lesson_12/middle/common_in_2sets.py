# Завдання: Знаходження спільних чисел у двох множинах
# Дано дві множини чисел. Створіть множину, яка містить числа, які зустрічаються і в першій, і в другій множині.
import random

nums1 = {random.randint(1, 11) for _ in range(10)}
nums2 = {random.randint(1, 11) for _ in range(10)}

result = {num for num in nums1 if num in nums2}

print(f'Множина 1 - {nums1}')
print(f'Множина 2 - {nums2}')
print(f'Множина, яка містить числа, які зустрічаються і в першій, і в другій множині - {result}')
