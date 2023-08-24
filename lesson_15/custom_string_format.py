# Задача з рядками: Напишіть функцію, яка приймає рядок і повертає рядок,
# де всі слова великими літерами зберігають першу та останню літеру, а
# інші літери в нижньому регістрі.
import re


def custom_format(string):
    formatted = []

    for word in string.split():
        if word.isupper() and len(word) > 2:
            formatted_word = word[0] + word[1:-1].lower() + word[-1]
        else:
            formatted_word = word

        formatted.append(formatted_word)

    return ' '.join(formatted)


user_input = input('Введiть рядок для тесту: ')
user_input = re.sub(r'[.,?!]', '', user_input)

print(f'Результат: {custom_format(user_input)}')
