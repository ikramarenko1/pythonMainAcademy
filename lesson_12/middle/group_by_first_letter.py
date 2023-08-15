# Завдання: Групування слів за першою літерою
# Дано список слів. Створіть словник, де ключами будуть перші літери слів,
# а значеннями - список слів, які починаються з цих літер.

words = ['hello', 'world', 'it', 'is', 'a', 'test', 'lets', 'do', 'filter', 'by', 'length', 'hi', 'woo', 'apple', 'bio']
first_letters = set([word[0] for word in words])

dictionary = {first_letter: [word for word in words if word.startswith(first_letter)] for first_letter in first_letters}

print(dictionary)
