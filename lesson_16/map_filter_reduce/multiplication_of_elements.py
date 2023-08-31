# Обчислити добуток елементів списку використовуючи reduce.
from functools import reduce

numbers = [1, 2, 3, 4, 5]
multiplication = reduce(lambda x, y: x * y, numbers)

print(multiplication)
