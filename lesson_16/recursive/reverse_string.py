# Створіть рекурсивну функцію для обертання рядка навпаки.

def recursive_string(string):
    if len(string) == 1:
        return string

    return string[-1] + recursive_string(string[:-1])


user_input = input('Введiть рядок для перевiрки: ')

print(recursive_string(user_input))
