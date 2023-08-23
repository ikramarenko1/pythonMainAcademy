# Пошук кількості слів: Напишіть функцію, яка підраховує кількість слів у заданому рядку.
import re


def get_words_count(string):
    string = re.sub(r'[.,?!]', '', string).split()

    return len(string)


user_input = input('Введiть рядок для тесту: ')
print(f'Результат: {get_words_count(user_input)} слiв')
