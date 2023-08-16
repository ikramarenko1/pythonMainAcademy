# Завдання: Підрахунок букв у рядку
# Дано рядок. Створіть словник, де ключами будуть букви, а значеннями - кількість їх входжень у рядок.
import re

user_str = str(input('Введiть рядок для пiдрахунку кiлькостi лiтер в ньому: '))
words = re.sub(r'[.,?!]', '', user_str).split()

letters = sorted(set([char for word in words for char in word]))

letters_dict = {letter: user_str.count(letter) for letter in letters}

print(letters_dict)
