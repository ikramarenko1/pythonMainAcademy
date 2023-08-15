# Реалізація алгоритму сортування за допомогою злиття (Merge Sort):
# Злиття - це алгоритм сортування, який базується на розділенні масиву на підмасиви,
# сортуванні їх окремо та об'єднанні відсортованих підмасивів. Ми використовуємо
# цикли для розділення та злиття підмасивів.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1

        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]

    return result


nums = [13, 52, 54, 76, 78, 23, 0, 19, 50]
print(merge_sort(nums))
