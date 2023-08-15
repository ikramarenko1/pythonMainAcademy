# Завдання: Генерація списку квадратних коренів
# Створіть список, що містить квадратні корені чисел від 1 до 6, за допомогою List Comprehension.
import math

sqrts = [math.sqrt(num) for num in range(1, 7)]

print(sqrts)
