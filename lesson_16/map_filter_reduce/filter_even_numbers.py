# Відфільтрувати парні числа зі списку використовуючи filter.
even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(even(lst))
