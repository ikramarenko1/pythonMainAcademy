# Обчислити середнє арифметичне елементів списку використовуючи reduce.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

average = lambda lst: reduce(lambda x, y: x + y, lst) / len(lst)

print(average(numbers))
