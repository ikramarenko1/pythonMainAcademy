# Завдання: Пошук найбільш часто зустрічаючих слів у списку речень
# Дано список речень. Знайдіть топ-3 найбільш часто зустрічаючих слів у всьому
# списку, і виведіть їх разом з кількістю входжень.

sentences = ['Hello world', 'Hello world is beautiful', 'Hello from the other side beautiful']

words = [word.lower() for sentence in sentences for word in sentence.split()]
words_count = {word: words.count(word) for word in words}

top_3_words = sorted(words_count.items(), key=lambda word: word[1], reverse=True)[:3]

print(top_3_words)
