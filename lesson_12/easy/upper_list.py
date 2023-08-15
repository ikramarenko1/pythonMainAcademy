# Завдання: Створення списку з великими літерами
# Дано список слів. Створіть список, де кожне слово записано великими літерами, за допомогою List Comprehension.

words = ('hello', 'world', 'it', 'is', 'a', 'test')
uppercase_words = [word.upper() for word in words]

print(uppercase_words)
