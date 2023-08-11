# Таблиця множення: Вивести на екран таблицю множення для заданого числа.

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


n = int(input("Введіть число для якого потрібно вивести таблицю множення: "))

print_multiplication_table(n)
