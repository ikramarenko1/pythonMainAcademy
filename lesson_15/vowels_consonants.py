# Задача з рядками: Напишіть функцію, яка приймає рядок і підраховує кількість голосних
# та приголосних букв у ньому.
import re


def count_vowels_consonants(string):
    vowels = ['a', 'e', 'i', 'o', 'u',
              'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']

    vowels_in_string = {letter: string.lower().count(letter) for letter in string.lower() if letter in vowels}
    consonants_in_string = {letter: string.lower().count(letter) for letter in string.lower() if letter not in vowels}

    return vowels_in_string, consonants_in_string


user_input = input('Введiть рядок для тесту: ')
user_input = re.sub(r'[.,?!]', '', user_input)

print(f'Результат: {count_vowels_consonants(user_input)}')
