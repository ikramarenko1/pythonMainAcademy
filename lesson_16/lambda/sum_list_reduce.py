# Знайдіть суму всіх елементів списку за допомогою лямбда-функції та reduce.
from functools import reduce

get_sum = lambda lst: reduce(lambda x, y: x + y, lst)

lst = [1, 2, 3, 4, 5]

print(get_sum(lst))