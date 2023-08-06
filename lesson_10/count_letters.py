# 2. Задача: Визначення частоти символів
# Опис: Напишіть програму, яка підраховує кількість кожного символу в рядку і виводить результат у вигляді словника.

def count_letters(user_str):
    result = {}

    for char in user_str.lower():
        if bool(result.get(char)):
            result[char] += 1
            continue

        result[char] = 1

    for key, value in result.items():
        print(f'{key}: {value}')

    return result


user_string = str(input('Введiть рядок для пiдрахунку кiлькостi лiтер: '))
count_letters(user_string)
