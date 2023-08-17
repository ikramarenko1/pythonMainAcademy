# Завдання: Видалення схожих слів із різних мов
# Дано два списка слів - один англійською, інший французькою. Створіть список слів,
# які не мають подібних варіантів у іншій мові (наприклад, "chat" - "cat").

def get_unique_words(words_geo1, words_geo2):
    unique_words_geo1 = []
    unique_words_geo2 = []

    for word_geo1 in words_geo1:
        if not any(word_geo2 in word_geo1 or word_geo1 in word_geo2 for word_geo2 in words_geo2):
            unique_words_geo1.append(word_geo1)

    for word_geo2 in words_geo2:
        if not any(word_geo1 in word_geo2 or word_geo2 in word_geo1 for word_geo1 in words_geo1):
            unique_words_geo2.append(word_geo2)

    return unique_words_geo1, unique_words_geo2


english_words = ["cat", "dog", "bird", "chat", "mouse"]
french_words = ["chat", "chien", "oiseau", "souris", "dog"]

unique_english_words, unique_french_words = get_unique_words(english_words, french_words)

print(f'Унiкальнi слова з англiйскої мови: {unique_english_words}')
print(f'Унiкальнi слова з францзуської мови: {unique_french_words}')
