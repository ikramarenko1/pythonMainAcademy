# Об'єднайте два списки в один за допомогою лямбда-функції та reduce.
from functools import reduce

concatenate_lists = lambda lst1, lst2: reduce(lambda x, y: x + y, [lst1, lst2])

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8]

print(concatenate_lists(lst1, lst2))