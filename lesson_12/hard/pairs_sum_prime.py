# Завдання: Генерація списку пар чисел з різницею від 1 до 5
# Створіть список пар чисел, де різниця між першим і другим числом буде від 1 до 5, а сума пари буде простим числом.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


pairs_sum_prime = [(a, b) for a in range(1, 11) for b in range(a + 1, a + 6) if is_prime(a + b)]

print(pairs_sum_prime)
