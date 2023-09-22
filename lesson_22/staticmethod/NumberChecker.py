# Перевірка на просте число: Реалізуйте статичний метод для визначення, чи є задане число простим.
class NumberChecker:
    @staticmethod
    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True


number = int(input("Введіть число для перевірки: "))

if NumberChecker.is_prime(number):
    print(f"{number} є простим.")
else:
    print(f"{number} не є простим.")
