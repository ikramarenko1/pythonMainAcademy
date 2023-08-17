# Завдання: Формування словника зі списку рядків
# Дано список рядків. Створіть словник, де ключами будуть рядки,
# а значеннями - словники, що містять кількість входжень кожної літери в рядок.
import re

sentences = ['Hello world', 'Hello world is', 'beautiful from', 'Hello from', 'the other side', 'beautiful']
result_dict = {sentence: {} for sentence in sentences}

for sentence in sentences:
    words = re.sub(r'[.,?!]', '', sentence.lower()).split()
    letters = sorted(set([char for word in words for char in word]))

    result_dict[sentence] = {letter: sentence.lower().count(letter) for letter in letters}

print(result_dict)
