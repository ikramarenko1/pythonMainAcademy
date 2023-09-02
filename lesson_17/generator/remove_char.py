# Видалення символів: Реалізуйте генератор для видалення певного символу з рядка.
def remove_char(string, char_to_remove):
    for char in string:
        if char != char_to_remove:
            yield char


string = 'Hello, World!'
char_to_remove = 'l'

remove_char_generator = remove_char(string, char_to_remove)

new_string = ''.join([char for char in remove_char_generator])

print(new_string)
