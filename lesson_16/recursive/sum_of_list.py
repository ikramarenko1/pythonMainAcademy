# Напишіть рекурсивну функцію для підрахунку суми елементів списку.

def get_sum(numbers):
    if len(numbers) == 0:
        return 0

    result = numbers.pop()

    return result + get_sum(numbers)


numbers = [1, 2, 3, 4, 5]

print(get_sum(numbers))
