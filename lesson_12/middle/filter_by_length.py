# Завдання: Відфільтрувати слова за довжиною
# Дано список слів. Створіть список, який містить слова, довжина яких становить
# більше середньої довжини всіх слів в початковому списку.

words = ['hello', 'world', 'it', 'is', 'a', 'test', 'lets', 'do', 'filter', 'by', 'length']
average = 0

for word in words:
    average += len(word)

average //= len(words)
words_more_than_average = [word for word in words if len(word) > 3]

print(words_more_than_average)
