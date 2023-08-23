# Підрахунок геометричної прогресії: Напишіть функцію, яка обчислює суму
# перших n членів геометричної прогресії.

def geometric_sum(first, denominator, n):
    if denominator == 1:
        return first * n
    else:
        return first * (denominator**n - 1) / (denominator - 1)


first = float(input("Введіть перший член прогресії: "))
denominator = float(input("Введіть знаменник прогресії: "))
n = int(input("Введіть кількість членів: "))

print(f"Сума перших {n} членів геометричної прогресії дорівнює: {geometric_sum(first, denominator, n)}")
