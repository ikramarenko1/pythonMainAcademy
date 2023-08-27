# Створіть рекурсивну функцію для знаходження найбільшого елемента в списку.

def get_largest_num(numbers):
    if len(numbers) == 1:
        return numbers[0]

    return max(numbers[0], get_largest_num(numbers[1:]))


numbers = [1, 4, 5, 3, 4, -1, 21, 4]

print(get_largest_num(numbers))
