# Сортування списку: Напишіть функцію, яка сортує список чисел в
# порядку зростання або спадання.

def sort_list(numbers, descending=False):
    if descending:
        return sorted(numbers, reverse=True)

    return sorted(numbers)


user_input = list(map(int, input('Введiть список чисел через пробiл для сортування за зростанням та спаданням: ').split()))

# "*" для розпаковування map обʼєкта
print(sort_list(user_input))
print(sort_list(user_input, descending=True))
