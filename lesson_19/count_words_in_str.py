# Створіть функцію, яка приймає текстовий рядок та повертає кількість слів у цьому рядку.

def count_words(string):
    return len(string.split())


user_string = input('Введiть рядок: ')

print(f'Кiлькiсть слiв в вашому рядку: {count_words(user_string)}')
