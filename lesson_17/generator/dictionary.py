# Словники зі списку ключів та значень: Напишіть генератор для створення словника зі списку
# ключів та відповідних значень.
def generate_dictionary(keys, values):
    for key, value in zip(keys, values):
        yield {key: value}


keys = ['name', 'age', 'lang', 'job']
values = ['Ilya', 20, 'ua', 'IT']

dictionary_generator = generate_dictionary(keys, values)

result_dictionary = {key: value for dictionary in dictionary_generator for key, value in dictionary.items()}

print(result_dictionary)
