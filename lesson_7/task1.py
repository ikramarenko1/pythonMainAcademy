# Завдання: Перевірити наявність слова в словнику
# Опис: Напишіть програму, яка приймає словник (dictionary) і перевіряє,
# чи міститься певне слово (key) у цьому словнику без використання розгалужень або циклів.
# Приклад вхідних даних: {"apple": 5, "banana": 3, "orange": 2}, "banana"
# Приклад вихідних даних: True

def check_for_key(key, dictionary):
    return True if key in dictionary.keys() else False


fruits = {"apple": 5, "banana": 3, "orange": 2}
print(check_for_key('banana', fruits))
