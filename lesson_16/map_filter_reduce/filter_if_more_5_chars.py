# Відфільтрувати слова у реченні, які мають більше 5 букв, використовуючи filter.
strings = ['hello world', 'world hello', 'its', 'a', 'task', 'with', 'map', 'function']
filtered = list(filter(lambda word: len(word) > 5, strings))

print(filtered)
