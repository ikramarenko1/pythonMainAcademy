# Знаходження простих чисел до N:
# Попросіть користувача ввести число N і знайдіть всі прості числа, менші або рівні N.
def is_simple(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_simple_nums_by(n):
    simple_nums = []

    for num in range(n + 1):
        if is_simple(num):
            simple_nums.append(num)

    return simple_nums


n = int(input('Введiть число до якого потрiбно знайти простi числа: '))

print(get_simple_nums_by(n))

