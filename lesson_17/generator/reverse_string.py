# Обернений рядок: Створіть генератор, який буде повертати рядки зі списку у зворотньому порядку.
def reverse_strings(lst):
    for string in lst:
        yield string[::-1]


strings = ['hello', 'world', 'its', 'a', 'test']

strings_reverser = reverse_strings(strings)

for _ in range(len(strings)):
    print(next(strings_reverser))
