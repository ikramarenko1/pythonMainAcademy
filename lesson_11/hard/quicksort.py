# Реалізація алгоритму сортування QuickSort:
# QuickSort - це швидкий алгоритм сортування, який використовує рекурсію.
# У цій задачі ми розбиваємо масив на менші частини за допомогою опорного елементу (пивота) і рекурсивно сортуємо ці підмасиви.

def quicksort(nums):
    if len(nums) <= 1:
        return nums

    elem = nums[len(nums) // 2]

    left = [x for x in nums if x < elem]
    middle = [x for x in nums if x == elem]
    right = [x for x in nums if x > elem]

    return quicksort(left) + middle + quicksort(right)


nums_list = [12, 3, 54, 12, 56, 8, 97, 23]
print(quicksort(nums_list))
