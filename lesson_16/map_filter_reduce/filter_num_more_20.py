# Відфільтрувати числа у списку, які більше за 20, використовуючи filter.
import random

lst = [random.randint(1, 51) for _ in range(1, 21)]
filtered_lst = list(filter(lambda num: num > 20, lst))

print(lst)
print(filtered_lst)
