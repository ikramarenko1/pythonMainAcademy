# Завдання 8: Отримати словник зі спільними ключами та значеннями
# Опис: Напишіть програму, яка приймає два словники (dictionary1 і dictionary2) і повертає новий словник,
# що містить тільки спільні ключі та відповідні їм значення. Використайте цю програму, щоб отримати новий
# словник зі спільними ключами та значеннями.

def new_dict_with_identical_keys(dictionary1, dictionary2):
    result = {}
    for key in dictionary1:
        if key in dictionary2 and dictionary1[key] == dictionary2[key]:
            result[key] = dictionary1[key]

    return result


fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
more_fruits = {"grapes": "purple", "lime": "green", "orange": "orange", "apple": "red"}
print(new_dict_with_identical_keys(fruits, more_fruits))
