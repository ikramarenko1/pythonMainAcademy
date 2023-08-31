# Обчислити суму елементів списку використовуючи reduce.
from functools import reduce

sum_of_elements = lambda lst: reduce(lambda x, y: x + y, lst)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum_of_elements(lst))
