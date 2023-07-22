# Завдання 6: Об'єднати два словники
# Опис: Напишіть програму, яка приймає два словники (dictionary1 і dictionary2) і
# об'єднує їх в один словник. Використайте цю програму, щоб об'єднати два словники.

fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
more_fruits = {"grapes": "purple", "lime": "green"}

fruits.update(more_fruits)

print(fruits)
