# Сума цифр числа: Обчислити суму цифр заданого числа.

def get_sum_of_digits(n):
    total = 0

    while n:
        total += n % 10
        n = n // 10

    return total


number = int(input("Введіть число: "))

print(f"Сума цифр числа {number} дорівнює {get_sum_of_digits(number)}")
