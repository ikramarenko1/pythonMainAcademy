# Завдання: Формування словника з підрахунком букв у словах
# Дано список слів. Створіть словник, де ключами будуть слова, а значеннями - словники,
# де ключами будуть букви, а значеннями - кількість входжень цих букв у відповідне слово.

words = ['hello', 'world', 'it', 'hello', 'world', 'test', 'lets', 'do', 'test', 'test', 'it', 'it', 'it', 'apple', 'bio']
unique_words = set(words)

dict_words = {word: {char: word.count(char) for char in word} for word in unique_words}

print(dict_words)
