# Створіть список, додайте до нього декілька елементів,
# і потім зробіть його копію за допомогою зрізу та методу list.copy().
# Змініть значення в одному списку і переконайтеся, що другий список залишився незмінним.

original_list = [1, 2, 3, 4, 5]

copied_list1 = original_list[:]
copied_list2 = original_list.copy()

copied_list1[0] = 6
copied_list2[0] = 7

print(original_list)
print(copied_list1)
print(copied_list2)
