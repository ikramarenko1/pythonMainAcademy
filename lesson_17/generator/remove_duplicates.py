# Видалення дублікатів: Реалізуйте генератор, який буде забирати дублікати зі списку.
def remove_duplicates(lst):
    have_been = set()

    for item in lst:
        if item not in have_been:
            have_been.add(item)
            yield item


numbers = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 1, 2, 3, 4, 5]
unique_numbers_generator = remove_duplicates(numbers)

unique_numbers = [num for num in unique_numbers_generator]

print(unique_numbers)
