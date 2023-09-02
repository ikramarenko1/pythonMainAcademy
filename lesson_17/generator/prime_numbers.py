# Прості числа: Реалізуйте генератор для генерації послідовності простих чисел.
def generate_prime():
    n = 2

    while True:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break

        else:
            yield n

        n += 1


prime_numbers = generate_prime()

for _ in range(5):
    print(next(prime_numbers))
