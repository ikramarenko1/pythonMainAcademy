# Словники: Створіть програму, яка приймає рядок від користувача та підраховує кількість кожної літери
# в рядку, записуючи результат у словник, де ключі - літери, а значення - кількість їх зустрічань.
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