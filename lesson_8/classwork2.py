# Створіть словник, додайте до нього декілька ключів та значень,
# і потім зробіть його копію за допомогою методу dict.copy().
# Змініть значення для одного ключа в одному словнику і переконайтеся,
# що значення в другому словнику залишилися незмінними.

fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
copied_fruits = fruits.copy()

fruits['apple'] = 'green'

print(fruits)
print(copied_fruits)
