# Пошук найбільшого числа: Напишіть функцію, яка приймає список чисел і повертає
# найбільше з них.

def get_largest_num(*args):
    return max(args)


print(get_largest_num(1, 2, 3, 4, 5))
