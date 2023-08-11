# Розклад числа на прості множники:
# Попросіть користувача ввести число і розкладіть його на прості множники.

def decompose_into_prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor

        divisor += 1

    return factors


num = int(input("Будь ласка, введіть число для його розкладення на прості множники: "))

prime_factors = decompose_into_prime_factors(num)

print(f"Прості множники числа {num} це: {', '.join(map(str, prime_factors))}.")