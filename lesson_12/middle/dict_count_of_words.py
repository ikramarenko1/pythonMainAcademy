# Завдання: Підрахунок частоти входження слів
# Дано список слів. Створіть словник, де ключами будуть слова, а значеннями - кількість їх входжень у початковий список.

words = ['hello', 'world', 'it', 'hello', 'world', 'test', 'lets', 'do', 'test', 'test', 'it', 'it', 'it', 'apple', 'bio']
words_dict = {word: words.count(word) for word in set(words)}

print(words_dict)
