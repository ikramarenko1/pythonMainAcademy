# Перетворіть список рядків на список їх довжин за допомогою лямбда-функції.
get_len_strings = lambda string: len(string)

strings = ['hello', 'world', 'its', 'a', 'task', 'with', 'lambda', 'function']
len_strings = [get_len_strings(string) for string in strings]

print(strings)
print(len_strings)
