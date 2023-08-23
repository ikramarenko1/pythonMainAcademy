# Перевірка простого числа: Напишіть функцію, яка перевіряє, чи є дане число простим.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


number = int(input("Введіть число для перевірки: "))

if is_prime(number):
    print(f"{number} є простим.")
else:
    print(f"{number} не є простим.")

