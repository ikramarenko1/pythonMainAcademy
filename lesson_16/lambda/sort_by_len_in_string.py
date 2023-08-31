# Відсортуйте слова у реченні за їх довжиною використовуючи лямбда-функцію та sorted.
import re

sort_words = lambda words: ' '.join(sorted(words, key=len))

string = input('Введiть рядок для тесту: ')  # hello world its a task with lambda function
words = re.sub(r'[.,?!]', '', string).split()

print(sort_words(words))
