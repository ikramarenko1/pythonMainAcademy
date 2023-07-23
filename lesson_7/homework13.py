# Завдання 13: Видалити елемент за певним значенням зі словника
# Опис: Напишіть програму, яка приймає словник (dictionary) і видаляє перший елемент, що має певне значення
# (value). Використайте цю програму, щоб видалити елемент зі словника за певним значенням.
def delete_elem_by_value(dictionary, value):
    temp = []
    for d_key, d_value in dictionary.items():
        if d_value == value:
            temp.append(d_key)

    for key in temp:
        del dictionary[key]


fruits = {"apple": "red", "banana": "yellow", "orange": "orange", "grapes": "purple"}

delete_elem_by_value(fruits, "purple")

print(fruits)

