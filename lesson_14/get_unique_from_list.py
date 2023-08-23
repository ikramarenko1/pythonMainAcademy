# Пошук унікальних елементів: Напишіть функцію, яка видаляє дублікати зі списку
# і повертає список унікальних елементів.

def get_unique(*args):
    return list(set(*args))


example_list = [1, 2, 3, 4, 4, 4, 3, 5]
print(get_unique(example_list))
