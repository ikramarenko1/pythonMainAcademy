# Обрізка рядка: Напишіть генератор, який буде обрізати заданий рядок до певної довжини.
def cut_the_string(string, length):
    result = ''

    for char in string:
        if len(result) < length:
            result += char
            yield result


string = 'Hello, World!'
length = 5

string_cutter = cut_the_string(string, length)
string_cutter_lst = [string for string in string_cutter]

new_string = string_cutter_lst[-1]

print(new_string)
