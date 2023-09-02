# Видалення спеціальних символів: Реалізуйте генератор для видалення спеціальних символів з рядка.
def delete_special_symbols(string):
    for char in string:
        if char not in '.,!?@#$%^&*()':
            yield char


string = 'Hello, World! It`s a test.'

delete_special_symbols_generator = delete_special_symbols(string)

new_string = ''.join([char for char in delete_special_symbols_generator])

print(new_string)
