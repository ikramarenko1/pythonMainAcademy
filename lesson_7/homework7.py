# Завдання 7: Перевірити спільні ключі в двох словниках
# Опис: Напишіть програму, яка приймає два словники (dictionary1 і dictionary2) і перевіряє,
# чи містять вони спільні ключі. Використайте цю програму, щоб перевірити наявність спільних
# ключів в двох словниках.

def check_for_identical_keys(dictionary1, dictionary2):
    return any(key in dictionary1 for key in dictionary2)


fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
more_fruits = {"grapes": "purple", "lime": "green", "orange": "orange"}
more_fruits2 = {"grapes": "purple", "lime": "green"}

print(check_for_identical_keys(fruits, more_fruits))  # True
print(check_for_identical_keys(fruits, more_fruits2))  # False
