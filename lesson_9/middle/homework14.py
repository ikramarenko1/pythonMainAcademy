# Пошук у списку: Напишіть функцію для сортування списку чисел методом бульбашки (bubble sort).
import random


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


nums = []
for _ in range(1, 11):
    nums.append(random.randint(1, 100))

print(bubble_sort(nums))
