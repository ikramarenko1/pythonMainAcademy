# Завдання: Створення словника з пар чисел
# Дано два списки: один містить ключі, інший - відповідні значення.
# Створіть словник, використовуючи ці два списки, за допомогою Dictionary Comprehension.
keys = ['key1', 'key2', 'key3', 'key4']
values = ['value1', 'value2', 'value3', 'value4']

dictionary = {key: value for key, value in zip(keys, values)}

print(dictionary)
