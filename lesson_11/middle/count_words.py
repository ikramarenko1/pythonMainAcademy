# Підрахунок слів у рядку:
# Попросіть користувача ввести рядок і підрахуйте кількість слів у цьому рядку.
def count_words(string):
    words = {}

    for word in string.lower().split():
        word = word.strip('.,!?')

        if bool(words.get(word)):
            words[word] += 1
            continue

        words[word] = 1

    for word, count in words.items():
        print(f'{word} - {count} шт.')


user_str = str(input('Введiть рядок для пiдрахунку слiв в ньому: '))

count_words(user_str)
