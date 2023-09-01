# Об'єднати два списки за допомогою map.
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

concatenate_lists = lambda lst1, lst2: list(map(lambda x: x, lst1)) + list(map(lambda x: x, lst2))

print(concatenate_lists(lst1, lst2))
