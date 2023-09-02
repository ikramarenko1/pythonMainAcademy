# Об'єднання списків: Створіть генератор, який об'єднає декілька списків в один.
def concatenate_lists(*args):
    for lst in args:
        for item in lst:
            yield item


lst1 = [1, 2, 3]
lst2 = [2, 3, 4]
lst3 = [3, 4, 5]
lst4 = [4, 5, 6]

concatenate_lists_generator = concatenate_lists(lst1, lst2, lst3, lst4)

concatenated_list = [item for item in concatenate_lists_generator]

print(concatenated_list)
