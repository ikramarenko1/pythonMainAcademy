# Завдання: Фільтрація списку слів за довжиною
# Дано список слів. Створіть список, що містить слова з довжиною більше 5 літер, за допомогою List Comprehension.

words = ['some', 'words', 'for', 'example', 'dictionary', 'ohmygod!']
words_more_than_5 = [word for word in words if len(word) > 5]

print(words_more_than_5)
