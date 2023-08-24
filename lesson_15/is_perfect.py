# Задача з числами: Реалізуйте функцію, яка перевіряє, чи є задане число
# досконалим (рівним сумі своїх дільників, крім самого себе).
def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


user_input = int(input("Введіть число: "))  # 28: 1, 2, 4, 7, 14

if is_perfect(user_input):
    print(f"Число {user_input} є досконалим!")
else:
    print(f"Число {user_input} не є досконалим.")
