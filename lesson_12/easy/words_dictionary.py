# Завдання: Створення словника зі списку
# Дано список слів. Створіть словник, де ключами будуть слова,
# а значеннями - їх довжина, за допомогою Dictionary Comprehension.

words = ('hello', 'world', 'it', 'is', 'a', 'test')

words_dict = {word: len(word) for word in words}
print(words_dict)
