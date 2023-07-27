# Підрахувати кількість слів у файлі
# Опис: Напишіть програму, яка відкриває файл і підраховує кількість слів у ньому.
# Слова вважаються окремими рядками, розділеними пробілами, комами або крапками.
def get_count_of_word(filename, word):
    with open(filename, 'r') as file:
        data = file.read()

    return data.count(word)


print(get_count_of_word('words.txt', 'string'))
