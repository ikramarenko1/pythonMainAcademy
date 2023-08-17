# Завдання: Визначення спільних дільників для списку чисел
# Дано список чисел. Створіть список всіх спільних дільників для цих чисел, використовуючи Set Comprehension.
def get_common_divisors(numbers):
    def divisors(num):
        return {i for i in range(1, num + 1) if num % i == 0}

    common_divisors = divisors(numbers[0])

    for num in numbers[1:]:
        common_divisors = common_divisors & divisors(num)
    return common_divisors


numbers = [21,49,56]
common_divisors = get_common_divisors(numbers)

print(common_divisors)
