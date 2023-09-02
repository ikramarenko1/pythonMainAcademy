# Фільтрація: Напишіть генератор, який відфільтрує числа менше заданого значення з послідовності.
def filter_list(lst, n):
    for item in lst:
        if item < n:
            yield item


lst = [1, 2, 3, 4, 5]

filter_list_generator = filter_list(lst, 4)

filtered_list = [item for item in filter_list_generator]

print(filtered_list)
