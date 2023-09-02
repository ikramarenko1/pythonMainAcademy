# Об'єднання рядків зі списку: Реалізуйте генератор для об'єднання рядків зі списку в один.
def concatenate_strings(lst):
    for string in lst:
        for char in string:
            yield char


strings = ['Hello, ', 'World! ', 'It`s ', 'a ', 'test.']

strings_concatenation = concatenate_strings(strings)
concatenated_string = ''.join([string for string in strings_concatenation])

print(concatenated_string)
