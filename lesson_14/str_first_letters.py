# Рядок з першими літерами: Напишіть функцію, яка приймає рядок і повертає новий рядок
# з першими літерами кожного слова.
import re


def get_string_from_first_letters(string):
    string = re.sub(r'[.,?!]', '', string).split()
    first_letters = [word[0] for word in string]

    return ''.join(first_letters)


user_input = input('Введiть рядок для тесту: ')
print(f'Результат: {get_string_from_first_letters(user_input)}')
