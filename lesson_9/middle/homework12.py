# Операції зі списками: Напишіть функцію, яка приймає список слів та повертає список,
# в якому кожне слово написано задом наперед.

def get_reversed_list(user_list):
    return [word[::-1] for word in user_list]


user_list = input('Введiть слова через пробiл: ').split()
print(get_reversed_list(user_list))
