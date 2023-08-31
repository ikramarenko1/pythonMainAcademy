# Відфільтруйте парні числа зі списку використовуючи лямбда-функцію та filter.
import random

is_even = lambda x: x % 2 == 0

lst = [random.randint(1, 21) for _ in range(1, 11)]
filtered_lst = list(filter(is_even, lst))

print(lst)
print(filtered_lst)
