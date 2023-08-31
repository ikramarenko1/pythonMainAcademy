# Видаліть дублікати зі списку за допомогою лямбда-функції та set.
delete_duplicates = lambda lst: list(set(lst))

lst = [1, 2, 3, 1, 1, 4, 5, 6]
print(delete_duplicates(lst))
