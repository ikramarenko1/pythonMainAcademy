# Пошук простого числа N:
# Попросіть користувача ввести число N і знайдіть N-те просте число.

def is_simple(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_nth_prime(n):
    count = 0
    num = 2

    while True:
        if is_simple(num):
            count += 1

            if count == n:
                return num

        num += 1


n = int(input('Введiть номер простого числа, яке хочете знайти: '))

print(f'{n}-е просте число - {get_nth_prime(n)}')