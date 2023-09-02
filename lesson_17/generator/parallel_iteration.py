# Паралельна ітерація: Створіть генератор, який дозволить ітерувати через два списки паралельно.
def parallel_iteration(lst1, lst2):
    for item1, item2 in zip(lst1, lst2):
        yield(item1, item2)


lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

parallel_iterator = parallel_iteration(lst1, lst2)

parallel_pairs = [pair for pair in parallel_iterator]

print(parallel_pairs)
