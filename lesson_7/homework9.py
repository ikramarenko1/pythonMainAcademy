# Завдання 9: Видалити спільні елементи зі словника
# Опис: Напишіть програму, яка приймає два словники (dictionary1 і dictionary2) і видаляє спільні елементи
# (ключі та значення) з першого словника. Використайте цю програму, щоб видалити спільні елементи зі словника.
def new_dict_without_identical_keys(dictionary1, dictionary2):
    temp = []
    for key in dictionary1:
        if key in dictionary2 and dictionary1[key] == dictionary2[key]:
            temp.append(key)

    for key in temp:
        del dictionary1[key]

    return dictionary1


fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
more_fruits = {"grapes": "purple", "lime": "green", "orange": "orange", "apple": "red"}

print(new_dict_without_identical_keys(fruits, more_fruits))  # {"banana": "yellow"}
