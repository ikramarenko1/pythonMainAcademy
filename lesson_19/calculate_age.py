# Створіть функцію, яка приймає два аргументи - дату народження та поточну дату. Функція має обчислити вік особи на
# момент поточної дати.
from datetime import datetime


def calculate_age(birthdate, currentdate):
    age = currentdate.year - birthdate.year

    if (currentdate.month, currentdate.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age


while True:
    birthdate = input('Введiть дату народження в форматi "рiк-мiсяць-день": ')

    try:
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        break
    except ValueError:
        print('Введiть коректну дату!')
    except Exception as e:
        print(f'Виникла помилка - {e}')

currentdate = datetime.now().date()

print(f'Вам {calculate_age(birthdate, currentdate)} рокiв!')
