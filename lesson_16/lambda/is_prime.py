# Створіть лямбда-функцію для перевірки на простоту числа.
is_prime = lambda x: not any(i for i in range(2, x) if x % i == 0) and x > 1

print(is_prime(7))
print(is_prime(4))
print(is_prime(13))
print(is_prime(1))